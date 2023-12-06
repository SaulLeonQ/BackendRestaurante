# Generated by Django 4.2.7 on 2023-12-06 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0021_dish_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='Amount',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='customer_phone',
        ),
        migrations.AddField(
            model_name='bill',
            name='pay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplication.pay'),
        ),
    ]