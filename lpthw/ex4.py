#setting cars to an int
cars = 100
#setting space_in_a_car to a float
space_in_a_car = 4.0
#setting drivers to an int
drivers = 30
#setting passengers to an int
passengers = 90
#setting cars_not_driven to an int
cars_not_driven = cars - drivers
#setting cars_driven to drivers
cars_driven = drivers
#setting carpool_capacity to a float
carpool_capacity = cars_driven * space_in_a_car
#setting average_passengers_per_car to float
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars availavle.")
print("Ther are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
