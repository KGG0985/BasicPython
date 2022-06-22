class Xi:
    def __init__(self):
        super().__init__()
        self.money = 1000
    def steal(self,smoney):
        self.money += smoney

class Putin:
    def __init__(self):
        super().__init__()
        self.nuclear = 5000
    def sick(self):
        self.nuclear -= 1

class Kim:
    def __init__(self):
        
        self.food = 10000
    def shoot(self):
        self.food -= 100
        
class Sungwoo(Xi,Putin,Kim):
    
    def __init__(self):
        super().__init__()
        # Xi.__init__(self)
        # Putin.__init__(self)
        # Kim.__init__(self)
        
    def Poo(self):
        a.steal(10)

        a.sick()
        a.shoot()
       
a = Sungwoo()
print(a.money)
print(a.nuclear)
print(a.food)

a.Poo()
print(a.money)
print(a.nuclear)
print(a.food)
    
        