from django.contrib import admin
from .models import GamesCategory, Games, Image

admin.site.register(GamesCategory)
admin.site.register(Games)
admin.site.register(Image)


@admin.register(Games)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        # 'quantity',
        'created',
    ]