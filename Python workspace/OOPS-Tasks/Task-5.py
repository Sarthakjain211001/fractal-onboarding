#Product class constaining name and price
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#shopping cart class
class ShoppingCart:
    products = []  #list of products
    count_array = [] #an array to maintain the count of the product
                     #at respective index
    total_price = 0.0  #total price of the cart

    def find_product(self, name):
        for i in range(0,len(self.products)):
            if(self.products[i].name == name):
                return i
        return -1

    def add_product(self, product):  #as a product will be added we need to
        index= self.find_product(product.name)
        if(index == -1):
            self.products.append(product) #append it to the products list
            self.count_array.append(1)
            self.total_price += product.price #and add its price to total price
        else:
            self.count_array[index] += 1
            self.total_price += product.price

    def remove_product(self, product_name): #removing a product by product_name
         index = self.find_product(product_name)
         if (index != -1):
            self.total_price = self.total_price-self.products[index].price
            if(self.count_array[index] > 1):
                self.count_array[index] -= 1
            else:
                self.products.pop(index)
                self.count_array.pop(index)
        
    def displayCart(self):   #display the items in the cart
        print('Product name, Count, Price')
        for i in range(0, len(self.products)):
            print (f'{self.products[i].name} , {self.count_array[i]}, {self.products[i].price * self.count_array[i]}')

    def get_totalPrice(self): #get total price of the cart
        return self.total_price

#crating some product objects
productP1 = Product("t-shirt", 472.40)
productP2 = Product("shoes", 723.13)
productP3 = Product("Jeans", 1024.17)
productP4 = Product("Trousers", 967.47)
productP5 = Product("Shirt", 828.73)
productP6 = Product("Shampoo", 235.69)
productP7 = Product("FaceWash", 321.38)

cartC1 = ShoppingCart() # a cart object
cartC1.add_product(productP3)
cartC1.add_product(productP2)
cartC1.add_product(productP4)
cartC1.add_product(productP7)
cartC1.add_product(productP4)
cartC1.add_product(productP4)
cartC1.add_product(productP2)
cartC1.add_product(productP2)
cartC1.add_product(productP2)
cartC1.add_product(productP7)
cartC1.displayCart()
print("Total: ", cartC1.get_totalPrice())

cartC1.remove_product('Trousers')
cartC1.remove_product('Trousers')
cartC1.remove_product('Trousers')


cartC1.displayCart()
print("Total: ", cartC1.get_totalPrice())

