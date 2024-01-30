from models1.comment import Comment
from models1.constants.user_role import UserRole
from models1.vehicle import Vehicle


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
        self.vehicles: list[Vehicle] = []

        print(f"Username: {self.username}, FullName: {self.firstname} {self.lastname}, Role: {self.user_role}")

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
        if index > len(self.vehicles) - 1:
            raise ValueError("Vehicle index out of range!")
        return self.vehicles[index]

    def add_vehicle(self, vehicle: Vehicle):
        if self.is_admin:
            raise ValueError('You are an admin and therefore cannot add vehicles!')
        if len(self.vehicles) > 4 and self.user_role != UserRole.VIP:
            raise ValueError(f'You are not VIP and cannot add more than 5 vehicles')
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            return f"{self.username} removed vehicle successfully!"


    def print_vehicles(self):
        user = f"--USER {self.username}--"
        vehicle_info = []
        if len(self.vehicles) > 0:
            for vehicle in self.vehicles:
                vehicle_info.append(f"""Make: {vehicle.make}
                Model: {vehicle.model}
                Wheels: {vehicle.wheels}
                Price: ${vehicle.price}""")
        else:
            vehicle_info = "--NO VEHICLES--"
            return f"{user}\n{vehicle_info}"
        return f"{user}"+"\n"+f"{"\n".join(vehicle_info)}"

    def remove_comment(self, author):
        pass

    def add_comment(self, comment):
        pass

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
