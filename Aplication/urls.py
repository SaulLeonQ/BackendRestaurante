from django.urls import path
from .views import CreateBoss, DeleteBoss, EditBoss, BosList, MenuList, CreateMenu, EditMenu, DeleteMenu
from .views import CreateCategory, DeleteCategory, EditCategory, CategoryList
from .views import CreateRecipe, DeleteRecipe, EditRecipe, RecipeList
from .views import CreateRestaurant, DeleteRestaurant, EditRestaurant, RestaurantList
from .views import CreateEmployee, DeleteEmployee, EditEmployee, EmployeeList
from .views import CreateAdministrative, DeleteAdministrative, EditAdministrative, AdministrativeList
from .views import CreateManager, DeleteManager, EditManager, ManagerList
from .views import CreateChef, DeleteChef, EditChef, ChefList
from .views import CreateCashier, DeleteCashier, EditCashier, CashierList
from .views import CreateWaiter, DeleteWaiter, EditWaiter, WaiterList
from .views import CreateCustomer, DeleteCustomer, EditCustomer, CustomerList
from .views import CreatePay, DeletePay, EditPay, PayList
from .views import CreateOrder, DeleteOrder, EditOrder, OrderList
from .views import CreateDish, DeleteDish, EditDish, DishList
from .views import CreateIngredients, DeleteIngredients, EditIngredients, IngredientsList
from .views import CreateBill, DeleteBill, EditBill, BillList

app_name = 'managment'

urlpatterns = [
    # Paths for boss
    path('create_boss/', CreateBoss, name='create_boss'),
    path('boss_list/', BosList, name='boss_list'),
    path('edit_boss/<int:ID_M>/', EditBoss, name='edit_boss'),
    path('delete_boss/<int:ID_M>/', DeleteBoss, name='delete_boss'),
    
    #Paths for Menu
    path('create_menu/', CreateMenu, name='create_menu'),
    path('menu_list/', MenuList, name='menu_list'),
    path('edit_menu/<int:Menu_ID>/', EditMenu, name='edit_menu'),
    path('delete_menu/<int:Menu_ID>/', DeleteMenu, name='delete_menu'),
    
    #Paths for Category
    path('create_category/', CreateCategory, name='create_category'),
    path('category_list/', CategoryList, name='category_list'),
    path('edit_category/<int:Cat_ID>/', EditCategory, name='edit_category'),
    path('delete_category/<int:Cat_ID>/', DeleteCategory, name='delete_category'),
    
    #Paths for Recipe
    path('create_recipe/', CreateRecipe, name='create_recipe'),
    path('recipe_list/', RecipeList, name='recipe_list'),
    path('edit_recipe/<int:RecipeID>/', EditRecipe, name='edit_recipe'),
    path('delete_recipe/<int:RecipeID>/', DeleteRecipe, name='delete_recipe'),

    #Paths for Restaurant
    path('create_restaurant/', CreateRestaurant, name='create_restaurant'),
    path('restaurant_list/', RestaurantList, name='restaurant_list'),
    path('edit_restaurant/<int:ID>/', EditRestaurant, name='edit_restaurant'),
    path('delete_restaurant/<int:ID>/', DeleteRestaurant, name='delete_restaurant'),

    #Paths for Employee
    path('create_employee/', CreateEmployee, name='create_employee'),
    path('employee_list/', EmployeeList, name='employee_list'),
    path('managment/edit_employee/<int:EmployeeID>/', EditEmployee, name='edit_employee'),
    path('delete_employee/<int:EmployeeID>/', DeleteEmployee, name='delete_employee'),

    #Paths for Administratives
    path('create_administrative/', CreateAdministrative, name='create_administrative'),
    path('administrative_list/', AdministrativeList, name='administrative_list'),
    path('edit_administrative/<int:Admin_ID>/', EditAdministrative, name='edit_administrative'),
    path('delete_administrative/<int:Admin_ID>/', DeleteAdministrative, name='delete_administrative'),

    #Paths for Manager
    path('create_manager/', CreateManager, name='create_manager'),
    path('manager_list/', ManagerList, name='manager_list'),
    path('edit_manager/<int:Manager_ID>/', EditManager, name='edit_manager'),
    path('delete_manager/<int:Manager_ID>/', DeleteManager, name='delete_manager'),

    #Paths for Chef
    path('create_chef/', CreateChef, name='create_chef'),
    path('chef_list/', ChefList, name='chef_list'),
    path('edit_chef/<int:Chef_ID>/', EditChef, name='edit_chef'),
    path('delete_chef/<int:Chef_ID>/', DeleteChef, name='delete_chef'),

    #Paths for Cashier
    path('create_cashier/', CreateCashier, name='create_cashier'),
    path('cashier_list/', CashierList, name='cashier_list'),
    path('edit_cashier/<int:Cashier_ID>/', EditCashier, name='edit_cashier'),
    path('delete_cashier/<int:Cashier_ID>/', DeleteCashier, name='delete_cashier'),

    #Paths for Waiter
    path('create_waiter/', CreateWaiter, name='create_waiter'),
    path('waiter_list/', WaiterList, name='waiter_list'),
    path('edit_waiter/<int:Waiter_ID>/', EditWaiter, name='edit_waiter'),
    path('delete_waiter/<int:Waiter_ID>/', DeleteWaiter, name='delete_waiter'),

    #Paths for Customer
    path('create_customer/', CreateCustomer, name='create_customer'),
    path('customer_list/', CustomerList, name='customer_list'),
    path('edit_customer/<int:Cust_ID>/', EditCustomer, name='edit_customer'),
    path('delete_customer/<int:Cust_ID>/', DeleteCustomer, name='delete_customer'),

    #Paths for Pay
    path('create_pay/', CreatePay, name='create_pay'),
    path('pay_list/', PayList, name='pay_list'),
    path('edit_pay/<int:Payment_ID>/', EditPay, name='edit_pay'),
    path('delete_pay/<int:Payment_ID>/', DeletePay, name='delete_pay'),

    #Paths for Order
    path('create_order/', CreateOrder, name='create_order'),
    path('order_list/', OrderList, name='order_list'),
    path('edit_order/<int:OrderID>/', EditOrder, name='edit_order'),
    path('delete_order/<int:OrderID>/', DeleteOrder, name='delete_order'),

    #Paths for Dish
    path('create_dish/', CreateDish, name='create_dish'),
    path('dish_list/', DishList, name='dish_list'),
    path('edit_dish/<int:Dish_ID>/', EditDish, name='edit_dish'),
    path('delete_dish/<int:Dish_ID>/', DeleteDish, name='delete_dish'),

    #Paths for Ingredients
    path('create_ingredients/', CreateIngredients, name='create_ingredients'),
    path('ingredients_list/', IngredientsList, name='ingredients_list'),
    path('edit_ingredients/<int:Ingredient_ID>/', EditIngredients, name='edit_ingredients'),
    path('delete_ingredients/<int:Ingredient_ID>/', DeleteIngredients, name='delete_ingredients'),
    
    #Paths for Ingredients
    path('create_bill/', CreateBill, name='create_bill'),
    path('bill_list/', BillList, name='bill_list'),
    path('edit_bill/<int:Bill_ID>/', EditBill, name='edit_bill'),
    path('delete_bill/<int:Bill_ID>/', DeleteBill, name='delete_bill'),
]
