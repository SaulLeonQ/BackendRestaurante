# Generated by Django 4.2.7 on 2023-11-20 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('ID_M', models.AutoField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Cat_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=255)),
                ('MenuID', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('Chef_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField(null=True)),
                ('Employee_Phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Cust_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ContcNumber', models.IntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Age', models.IntegerField(null=True)),
                ('Sex', models.CharField(max_length=20)),
                ('Booking', models.DateField(null=True)),
                ('Phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('Name', models.CharField(max_length=255)),
                ('Age', models.IntegerField(null=True)),
                ('Sex', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('TimeEntry', models.TimeField(null=True)),
                ('Type', models.CharField(max_length=255)),
                ('RestaurantID', models.IntegerField(null=True)),
                ('EmployeeID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('Menu_ID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('RecipeID', models.IntegerField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('Waiter_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField(null=True)),
                ('Employee_Phone', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=20)),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.boss')),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('Method', models.CharField(max_length=255)),
                ('Amount', models.FloatField(null=True)),
                ('Payment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False)),
                ('SaucersN', models.IntegerField(null=True)),
                ('customer_phone', models.CharField(max_length=20)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.chef')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.customer')),
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.waiter')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('Manager_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField(null=True)),
                ('Employee_Phone', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('Ingredient_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Cost', models.FloatField(null=True)),
                ('Amount', models.IntegerField(null=True)),
                ('Expiration', models.DateField(null=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.restaurant'),
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('Dish_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=255)),
                ('Cost', models.FloatField(null=True)),
                ('CategoryID', models.IntegerField(null=True)),
                ('RecipeID', models.IntegerField(null=True)),
                ('OrderID', models.IntegerField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.category')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.order')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='waiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.waiter'),
        ),
        migrations.AddField(
            model_name='chef',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.employees'),
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.menu'),
        ),
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('Cashier_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField(null=True)),
                ('Employee_Phone', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('Amount', models.FloatField(null=True)),
                ('Bill_ID', models.AutoField(primary_key=True, serialize=False)),
                ('customer_phone', models.CharField(max_length=20)),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.cashier')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Administrative',
            fields=[
                ('Admin_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField(null=True)),
                ('Employee_Phone', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aplication.employees')),
            ],
        ),
    ]