# Find the lost car key in home and when found stop searching

home = ["kitchen", "garaage", "garden", "balcony", "livingroom", "bedroom", "bathroom", "car key"]
lost_car_key = "car key"

for i in home:
    if i == lost_car_key:
        print("found the lost car key")
        break
else:
    print("lost car key not found in home")
