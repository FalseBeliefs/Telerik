from models1.constants.vehicle_type import VehicleType

class Vehicle:
    def __init__(self, make, model, price: float, wheels):
        self.make = make
        self.model = model
        self.price = price
        self.wheels = wheels
        self.comments = []

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make_name):
        if len(make_name) < 2 or len(make_name) > 15:
            raise ValueError('Make must be between 2 and 15 characters long!')
        self._make = make_name

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model_name):
        if len(model_name) < 1 or len(model_name) > 15:
            raise ValueError('Model must be between 1 and 15 characters long!')
        self._model = model_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0 or value > 1000000:
            raise ValueError('Price must be between 0 and 1000000!')
        self._price = value

