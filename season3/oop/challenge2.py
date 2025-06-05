# Extend Car into an ElectricCar subclass with battery capacity
# class vehicle:
#       def general_usage(self):
#             print('general use of vehicle: transporatation')

class car:
      def general_features(self):
            print('general features of car: 4 wheels, steering wheel, seats')

class electric_car(car):
      def __init__(self, battery_capacity):
            self.battery_capacity = battery_capacity
            print(f'I am an electric car with a battery capacity of {self.battery_capacity} kWh')

      def specific_usage(self):
            self.general_features()
            print('specific use of electric car: driving with electric power')

# my_electric_car = electric_car(75)

e = electric_car(75)
e.specific_usage
