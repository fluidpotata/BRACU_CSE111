''''''
'''
You want to order Burger from Chillox through the FoodPanda App. You have to calculate the total price. Write a function 
which will take the name of the burger and place(Mohakhali/Outside of Mohakhali) as input. Use default argument technique 
for taking place input.
                            Menu
    Price                                           (Tk)
    BBQ Chicken Cheese Burger                       250
    Beef Burger                                     170
    Naga Drums                                      200
    
Hint: Total Price = meal_cost + delivery_charge + tax Note that:
● If your home is in Mohakhali area then your delivery charge is 40 taka else 60 taka
● Your tax rate is 8% of your meal.
=======================================================================================================================
Sample Input                                            Sample Output
(‘Beef Burger’, ‘Dhanmondi’)                            243.6
(‘Beef Burger’)                                         223.6
'''
def foodpanda(name,place="Mohakhali"):
    menu = {'BBQ Chicken Cheese Burger' : 250, 'Beef Burger' : 170, 'Naga Drums' : 200}
    price = menu[name] + (menu[name])*0.08
    if place== "Mohakhali":
        delivery = 40
    else:
        delivery = 60
    print(price+delivery)

foodpanda('Beef Burger')