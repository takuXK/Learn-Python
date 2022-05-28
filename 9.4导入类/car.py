class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        total = self.make + ' ' + self.model + ' ' + str(self.year)
        return total.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
    def increment_odometre(self,miles):
        if miles > 0:
            self.odometer_reading += miles

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print('Remain ' + str(self.battery_size) +"-KWh.")
    def get_range(self,battery_size):
        range = 3*battery_size
        print("This car can go approximately " + str(range) + " miles on full charge.")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()