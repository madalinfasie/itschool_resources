import dataclasses
import typing as t
import json


class UserAlreadyExistsError(Exception):
    pass


@dataclasses.dataclass
class User:
    id: int
    name: str
    date_of_birth: str
    number_of_pets: t.Optional[int] = None


class UsersRepository:
    def __init__(self, file_handler):
        self.file = file_handler

    def get_users(self) -> t.List[t.Dict[str, t.Any]]:
        self.file.seek(0)
        content = self.file.read()
        if not content:
            return []

        return json.loads(content)

    def add_user(self, user: User) -> None:
        users = self.get_users()
        if self.check_user_exists(user, users):
            raise UserAlreadyExistsError(f'User with id {user.id} already exists')

        users.append(dataclasses.asdict(user))
        self.file.seek(0)
        self.file.truncate()

        json.dump(users, self.file)

    def check_user_exists(self, user: User, users: t.List[t.Dict[str, t.Any]]) -> bool:
        for db_user in users:
            if db_user['id'] == user.id:
                return True

        return False

    def get_user_by_id(self, id: int) -> t.Dict[str, t.Any]:
        filtered_users = [user for user in self.get_users() if user['id'] == id]
        return filtered_users[0] if filtered_users else None
