from django.db import models


class GamesCategory(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=64,
        unique=True
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    is_deleted = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name or f"Game with id - {self.pk}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Games(models.Model):
    category = models.ForeignKey(
        GamesCategory,
        on_delete=models.CASCADE,
        verbose_name='категория',
    )
    name = models.CharField(
        verbose_name='название',
        max_length=128,
        unique=True,
    )
    part = models.CharField(
        verbose_name='часть',
        max_length=128,
        blank=True,
    )
    top_image = models.ImageField(
        upload_to='top_product_images',
        blank=True,
        verbose_name='обложка',
    )
    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=100,
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    is_deleted = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name or f"Game with id - {self.pk}"

    class Meta:
        verbose_name = 'игра'
        verbose_name_plural = 'игры'


class Image(models.Model):
    game = models.ForeignKey(
        Games,
        on_delete=models.CASCADE,
        verbose_name='игра',
    )
    image = models.ImageField(
        upload_to='product_images',
        blank=True,
        verbose_name='изображениe',
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения для игр'