import os
import json

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from mainapp.models import GamesCategory, Games, Image

from authapp.models import ShopUser

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8')as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        GamesCategory.objects.all().delete()
        for category in categories:
            new_category = GamesCategory(**category)
            new_category.save()

        games = load_from_json('games')

        Games.objects.all().delete()
        for game in games:
            category_name = game['category']
            _category = GamesCategory.objects.get(name=category_name)
            game['category'] = _category
            new_category = Games(**game)
            new_category.save()

        images = load_from_json('images')

        Image.objects.all().delete()
        for image in images:
            image_game = image['game']
            _game = Games.objects.get(name=image_game)
            image['game'] = _game
            new_category = Image(**image)
            new_category.save()

        super_user = ShopUser.objects.create_superuser('admin', 'admin@geekshop.local', '123', age="30")
