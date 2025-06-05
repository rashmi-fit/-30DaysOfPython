# Extend Car into an ElectricCar subclass with battery capacity

class car:
      def general_features(self):
            print('general features of car: 4 wheels, steering wheel, seats')
# below function i have used so that same can be used in child so that it can be overridden
      def specific_usage(self):
            self.general_features()
            print("Specific use of car: General transportation")
class electric_car(car):
      def __init__(self, battery_capacity):
            self.battery_capacity = battery_capacity
            print(f'I am an electric car with a battery capacity of {self.battery_capacity} kWh')
# here method over riding happening
      def specific_usage(self):
            self.general_features()
            print('specific use of electric car: driving with electric power')


def describe_car_usage(car_obj):
    car_obj.specific_usage()


car1 = car()
e = electric_car(75)

print("\nDescribing car1:")
describe_car_usage(car1)

print("\nDescribing electric1:")
describe_car_usage(e)
