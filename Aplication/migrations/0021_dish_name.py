# Generated by Django 4.2.7 on 2023-12-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0020_remove_dish_categoryid_remove_dish_recipeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='Name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
