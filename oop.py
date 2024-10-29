class Fruits:
    # constructor method
    def __init__(self, name, price, color):
        self.name=name
        self.price=price
        self.color=color
        # method
    def display(self):
        print(f"I love eating {self.name}, it costs{self.price} and it is {self.color} in color")

# instance
myobj=Fruits("Banana",20,"Yellow")
myobj.display()
myobj2=Fruits("Mango",40,"Green")
myobj2.display()
