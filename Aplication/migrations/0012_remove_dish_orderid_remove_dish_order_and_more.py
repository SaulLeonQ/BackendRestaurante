# Generated by Django 4.2.7 on 2023-12-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0011_pay_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='OrderID',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='order',
        ),
        migrations.AddField(
            model_name='dish',
            name='popularity_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='dishes',
            field=models.ManyToManyField(to='Aplication.dish'),
        ),
    ]
