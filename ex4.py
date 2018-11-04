
cars=100
space_in_cars=4.0
drivers=30
passenger=90
cars_not_driven=cars-drivers
cars_driven=passenger
carpool_capacity=cars_driven*space_in_cars
average_passengers_per_car=passenger/cars_driven
#calculate the cars
print("There are",cars,"cars avaliable")
#drivers
print("There are ",drivers,"drivers avaliable")

print("There are",cars_not_driven,"empty cars today")

print("We can transport",carpool_capacity,"people today")

print("We have",passenger,"to carpool today")

print("We need to put about",average_passengers_per_car,"in each car")

