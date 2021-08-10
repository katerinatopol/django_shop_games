from django.db import models

from shop_games import settings
from mainapp.models import Games


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )
    game = models.ForeignKey(
        Games,
        on_delete=models.CASCADE,
    )
    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )
    is_deleted = models.BooleanField(default=False)

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    @property
    def product_cost(self):
        return self.game.price

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = len(_items)
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost

    def delete(self):
        self.game.quantity += self.quantity
        self.game.save()
        super(self.__class__, self).delete()

    def save(self, *args, **kwargs):
        if self.pk:
            self.game.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.game.quantity -= self.quantity

        self.game.save()
        super(self.__class__, self).save(*args, **kwargs)