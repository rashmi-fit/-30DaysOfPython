# - Create a Car class with attributes and a display method
class car:
      def __init__(self,c ,s):
            self.color = c
            self.speed = s
      def display(self):
            if self.color == 'red':
                  print("The car is red", self.speed)
            elif self.color == 'blue':
                  print("The car is blue", self.speed)

      def accelerate(self):
            if self.speed < 56:
                  print("The car is accelerating")
            else:
                  print("The car is at maximum speed")

maruti = car("red", 50)
maruti.display()
maruti.accelerate()
