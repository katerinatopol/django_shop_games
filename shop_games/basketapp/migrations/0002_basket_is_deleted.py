# Generated by Django 3.2.4 on 2021-07-20 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
