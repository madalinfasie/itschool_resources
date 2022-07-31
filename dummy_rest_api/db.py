import dataclasses
import typing as t
import json

import redis


class UserAlreadyExistsError(Exception):
    pass


@dataclasses.dataclass
class User:
    id: int
    name: str
    date_of_birth: str
    number_of_pets: t.Optional[int] = None


class UsersRepository:
    def __init__(self, redis_db: redis.Redis):
        self.client = redis_db

    def get_users(self) -> t.Dict[str, t.Any]:
        return [json.loads(user) for user in self.client.lrange('users', start=0, end=-1)]

    def add_user(self, user: User) -> None:
        if self.check_user_exists(user):
            raise UserAlreadyExistsError(f'User with id {user.id} already exists')

        self.client.rpush('users', json.dumps(dataclasses.asdict(user)))

    def check_user_exists(self, user: User) -> bool:
        for db_user in self.get_users():
            if db_user['id'] == user.id:
                return True

        return False

    def get_user_by_id(self, id: int) -> t.Dict[str, t.Any]:
        filtered_users = [user for user in self.get_users() if user['id'] == id]
        return filtered_users[0] if filtered_users else None
