from models1.comment import Comment

class Vehicle:
    def __init__(self, make, model, price: float, wheels):
        self.make = make
        self.model = model
        self.price = price
        self.wheels = wheels
        self._comments: list[Comment] = []

    @property
    def comments(self):
        return tuple(self._comments)

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
            raise ValueError('Price must be between 0.0 and 1000000.00!')
        self._price = value

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    def get_comment(self, idx: int):
        if len(self._comments) == 0:
            raise ValueError("There is no comment on this index.")
        elif idx > len(self._comments) - 1:
            raise ValueError("The vehicle does not exist!")
        return self.comments[idx]

    def remove_comment(self, comment: Comment):
        if comment in self._comments:
            self._comments.remove(comment)
        else:
            pass


    def __str__(self):
        return '\n'.join([f'{self.__class__.__name__}:', f'Make: {self._make}', f'Model: {self._model}',
                          f'Wheels: {self.wheels}', f'Price: ${self._price:.2f}'])

