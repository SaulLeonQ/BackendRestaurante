# Generated by Django 4.2.7 on 2023-11-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0003_alter_bill_bill_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='Bonus',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='boss',
            name='Hire_Date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='boss',
            name='Name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='Created_At',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='Name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pay',
            name='Transaction_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='Name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='PreparationTime',
            field=models.DurationField(null=True),
        ),
    ]