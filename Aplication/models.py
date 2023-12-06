from django.db import models

class Boss(models.Model):
    ID_M = models.AutoField(primary_key=True)
    Salary = models.FloatField(null=True)
    Name = models.CharField(max_length=255, null=True)##A
    Hire_Date = models.DateField(null=True)##A
    Email = models.EmailField(null=True)##A
    Phone = models.CharField(max_length=20, null=True)##A
    Password = models.CharField(max_length=128, null=True, blank=True)##A
    def __str__(self) -> str:
        return 'ID: {0}, Name: {1}, Salary: {2}, Hire Date: {3}, Email: {4}, Phone: {5}, Password: {6}'.format(
            self.ID_M, self.Name, self.Salary, self.Hire_Date, self.Email, self.Phone, self.Password)##A

class Menu(models.Model):
    Menu_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null=True)##A
    Description = models.TextField(null=True)##A
    Created_At = models.DateTimeField(null=True)##A
    def __str__(self) -> str:
        return 'ID: {0}, Name: {1}'.format(
            self.Menu_ID, self.Name)

class Category(models.Model):
    Cat_ID = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=255)
    Description = models.CharField(max_length=255, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Cat_ID,self.Type,self.Description,self.menu)

class Recipe(models.Model):
    RecipeID = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=255)
    Name = models.CharField(max_length=255, null=True)##A
    Description = models.TextField(null=True)##A
    PreparationTime = models.DurationField(null=True)##A
    def __str__(self):
        return 'ID: {0}, Name: {1}'.format(
            self.RecipeID,self.Name)##A

class Restaurant(models.Model):
    ID = models.AutoField(primary_key=True, null=False)
    Address = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name

class Employees(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.IntegerField(null=True)
    Sex = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    TimeEntry = models.TimeField(null=True)
    Type = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    EmployeeID = models.AutoField(primary_key=True) 

    def __str__(self) -> str:
        return 'ID: {0}, Name: {1}'.format(self.EmployeeID,self.Name)


class Administrative(models.Model):
    Admin_ID = models.AutoField(primary_key=True)
    Salary = models.FloatField(null=True)
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Admin_ID,self.Salary,self.Employee_Phone,self.employee)

class Manager(models.Model):
    Manager_ID = models.AutoField(primary_key=True)
    Salary = models.FloatField(null=True)
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Manager_ID,self.Salary,self.Employee_Phone)

class Chef(models.Model):
    Chef_ID = models.AutoField(primary_key=True)
    Salary = models.FloatField(null=True)
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Chef_ID,self.Salary,self.Employee_Phone)

class Cashier(models.Model):
    Cashier_ID = models.AutoField(primary_key=True)
    Salary = models.FloatField(null=True)
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Cashier_ID,self.Salary,self.Employee_Phone,self.employee)

class Waiter(models.Model):
    Waiter_ID = models.AutoField(primary_key=True)
    Salary = models.FloatField(null=True)
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Waiter_ID,self.Salary)

class Customer(models.Model):
    Cust_ID = models.AutoField(primary_key=True)
    ContcNumber = models.IntegerField(null=True)
    Name = models.CharField(max_length=255)
    Age = models.IntegerField(null=True)
    Sex = models.CharField(max_length=20, null=True)
    Booking = models.DateField(null=True)
    Phone = models.CharField(max_length=20, null=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Cust_ID,self.Name)

class Dish(models.Model):
    Dish_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null=True)
    Type = models.CharField(max_length=255)
    Cost = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    popularity_count = models.IntegerField(default=0)
    def __str__(self) -> str:
        return '{0}'.format(self.Name,self.Type,self.Cost,self.category,self.recipe)

    def increment_popularity(self):
        self.popularity_count += 1
        self.save()

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    SaucersN = models.IntegerField(null=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)
    def __str__(self) -> str:
        return '{0}'.format(self.OrderID,self.SaucersN,self.waiter,self.chef,self.customer_phone,self.customer)

class Pay(models.Model):
    Payment_ID = models.AutoField(primary_key=True)
    Method = models.CharField(max_length=255)
    Amount = models.FloatField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Transaction_Date = models.DateField(null=True)##A
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return 'ID: {0}, Method: {1}, Amount: {2}, Date: {3}'.format(self.Payment_ID,self.Method,self.Amount,self.Transaction_Date)

    
class Ingredient(models.Model):
    Ingredient_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null=True)
    Cost = models.FloatField(null=True)
    Amount = models.FloatField(null=True)
    Unit = models.CharField(max_length=255, null=True)
    Expiration = models.DateField(null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return 'ID: {0},Name: {1}, Cost: {2}, Amount: {3}, Unit: {4}, Expiration: {5}, recipe: {6}'.format(
            self.Ingredient_ID,self.Name,self.Cost,self.Amount,self.Unit,self.Expiration,self.recipe)


class Bill(models.Model):
    Bill_ID = models.AutoField(primary_key=True)
    cashier = models.ForeignKey(Cashier, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pay = models.ForeignKey(Pay, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return '{0}'.format(self.cashier,self.customer,self.pay)