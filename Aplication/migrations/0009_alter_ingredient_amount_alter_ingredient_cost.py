# Generated by Django 4.2.7 on 2023-12-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0008_alter_ingredient_amount_alter_ingredient_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='Amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Cost',
            field=models.FloatField(null=True),
        ),
    ]