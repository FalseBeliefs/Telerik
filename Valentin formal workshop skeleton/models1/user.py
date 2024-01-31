from models1.constants.user_role import UserRole
from models1.vehicle import Vehicle
from models1.comment import Comment


class User:
    def __init__(self, username, firstname, lastname, password, user_role: UserRole):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.user_role = user_role

        if self.user_role == UserRole.ADMIN:
            self.is_admin = True
        else:
            self.is_admin = False

        self.vehicle_limit = 5
        self._vehicles: list[Vehicle] = []

    @property
    def vehicles(self):
        return tuple(self._vehicles)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if len(username) < 2 or len(username) > 20:
            raise ValueError('Username must be between 2 and 20 characters long!')
        elif not username.isalnum():
            raise ValueError('Username contains invalid symbols!')
        else:
            self._username = username

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, first_name):
        if len(first_name) < 2 or len(first_name) > 20:
            raise ValueError('Firstname must be between 2 and 20 characters long!')
        self._firstname = first_name

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, last_name):
        if len(last_name) < 2 or len(last_name) > 20:
            raise ValueError('Lastname must be between 2 and 20 characters long!')

        self._lastname = last_name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if len(password) < 5 or len(password) > 30:
            raise ValueError('Password must be between 5 and 30 characters long!')
        if all(char.isalnum() or char in ["@", "*", "-", "_"] for char in password):
            self._password = password
        else:
            raise ValueError("Password contains invalid symbols!")

    def get_vehicle(self, index: int) -> Vehicle:
        if index > len(self._vehicles) - 1:
            raise ValueError("The vehicle does not exist!")
        return self._vehicles[index]

    def add_vehicle(self, vehicle: Vehicle):
        if self.is_admin:
            raise ValueError('You are an admin and therefore cannot add vehicles!')
        if len(self._vehicles) > 4 and self.user_role != UserRole.VIP:
            raise ValueError(f'You are not VIP and cannot add more than 5 vehicles!')
        self._vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)
            return f"{self.username} removed vehicle successfully!"

    def print_vehicles(self):
        if len(self._vehicles) == 0:
            return f"--USER {self.username}--\n--NO VEHICLES--"
        else:
            result = f"--USER {self.username}--\n"
            vehicles = []
            num = 1
            for vehicle in self._vehicles:
                vehicles.append(f"{num}. {vehicle}")
                num += 1
            all_vehicles = "\n".join(vehicles)
            return f"{result}{all_vehicles}"

    def remove_comment(self, comment: Comment, vehicle: Vehicle):
        if comment.author != self.username:
            raise ValueError("You are not the author of the comment you are trying to remove!")
        if comment not in vehicle.comments:
            raise ValueError("That comment does not exist!")
        vehicle.remove_comment(comment)

    def add_comment(self, comment: Comment, vehicle: Vehicle):
        vehicle.add_comment(comment)


    def __str__(self):
        return f"Username: {self.username}, FullName: {self.firstname} {self.lastname}, Role: {self.user_role}"

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
