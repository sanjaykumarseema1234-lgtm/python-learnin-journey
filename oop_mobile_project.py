class Mobile:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def display(self):
        print(f" {self.brand} is the best working device.")
        print(f"This {self.brand} is now available at ₹{self.cost}")

    def call(self):
        print(f"Finally! {self.brand} is best in making calls with excellent audio performance.")
        
m1 = Mobile("samsung" ,90000)
m1.display()
m1.call()
