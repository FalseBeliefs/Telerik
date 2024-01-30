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



    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, username):
        if len(username) < 2 or len(username) > 20:
            print('Username must be between 2 and 20 characters long!\n',"####################")
        elif not username.isalnum():
            print('Username contains invalid symbols!\n',"####################")
        self.username = username

    @property
    def firstname(self):
        return self.firstname

    @firstname.setter
    def firstname(self, first_name):
        if len(first_name) > 2 or len(first_name) > 20:
            print('Firstname must be between 2 and 20 characters long!\n',"####################")
        self.firstname = first_name

    @property
    def lastname(self):
        return self.lastname

    @lastname.setter
    def lastname(self, last_name):
        if len(last_name) > 2 or len(last_name) > 20:
            print('Lastname must be between 2 and 20 characters long!\n',"####################")
        self.lastname = last_name

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        if len(password) < 5 or len(password) > 30:
            print('Password must be between 5 and 30 characters long!\n',"####################")
        #if not password.isalnum():
        #    if ["@", "*", "-", "_"] not in password:
        #print('Password contains invalid symbols!')

    def get_vehicle_by_index(self, index: int) -> Vehicle:
        return self.vehicles[index]

    def add_vehicle(self, vehicle: Vehicle):
        if self.is_admin:
            print('You are an admin and therefore cannot add vehicles!\n',"####################")
            return
        if len(self.vehicles) > 4 and self.user_role != UserRole.VIP:
            print(f'You are not VIP and cannot add more than 5 vehicles\n',"####################")
            return
        self.vehicles.append(vehicle)


    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file
