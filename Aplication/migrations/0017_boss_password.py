# Generated by Django 4.2.7 on 2023-12-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0016_alter_recipe_recipeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='Password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
