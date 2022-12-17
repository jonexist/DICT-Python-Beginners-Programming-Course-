class Customers:
  greeting = "Welcome to the Coffee Palace!"
  pass

c_1 = Customers()

c_1.name = "Samirah"
c_1.beverage = "Iced coffee latte"
c_1.food = "Cinnamon roll"
c_1.total = 225

c_2 = Customers()

c_2.name = "Jerry"
c_2.beverage = "Caramel macchiato"
c_2.food = "Glazed doughnut"
c_2.total = 230

print(Customers.greeting)
print(c_1.beverage)
print(c_2.food)