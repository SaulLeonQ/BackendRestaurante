from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import  Boss, Bill, Cashier, Category, Chef, Customer, Dish, Employees, Administrative, Ingredient, Manager, Menu, Order, Pay, Recipe, Restaurant, Waiter

class BossForm(forms.ModelForm):
    class Meta:
        model = Boss
        exclude = ['ID_M']
        fields = ['Salary', 'Name', 'Hire_Date', 'Email', 'Phone']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['Menu_ID', 'Name', 'Description', 'Created_At']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Cat_ID', 'Type', 'MenuID', 'menu']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['RecipeID', 'Type','Name','Description','PreparationTime']
        
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['ID', 'Address', 'Name', 'Phone', 'boss']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['EmployeeID' ,'Name', 'Age', 'Sex', 'Phone', 'TimeEntry', 'Type', 'RestaurantID', 'restaurant']
        labels = {
           'RestaurantID' : 'Restaurant'
        }
        #Combobox for Employees
        def __init__(self, *arg, **kwargs):
            super(EmployeeForm, self).__init__(*arg, **kwargs)
            self.fields['RestaurantID'].queryset = Restaurant.objects.all()

class AdministrativeForm(forms.ModelForm):
    class Meta:
        model = Administrative
        fields = ['Admin_ID', 'Salary', 'Employee_Phone', 'employee']


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['Manager_ID', 'Salary', 'Employee_Phone', 'employee']
        labels ={
            'employee':'Employees'
        }
        #Combobox for Employees
        def __init__(self, *arg, **kwargs):
            super(ManagerForm, self).__init__(*arg, **kwargs)
            self.fields['EmployeeID'].queryset = Employees.objects.all()



class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ['Chef_ID', 'Salary', 'Employee_Phone', 'employee']

class CashierForm(forms.ModelForm):
    class Meta:
        model = Cashier
        fields = ['Cashier_ID', 'Salary', 'Employee_Phone', 'employee']

class WaiterForm(forms.ModelForm):
    class Meta:
        model = Waiter
        fields = ['Waiter_ID', 'Salary', 'Employee_Phone', 'employee']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Cust_ID', 'ContcNumber', 'Name', 'Age', 'Sex', 'Booking', 'Phone', 'waiter']

class PayForm(forms.ModelForm):
    class Meta:
        model = Pay
        fields = ['Method', 'Amount', 'Payment_ID', 'customer']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['OrderID', 'SaucersN', 'waiter', 'chef', 'customer_phone', 'customer']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['Dish_ID', 'Type', 'Cost', 'CategoryID', 'RecipeID', 'OrderID', 'category', 'recipe', 'order']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['Ingredient_ID', 'Cost', 'Amount', 'Expiration', 'recipe']

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['Amount', 'Bill_ID', 'cashier', 'customer_phone', 'customer']