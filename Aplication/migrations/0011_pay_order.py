# Generated by Django 4.2.7 on 2023-12-03 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0010_ingredient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplication.order'),
        ),
    ]
