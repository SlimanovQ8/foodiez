# Generated by Django 4.1 on 2022-08-13 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_recipe_descreption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='descreption',
            new_name='description',
        ),
    ]
