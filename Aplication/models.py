from django.db import models

class Boss(models.Model):
    ID_M = models.AutoField(primary_key=True)
    Salary = models.FloatField(null=True)
    Name = models.CharField(max_length=255, null=True)##A
    Hire_Date = models.DateField(null=True)##A
    Email = models.EmailField(null=True)##A
    Phone = models.CharField(max_length=20, null=True)##A
    def __str__(self) -> str:
        return 'ID: {0}, Name: {1}, Salary: {2}, Hire Date: {3}, Email: {4}, Phone: {5}'.format(
            self.ID_M, self.Name, self.Salary, self.Hire_Date, self.Email, self.Phone)##A

class Menu(models.Model):
    Menu_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null=True)##A
    Description = models.TextField(null=True)##A
    Created_At = models.DateTimeField(null=True)##A
    def __str__(self) -> str:
        return 'ID: {0}, Name: {1}, Description: {2}, Created At: {3}'.format(
            self.Menu_ID, self.Name, self.Description, self.Created_At)##A

class Category(models.Model):
    Cat_ID = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=255)
    MenuID = models.IntegerField(null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Cat_ID,self.Type,self.menu)

class Recipe(models.Model):
    RecipeID = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=255)
    Name = models.CharField(max_length=255, null=True)##A
    Description = models.TextField(null=True)##A
    PreparationTime = models.DurationField(null=True)##A
    def __str__(self):
        return 'ID: {0}, Type: {1}, Name: {2}, Description: {3}, Preparation Time: {4}'.format(
            self.RecipeID, self.Type, self.Name, self.Description, self.PreparationTime)##A

class Restaurant(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    Address = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Employees(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.IntegerField(null=True)
    Sex = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    TimeEntry = models.TimeField(null=True)
    Type = models.CharField(max_length=255)
    RestaurantID = models.IntegerField(null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    EmployeeID = models.AutoField(primary_key=True) 

    def __str__(self) -> str:
        return f'{self.Name}, {self.Age}, {self.Sex}, {self.Phone}, {self.TimeEntry}, {self.RestaurantID}, {self.restaurant}, {self.EmployeeID}'


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
    Cashier_ID = models.IntegerField(primary_key=True)
    Salary = models.FloatField(null=True)
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Cashier_ID,self.Salary)

class Waiter(models.Model):
    Waiter_ID = models.AutoField(primary_key=True)
    Salary = models.FloatField(null=True)
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Waiter_ID,self.Salary)

class Customer(models.Model):
    Cust_ID = models.AutoField(primary_key=True)
    ContcNumber = models.IntegerField()
    Name = models.CharField(max_length=255)
    Age = models.IntegerField(null=True)
    Sex = models.CharField(max_length=20)
    Booking = models.DateField(null=True)
    Phone = models.CharField(max_length=20)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Cust_ID,self.Name)

class Pay(models.Model):
    Method = models.CharField(max_length=255)
    Amount = models.FloatField(null=True)
    Payment_ID = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Transaction_Date = models.DateTimeField(null=True)##A
    def __str__(self) -> str:
        return '{0}'.format(self.Method,self.Amount)

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    SaucersN = models.IntegerField(null=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.OrderID,self.SaucersN,self.waiter,self.chef,self.customer_phone,self.customer)

class Dish(models.Model):
    Dish_ID = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=255)
    Cost = models.FloatField(null=True)
    CategoryID = models.IntegerField(null=True)
    RecipeID = models.IntegerField(null=True)
    OrderID = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Type,self.Cost,self.Cost,self.category,self.recipe,self.order)
    
class Ingredient(models.Model):
    Ingredient_ID = models.AutoField(primary_key=True)
    Cost = models.FloatField(null=True)
    Amount = models.IntegerField(null=True)
    Expiration = models.DateField(null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Ingredient_ID,self.Cost,self.Amount,self.Expiration,self.recipe)


class Bill(models.Model):
    Amount = models.FloatField(null=True)
    Bill_ID = models.AutoField(primary_key=True)
    cashier = models.ForeignKey(Cashier, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{0}'.format(self.Amount,self.cashier,self.customer)