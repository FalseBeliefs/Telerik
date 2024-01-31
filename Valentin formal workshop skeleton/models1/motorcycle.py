from models1.vehicle import Vehicle
from models1.comment import Comment

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
            raise ValueError('Category must be between 3 and 10 characters long!')
        self._category = category_name


    def __str__(self):
        comments_start_end = ['--COMMENTS--']

        if len(self.comments) == 0:
            return f"{super().__str__()}\nCategory: {self.category}\n--NO COMMENTS--"

        for comment in self.comments:
            comments_start_end.append(str(comment))

        comments_start_end.extend(['--COMMENTS--'])
        all_together = "\n".join(comments_start_end)
        return f"{super().__str__()}\nCategory: {self.category}\n{all_together}"

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
