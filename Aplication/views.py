from django.shortcuts import render, redirect
from .forms import BossForm, MenuForm, CategoryForm, RecipeForm, RestaurantForm, EmployeeForm, AdministrativeForm, ManagerForm, ChefForm, CashierForm, WaiterForm, CustomerForm, PayForm, OrderForm, DishForm, IngredientForm, BillForm
from .models import Boss, Menu, Category, Recipe, Restaurant, Employees, Administrative, Manager, Chef, Cashier, Waiter, Customer, Pay, Order, Dish, Ingredient, Bill
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def Home(request):
    return render(request, 'index.html')

# Views for Boss
def CreateBoss(request):
    if request.method == 'POST':
        boss_form = BossForm(request.POST)
        if boss_form.is_valid():
            boss_form.save()
            return redirect('boss_list')
    else:
        boss_form = BossForm()

    return render(request, 'BossViews/CreateBoss.html', {'Boss_form': boss_form})

def BosList(request):
    bosses = Boss.objects.all()
    return render(request, 'BossViews/BossList.html', {'bosses': bosses})

def EditBoss(request, ID_M):
    error = None
    boss_form = None

    try:
        bosss = Boss.objects.get(ID_M=ID_M)

        if request.method == 'GET':
            boss_form = BossForm(instance=bosss)
        elif request.method == 'POST':
            boss_form = BossForm(request.POST, instance=bosss)

            if boss_form.is_valid():
                boss_form.save()
                return redirect('boss_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'BossViews/CreateBoss.html', {'Boss_form': boss_form, 'error': error})

def DeleteBoss(request, ID_M):
    bosss = Boss.objects.get(ID_M = ID_M)
    bosss.delete()
    return redirect('boss_list')

# Views for Menu

def CreateMenu(request):
    if request.method == 'POST':
        menu_form = MenuForm(request.POST)
        if menu_form.is_valid():
            menu_form.save()
            return redirect('menu_list')
    else:
        menu_form = MenuForm()

    return render(request, 'MenuViews/CreateMenu.html', {'menu_form': menu_form})

def MenuList(request):
    menus = Menu.objects.all()
    return render(request, 'MenuViews/MenuList.html', {'menus': menus})

def EditMenu(request, Menu_ID):
    error = None
    menu_form = None

    try:
        menus = Boss.objects.get(Menu_ID=Menu_ID)

        if request.method == 'GET':
            menu_form = MenuForm(instance=menus)
        elif request.method == 'POST':
            menu_form = MenuForm(request.POST, instance=menus)

            if menu_form.is_valid():
                menu_form.save()
                return redirect('menu_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'MenuViews/CreateMenu.html', {'menu_form': menu_form, 'error': error})

def DeleteMenu(request, Menu_ID):
    menus = Menu.objects.get(Menu_ID = Menu_ID)
    menus.delete()
    return redirect('menu_list')

#Views for Category

def CreateCategory(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category_list')
    else:
        category_form = MenuForm()

    return render(request, 'CategoryViews/CreateCategory.html', {'category_form': category_form})

def CategoryList(request):
    categories = Category.objects.all()
    return render(request, 'CategoryViews/CategoryList.html', {'categories': categories})

def EditCategory(request, Cat_ID):
    error = None
    category_form = None

    try:
        categorys = Boss.objects.get(Cat_ID=Cat_ID)

        if request.method == 'GET':
            category_form = CategoryForm(instance=categorys)
        elif request.method == 'POST':
            category_form = CategoryForm(request.POST, instance=categorys)

            if category_form.is_valid():
                category_form.save()
                return redirect('category_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'CategoryViews/CreateCategory.html', {'category_form': category_form, 'error': error})

def DeleteCategory(request, Cat_ID):
    categorys = Menu.objects.get(Cat_ID = Cat_ID)
    categorys.delete()
    return redirect('category_list')

# Views for Recipe
def CreateRecipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('recipe_list')
    else:
        recipe_form = RecipeForm()

    return render(request, 'RecipeViews/CreateRecipe.html', {'recipe_form': recipe_form})

def RecipeList(request):
    recipes = Recipe.objects.all()
    return render(request, 'RecipeViews/RecipeList.html', {'recipes': recipes})

def EditRecipe(request, RecipeID):
    error = None
    recipe_form = None

    try:
        recipes = Recipe.objects.get(RecipeID=RecipeID)

        if request.method == 'GET':
            recipe_form = RecipeForm(instance=recipes)
        elif request.method == 'POST':
            recipe_form = RecipeForm(request.POST, instance=recipes)

            if recipe_form.is_valid():
                recipe_form.save()
                return redirect('recipe_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'RecipeViews/CreateRecipe.html', {'recipe_form': recipe_form, 'error': error})

def DeleteRecipe(request, RecipeID):
    recipes = Recipe.objects.get(RecipeID = RecipeID)
    recipes.delete()
    return redirect('recipe_list')

#Views for Restaurant

def CreateRestaurant(request):
    if request.method == 'POST':
        restaurant_form = RestaurantForm(request.POST)
        if restaurant_form.is_valid():
            restaurant_form.save()
            return redirect('restaurant_list')
    else:
        restaurant_form = RestaurantForm()

    return render(request, 'RestaurantViews/CreateRestaurant.html', {'restaurant_form': restaurant_form})

def RestaurantList(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'RestaurantViews/RestaurantList.html', {'restaurants': restaurants})

def EditRestaurant(request, ID):
    error = None
    restaurant_form = None

    try:
        restaurant = Restaurant.objects.get(ID=ID)

        if request.method == 'GET':
            restaurant_form = RestaurantForm(instance=restaurant)
        elif request.method == 'POST':
            restaurant_form = RestaurantForm(request.POST, instance=restaurant)

            if restaurant_form.is_valid():
                restaurant_form.save()
                return redirect('restaurant_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'RestaurantViews/CreateRestaurant.html', {'restaurant_form': restaurant_form, 'error': error})

def DeleteRestaurant(request, ID):
    restaurants = Restaurant.objects.get(ID = ID)
    restaurants.delete()
    return redirect('restaurant_list')

#Views for Employee
def CreateEmployee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('employee_list')
    else:
        employee_form = EmployeeForm()

    return render(request, 'EmployeeViews/CreateEmployee.html', {'employee_form': employee_form})

def EmployeeList(request):
    employees = Employees.objects.all()
    return render(request, 'EmployeeViews/EmployeeList.html', {'employees': employees})

def EditEmployee(request, EmployeeID):
    error = None
    employee = None

    try:
        employee = Employees.objects.get(EmployeeID=EmployeeID)

        if request.method == 'GET':
            employee_form = EmployeeForm(instance=employee)
        elif request.method == 'POST':
            employee_form = EmployeeForm(request.POST, instance=employee)

            if employee_form.is_valid():
                employee_form.save()
                return redirect('employee_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'EmployeeViews/CreateEmployee.html', {'employee_form': employee_form, 'error': error})

def DeleteEmployee(request, EmployeeID):
    employees = Employees.objects.get(EmployeeID = EmployeeID)
    employees.delete()
    return redirect('employee_list')
# Views for Adminitrative

def CreateAdministrative(request):
    if request.method == 'POST':
        administrative_form = AdministrativeForm(request.POST)
        if administrative_form.is_valid():
            administrative_form.save()
            return redirect('administrative_list')
    else:
        administrative_form = AdministrativeForm()

    return render(request, 'AdministrativeViews/CreateAdministrative.html', {'administrative_form': administrative_form})

def AdministrativeList(request):
    administratives = Administrative.objects.all()
    return render(request, 'AdministrativeViews/AdministrativeList.html', {'administratives': administratives})

def EditAdministrative(request, Admin_ID):
    error = None
    administrative = None

    try:
        administrative = Administrative.objects.get(Admin_ID=Admin_ID)

        if request.method == 'GET':
            administrative_form = AdministrativeForm(instance=administrative)
        elif request.method == 'POST':
            administrative_form = AdministrativeForm(request.POST, instance=administrative)

            if administrative_form.is_valid():
                administrative_form.save()
                return redirect('administrative_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'AdministrativeViews/CreateAdministrative.html', {'administrative_form': administrative_form, 'error': error})

def DeleteAdministrative(request, Admin_ID):
    administratives = Administrative.objects.get(Admin_ID = Admin_ID)
    administratives.delete()
    return redirect('administrative_list')

# Views for Manager
def CreateManager(request):
    if request.method == 'POST':
        manager_form = ManagerForm(request.POST)
        if manager_form.is_valid():
            manager_form.save()
            return redirect('manager_list')
    else:
        manager_form = ManagerForm()

    return render(request, 'ManagerViews/CreateManager.html', {'manager_form': manager_form})

def ManagerList(request):
    managers = Manager.objects.all()
    return render(request, 'ManagerViews/ManagerList.html', {'managers': managers})

def EditManager(request, Manager_ID):
    error = None
    manager_form = None

    try:
        managers = Manager.objects.get(Manager_ID=Manager_ID)

        if request.method == 'GET':
            manager_form = ManagerForm(instance=managers)
        elif request.method == 'POST':
            manager_form = ManagerForm(request.POST, instance=managers)

            if manager_form.is_valid():
                manager_form.save()
                return redirect('manager_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'ManagerViews/CreateManager.html', {'manager_form': manager_form, 'error': error})

def DeleteManager(request, Manager_ID):
    managers = Manager.objects.get(Manager_ID = Manager_ID)
    managers.delete()
    return redirect('manager_list')

#Views for Chef
def CreateChef(request):
    if request.method == 'POST':
        chef_form = ChefForm(request.POST)
        if chef_form.is_valid():
            chef_form.save()
            return redirect('chef_list')
    else:
        chef_form = ChefForm()

    return render(request, 'ChefViews/CreateChef.html', {'chef_form': chef_form})

def ChefList(request):
    chefs = Chef.objects.all()
    return render(request, 'ChefViews/ChefList.html', {'chefs': chefs})

def EditChef(request, Chef_ID):
    error = None
    chef_form = None

    try:
        chefs = Chef.objects.get(Chef_ID=Chef_ID)

        if request.method == 'GET':
            chef_form = ChefForm(instance=chefs)
        elif request.method == 'POST':
            chef_form = ChefForm(request.POST, instance=chefs)

            if chef_form.is_valid():
                chef_form.save()
                return redirect('chef_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'ChefViews/CreateChef.html', {'chef_form': chef_form, 'error': error})

def DeleteChef(request, Chef_ID):
    chefs = Chef.objects.get(Chef_ID = Chef_ID)
    chefs.delete()
    return redirect('chef_list')

#Views for Cashier
def CreateCashier(request):
    if request.method == 'POST':
        cashier_form = CashierForm(request.POST)
        if cashier_form.is_valid():
            cashier_form.save()
            return redirect('cashier_list')
    else:
        cashier_form = CashierForm()

    return render(request, 'CashierViews/CreateCashier.html', {'cashier_form': cashier_form})

def CashierList(request):
    cashiers = Cashier.objects.all()
    return render(request, 'CashierViews/CashierList.html', {'cashiers': cashiers})

def EditCashier(request, Cashier_ID):
    error = None
    cashier_form = None

    try:
        cashiers = Cashier.objects.get(Cashier_ID=Cashier_ID)

        if request.method == 'GET':
            cashier_form = CashierForm(instance=cashiers)
        elif request.method == 'POST':
            cashier_form = CashierForm(request.POST, instance=cashiers)

            if cashier_form.is_valid():
                cashier_form.save()
                return redirect('cashier_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'CashierViews/CreateCashier.html', {'cashier_form': cashier_form, 'error': error})

def DeleteCashier(request, Cashier_ID):
    cashiers = Cashier.objects.get(Cashier_ID = Cashier_ID)
    cashiers.delete()
    return redirect('cashier_list')

#Views for Waiter
def CreateWaiter(request):
    if request.method == 'POST':
        waiter_form = WaiterForm(request.POST)
        if waiter_form.is_valid():
            waiter_form.save()
            return redirect('waiter_list')
    else:
        waiter_form = WaiterForm()

    return render(request, 'WaiterViews/CreateWaiter.html', {'waiter_form': waiter_form})

def WaiterList(request):
    waiters = Waiter.objects.all()
    return render(request, 'WaiterViews/WaiterList.html', {'waiters': waiters})

def EditWaiter(request, Waiter_ID):
    error = None
    customer_form = None

    try:
        waiters = Waiter.objects.get(Waiter_ID=Waiter_ID)

        if request.method == 'GET':
            waiter_form = WaiterForm(instance=waiters)
        elif request.method == 'POST':
            waiter_form = WaiterForm(request.POST, instance=waiters)

            if waiter_form.is_valid():
                waiter_form.save()
                return redirect('waiter_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'WaiterViews/CreateWaiter.html', {'waiter_form': waiter_form, 'error': error})

def DeleteWaiter(request, Waiter_ID):
    waiters = Waiter.objects.get(Waiter_ID = Waiter_ID)
    waiters.delete()
    return redirect('waiter_list')


#Views for Customer
def CreateCustomer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('customer_list')
    else:
        customer_form = CustomerForm()

    return render(request, 'CustomerViews/CreateCustomer.html', {'customer_form': customer_form})

def CustomerList(request):
    customers = Customer.objects.all()
    return render(request, 'CustomerViews/CustomerList.html', {'customers': customers})

def EditCustomer(request, Cust_ID):
    error = None
    customer_form = None

    try:
        customers = Customer.objects.get(Cust_ID=Cust_ID)

        if request.method == 'GET':
            customer_form = CustomerForm(instance=customers)
        elif request.method == 'POST':
            customer_form = CustomerForm(request.POST, instance=customers)

            if customer_form.is_valid():
                customer_form.save()
                return redirect('customer_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'CustomerViews/CreateCustomer.html', {'customer_form': customer_form, 'error': error})

def DeleteCustomer(request, Cust_ID):
    customers = Customer.objects.get(Cust_ID = Cust_ID)
    customers.delete()
    return redirect('customer_list')

#Views for Pay
def CreatePay(request):
    if request.method == 'POST':
        pay_form = PayForm(request.POST)
        if pay_form.is_valid():
            pay_form.save()
            return redirect('pay_list')
    else:
        pay_form = PayForm()

    return render(request, 'PayViews/CreatePay.html', {'pay_form': pay_form})

def PayList(request):
    pays = Pay.objects.all()
    return render(request, 'PayViews/PayList.html', {'pays': pays})

def EditPay(request, Payment_ID):
    error = None
    pay_form = None

    try:
        pays = Pay.objects.get(Payment_ID=Payment_ID)

        if request.method == 'GET':
            pay_form = PayForm(instance=pays)
        elif request.method == 'POST':
            pay_form = PayForm(request.POST, instance=pays)

            if pay_form.is_valid():
                pay_form.save()
                return redirect('pay_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'PayViews/CreatePay.html', {'pay_form': pay_form, 'error': error})

def DeletePay(request, Payment_ID):
    pays = Pay.objects.get(Payment_ID = Payment_ID)
    pays.delete()
    return redirect('pay_list')

#Views for Order
def CreateOrder(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('order_list')
    else:
        order_form = OrderForm()

    return render(request, 'OrderViews/CreateOrder.html', {'Order_form': order_form})

def OrderList(request):
    orders = Order.objects.all()
    return render(request, 'OrderViews/OrderList.html', {'orders': orders})

def EditOrder(request, OrderID):
    error = None
    order_form = None

    try:
        orders = Order.objects.get(OrderID=OrderID)

        if request.method == 'GET':
            order_form = OrderForm(instance=orders)
        elif request.method == 'POST':
            order_form = OrderForm(request.POST, instance=orders)

            if order_form.is_valid():
                order_form.save()
                return redirect('order_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'OrderViews/CreateOrder.html', {'Order_form': order_form, 'error': error})

def DeleteOrder(request, OrderID):
    orders = Order.objects.get(OrderID = OrderID)
    orders.delete()
    return redirect('order_list')

#Views for Dish
def CreateDish(request):
    if request.method == 'POST':
        dish_form = DishForm(request.POST)
        if dish_form.is_valid():
            dish_form.save()
            return redirect('dish_list')
    else:
        dish_form = DishForm()

    return render(request, 'DishViews/CreateDish.html', {'Dish_form': dish_form})

def DishList(request):
    dishs = Dish.objects.all()
    return render(request, 'DishViews/DishList.html', {'dishs': dishs})

def EditDish(request, Dish_ID):
    error = None
    dish_form = None

    try:
        dishs = Dish.objects.get(Dish_ID=Dish_ID)

        if request.method == 'GET':
            dish_form = DishForm(instance=dishs)
        elif request.method == 'POST':
            dish_form = DishForm(request.POST, instance=dishs)

            if dish_form.is_valid():
                dish_form.save()
                return redirect('dish_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'DishViews/CreateDish.html', {'Dish_form': dish_form, 'error': error})

def DeleteDish(request, Dish_ID):
    dishs = Dish.objects.get(Dish_ID = Dish_ID)
    dishs.delete()
    return redirect('dish_list')

#Views for Ingredients
def CreateIngredients(request):
    if request.method == 'POST':
        ingredients_form = IngredientForm(request.POST)
        if ingredients_form.is_valid():
            ingredients_form.save()
            return redirect('ingredients_list')
    else:
        ingredients_form = IngredientForm()

    return render(request, 'IngredientsViews/CreateIngredients.html', {'Ingredient_form': ingredients_form})

def IngredientsList(request):
    ingredientss = Ingredient.objects.all()
    return render(request, 'IngredientsViews/IngredientsList.html', {'ingredientss': ingredientss})

def EditIngredients(request, Ingredients_ID):
    error = None
    ingredients_form = None

    try:
        ingredientss = Ingredient.objects.get(Ingredients_ID=Ingredients_ID)

        if request.method == 'GET':
            ingredients_form = IngredientForm(instance=ingredientss)
        elif request.method == 'POST':
            ingredients_form = IngredientForm(request.POST, instance=ingredientss)

            if ingredients_form.is_valid():
                ingredients_form.save()
                return redirect('ingredients_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'IngredientsViews/CreateIngredients.html', {'Ingredient_form': ingredients_form, 'error': error})

def DeleteIngredients(request, Ingredients_ID):
    ingredientss = Ingredient.objects.get(Ingredients_ID = Ingredients_ID)
    ingredientss.delete()
    return redirect('ingredients_list')

# Views for Bill
def CreateBill(request):
    if request.method == 'POST':
        bill_form = BillForm(request.POST)
        if bill_form.is_valid():
            bill_form.save()
            return redirect('bill_list')
    else:
        bill_form = BillForm()

    return render(request, 'BillViews/CreateBill.html', {'Bill_form': bill_form})

def BillList(request):
    bills = Bill.objects.all()
    return render(request, 'BillViews/BillList.html', {'bills': bills})

def EditBill(request, Bill_ID):
    error = None
    bill_form = None

    try:
        bills = Bill.objects.get(Bill_ID=Bill_ID)

        if request.method == 'GET':
            bill_form = BillForm(instance=bills)
        elif request.method == 'POST':
            bill_form = BillForm(request.POST, instance=bills)

            if bill_form.is_valid():
                bill_form.save()
                return redirect('bill_list')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'BillViews/CreateBill.html', {'Bill_form': bill_form, 'error': error})

def DeleteBill(request, Bill_ID):
    bills = Bill.objects.get(Bill_ID = Bill_ID)
    bills.delete()
    return redirect('bill_list')
