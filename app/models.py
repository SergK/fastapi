class User:
    """
    User model for the in-memory database.

    :param username: The username of the user.
    :param email: The email of the user.
    :param tasks: The number of tasks assigned to the user.
    """
    def __init__(self, username: str, email: str, tasks: int):
        self.username = username
        self.email = email
        self.tasks = tasks

    def to_dict(self):
        """
        Convert the User object to a dictionary.

        :return: The User object as a dictionary.
        """
        return {
            'username': self.username,
            'email': self.email,
            'tasks': self.tasks
        }