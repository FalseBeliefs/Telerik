from models1.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, make, model, price: float, seats: int, wheels=4):
        super().__init__(make, model, price, wheels)
        self.seats = seats

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, seats_num: int):
        if seats_num < 1 or seats_num > 10:
            raise ValueError("Seats must be between 1 and 10!")
        self._seats = seats_num

    def __str__(self):
        comments_start_end = ['--COMMENTS--']

        if len(self.comments) == 0:
            return f"{super().__str__()}\nSeats: {self.seats}\n--NO COMMENTS--"

        for comment in self.comments:
            comments_start_end.append(str(comment))

        comments_start_end.extend(['--COMMENTS--'])
        all_together = "\n".join(comments_start_end)
        return f"{super().__str__()}\nSeats: {self.seats}\n{all_together}"

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
