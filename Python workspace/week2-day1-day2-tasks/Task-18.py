class Car:
    def __init__(self, make, model, year):
        self.make =make
        self.model = model
        self.year = year
    def get_car_info(self):
        print(f"This car is {self.make} {self.model} {self.year}")
    def update_model(self, model):
        self.model = model

#creating car objects
car_obj1 = Car('Suzuki', 'Alto', 2003)  
car_obj2 = Car('Mahindra', 'Bolero', 2005)

#getting car objects info
car_obj1.get_car_info()
car_obj2.get_car_info()

#updatinf car model:
car_obj2.update_model('Scorpio')
car_obj2.get_car_info()