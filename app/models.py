class User:
    def __init__(self, username: str, email: str, tasks: int):
        self.username = username
        self.email = email
        self.tasks = tasks

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'tasks': self.tasks
        }