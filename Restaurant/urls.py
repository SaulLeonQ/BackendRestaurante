from django.contrib import admin
from Aplication import views
from django.urls import path, include
from Aplication.views import Home, BosList, MenuList, CategoryList, RecipeList, RestaurantList, EmployeeList, AdministrativeList, ManagerList, ChefList, CashierList, WaiterList, CustomerList, PayList, OrderList, DishList, IngredientsList, BillList, LoggedHome
from Aplication.views import CreateBoss, CreateMenu, CreateCategory, CreateRecipe, CreateRestaurant, CreateEmployee, CreateAdministrative, CreateManager, CreateChef, CreateCashier, CreateWaiter, CreateCustomer, CreatePay, CreateOrder, CreateDish, CreateIngredients, CreateBill

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('restaurant/<int:restaurant_id>/', include('Aplication.urls')),
    path('managment/', include('Aplication.urls', namespace='managment')),
    path('home/', Home, name='home_login'),
    path('loggedhome/',LoggedHome, name='loggedhome'),
    path('login/', views.login, name='login'),
    path('boss_list/', BosList, name='boss_list'),
    path('create_boss/<int:restaurant_id>/', CreateBoss, name='create_boss'),
    path('menu_list/',MenuList, name='menu_list'),
    path('create_menu/', CreateMenu, name='create_menu'),
    path('create_category/', CreateCategory, name='create_category'),
    path('category_list/',CategoryList, name='category_list'),
    path('recipe_list/', RecipeList, name='recipe_list'),
    path('create_recipe/', CreateRecipe, name='create_recipe'),
    path('restaurant_list/', RestaurantList, name='restaurant_list'),
    path('create_restaurant/', CreateRestaurant, name='CreateRestaurant'),
    path('create_employee/', CreateEmployee, name='create_employee'),
    path('employee_list/', EmployeeList, name='employee_list'),
    path('create_administrative/', CreateAdministrative, name='create_administrative'),
    path('administrative_list/', AdministrativeList, name='administrative_list'),
    path('create_manager/', CreateManager, name='create_manager'),
    path('manager_list/', ManagerList, name='manager_list'),
    path('create_chef/', CreateChef,name='create_chef'),
    path('chef_list/', ChefList, name='chef_list'),
    path('create_cashier/', CreateCashier,name='create_cashier'),
    path('cashier_list/', CashierList, name='cashier_list'),
    path('create_waiter/', CreateWaiter,name='create_waiter'),
    path('waiter_list/', WaiterList, name='waiter_list'),
    path('create_customer/', CreateCustomer, name='create_customer'),
    path('customer_list/', CustomerList, name='customer_list'),
    path('create_pay/', CreatePay, name='create_pay'),
    path('pay_list/', PayList, name='pay_list'),
    path('create_order/', CreateOrder, name='create_order'),
    path('order_list/', OrderList, name='order_list'),
    path('create_dish/', CreateDish, name='create_dish'),
    path('dish_list/', DishList, name='dish_list'),
    path('create_ingredients/', CreateIngredients, name='create_ingredients'),
    path('ingredients_list/', IngredientsList, name='ingredients_list'),
    path('create_bill/', CreateBill, name='create_bill'),
    path('bill_list/', BillList, name='bill_list'),
]
##urlpatterns = [
##    path('admin/', admin.site.urls),
##    path('home/', include('Aplication.urls', namespace='managment')),
##    path('restaurant/<int:restaurant_id>/', include('Aplication.restaurant_urls')),
##]
