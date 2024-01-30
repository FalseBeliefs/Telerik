from models1.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, make, model, price: float, category, wheels=2):
        super().__init__(make, model, price, wheels)
        self.category = category


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category_name):
        if len(category_name) < 3 or len(category_name) > 10:
            raise ValueError('Category must be between 3 and 10 characters long')
        self._category = category_name


    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
