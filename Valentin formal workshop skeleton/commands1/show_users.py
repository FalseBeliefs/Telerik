from commands1.base_command import BaseCommand
from core.application_data import ApplicationData
from models1.user import User

class ShowUsersCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        logged_user = self._app_data.logged_in_user
        id = 1
        start = ['--USERS--']
        if logged_user.is_admin != True:
            raise ValueError("You are not an admin!")
        else:
            for user in self._app_data.users:
                    start.append(f'{id}. {user}')
                    id += 1
            return "\n".join(start)

