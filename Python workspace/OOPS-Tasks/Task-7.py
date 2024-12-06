#Product class (Parent class)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_info(self):
        print(f'name: {self.name}, price:{self.price}')
#Electronics class (child1) 
class Electronics(Product):
    def __init__(self,name,price,warranty_period): #additional attribute warranty
        self.warranty_period = warranty_period
        Product.__init__(self, name, price) #calling parent constructor
    def get_info(self):  #method overriding
        print(f'name: {self.name}, price:{self.price}, warranty:{self.warranty_period}')
#clothing class(child2)
class Clothing(Product):
    def __init__(self, name, price,size):#additional attribute size
        self.size = size
        Product.__init__(self,name,price)
    def get_info(self):#method overriding
        print(f'name: {self.name}, price:{self.price}, size:{self.size}')
        
#class shopping cart
class ShoppingCart:
    products=[]  #list of products.
    total_price = 0.0
    def add_product(self,product):
        self.products.append(product) #appending product object to list
        self.total_price+=product.price

#creating some products(electronics, clothing)
ProductP1 = Product("p1",270.35)
ProductP2 = Product("p2",6431.47)
ProductP3 = Product("p3",3725.81)
electronicE1 = Electronics("E1", 42535.24, 2)
electronicE2 = Electronics("E2", 52431.65, 3)
clothC1 = Clothing("C1", 2365.42, "M")
clothC2 = Clothing("C2", 1232.50, "XL")

CartC1 = ShoppingCart()
#Adding items to cart
CartC1.add_product(ProductP1)
CartC1.add_product(ProductP2)
CartC1.add_product(electronicE1)
CartC1.add_product(electronicE2)
CartC1.add_product(clothC1)
CartC1.add_product(clothC2)

#printing total amount
print(CartC1.total_price)

#printing product details:
ProductP1.get_info()
electronicE1.get_info()
clothC1.get_info()
