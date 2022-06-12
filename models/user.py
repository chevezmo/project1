class User:
    def __init__(self, user_id: int, username: str, first_name: str, last_name: str, manager: False):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.manager = manager

    def __repr__(self) -> str:
        return f'User_ID: {self.user_id}\nUsername: {self.username}\nName: {self.first_name} {self.last_name}\nManager: {self.manager}'

    def get_name(self):
        return f'{self.first_name} {self.last_name}'