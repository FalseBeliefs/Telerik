from models1.vehicle import Vehicle
from models1.comment import Comment
from models1.user import User

class Truck(Vehicle):
    def __init__(self, make, model, price: float, weight_capacity, wheels=8):
        super().__init__(make, model, price, wheels)
        self.weight_capacity = weight_capacity


    @property
    def weight_capacity(self):
        return self._weight_capacity

    @weight_capacity.setter
    def weight_capacity(self, weight_cap):
        if weight_cap < 1 or weight_cap > 100:
            raise ValueError('Weight capacity must be between 1 and 100!')
        self._weight_capacity = weight_cap

    def __str__(self):
        comments_start_end = ['--COMMENTS--']
        if len(self.comments) == 0:
            return f"{super().__str__()}\nWeight Capacity: {self.weight_capacity}t\n--NO COMMENTS--"

        for comment in self.comments:
            comments_start_end.append(str(comment)) # WHY
        comments_start_end.extend(['--COMMENTS--'])
        all_together = "\n".join(comments_start_end)
        return f"{super().__str__()}\nWeight Capacity: {self.weight_capacity}t\n{all_together}"



    WHEELS_COUNT = 8

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
