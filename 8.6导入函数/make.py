def make_car(factory,type,**car_info):
    profile = {}
    profile['factory'] = factory
    profile['type'] = type
    for key,value in car_info.items():
        profile[key] = value
    print(profile)

def make_pizza(size ,*toppings):
    print("You have ordered a " + str(size) + "-inch pizza!")
    for topping in toppings:
        print("You have ordered adding " + topping + '!')