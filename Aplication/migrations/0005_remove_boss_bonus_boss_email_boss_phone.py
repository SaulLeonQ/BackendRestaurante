# Generated by Django 4.2.7 on 2023-11-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0004_boss_bonus_boss_hire_date_boss_name_menu_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boss',
            name='Bonus',
        ),
        migrations.AddField(
            model_name='boss',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='boss',
            name='Phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
