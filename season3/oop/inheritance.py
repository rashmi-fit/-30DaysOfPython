class vehicle:
      def general_usage(self):
            print('general use of vehicle: transporatation')

class Car(vehicle):
      def __init__(self):
            print('I am a car')
            self.wheels =4
            self.has_roof = True
      def specific_usage(self):
            self.general_usage
            print('specific use of car: driving on roads')

class motorcycle(vehicle):
      def __init__(self):
            print('I am motorcycle')
            self.wheels = 4
            self.has_roof = True

      def specific_usage(self):
            self.general_usage
            print("specific use of motorcycle: driving on roads")

c = Car()
# c.general_usage()
c.specific_usage()

m = motorcycle()
# m.general_usage()
m.specific_usage()
