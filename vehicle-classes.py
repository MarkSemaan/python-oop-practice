class Vehicle:
  def __init__(self, brand, model, year, rental_price_per_day):
    self.brand = brand
    self.model = model
    self.year = year
    self.__rental_price_per_day = rental_price_per_day

  def displayInfo(self):
    print(f"Brand: {self.brand}")
    print(f"Model: {self.model}")
    print(f"Year: {self.year}")
    print(f"Daily Rental Price: ${self.__rental_price_per_day}")
  def displayName(self):
    return f"{self.brand} {self.model}"


  def getRentalPrice(self):
    return self.__rental_price_per_day
  def setRentalPrice(self, rental_price_per_day):
    self.__rental_price_per_day = rental_price_per_day
  def showRentalPrice(self):
    return print(f"Daily rental price of {self.brand} {self.model}: ${self.__rental_price_per_day}")

  def calculate_rental_cost(self, days):
    return print(f"Rental cost for {self.brand} {self.model} for {days} day(s) is: " + f"${days*self.__rental_price_per_day}" )

class Car(Vehicle):
    def __init__(self, brand, model, year, seating_capacity, rental_price_per_day):
      super().__init__(brand, model, year, rental_price_per_day)
      self.seat = seating_capacity
    def displayInfo(self):
      super().displayInfo()
      print(f"Seats: {self.seat}")
class Bike(Vehicle):
  def __init__(self, brand, model, year, engine_capacity, rental_price_per_day):
    super().__init__(brand, model, year, rental_price_per_day)
    self.engine_capacity = engine_capacity
  def displayInfo(self):
    super().displayInfo()
    print(f"Engine Capacity: {self.engine_capacity}cc")

def show_vehicle_info(Vehicle):
  Vehicle.displayInfo()

car1 = Car("Toyota", "Corolla", 2020, 5, 15)
bike1 = Bike("Yamahama", "R1", 2019, 999, 20)

print("-----")
show_vehicle_info(car1)
print("-----")
show_vehicle_info(bike1)
print("-----")
car1.showRentalPrice()
car1.calculate_rental_cost(5)
car1.setRentalPrice(10)
print("-----")
print(f"Updating rental price for", car1.displayName() + "...")
print(f"Updated rental price for {car1.displayName()} is: ${car1.getRentalPrice()}")
car1.calculate_rental_cost(5)

