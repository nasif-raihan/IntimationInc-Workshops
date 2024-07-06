from blog.models import User as DBUser
from domain.model import User
from domain.repository import UserRepository


class DBUserRepository(UserRepository):
    def get_user_by_username(self, username: str) -> User | None:
        try:
            db_user = DBUser.objects.get(username=username)
        except DBUser.DoesNotExist:
            return None
        return self.to_user(db_user)

    def get_all_users(self) -> list[User]:
        db_users = DBUser.objects.all()
        if len(db_users):
            return [self.to_user(db_user) for db_user in db_users]
        return []

    def add_user(self, user: User) -> User:
        try:
            DBUser.objects.get(email=user.email)
        except DBUser.DoesNotExist:
            db_user = DBUser(
                email=user.email,
                username=user.username,
                is_active=user.is_active,
                is_staff=user.is_staff,
                is_admin=user.is_admin,
            )
            db_user.save()
            return self.to_user(db_user)

        return self.update_user(user)

    def update_user(self, user: User) -> User:
        try:
            db_user = DBUser.objects.get(email=user.email)
        except DBUser.DoesNotExist:
            raise RuntimeError("Email not found.")

        db_user.username = user.username
        db_user.is_active = user.is_active
        db_user.is_staff = user.is_staff
        db_user.is_admin = user.is_admin
        db_user.save()

        return self.to_user(db_user)

    def delete_user(self, username: str) -> bool:
        try:
            db_user = DBUser.objects.get(username=username)
            db_user.delete()
            return True
        except DBUser.DoesNotExist:
            return False

    @classmethod
    def to_user(cls, db_user: DBUser) -> User:
        return User(
            email=db_user.email,
            username=db_user.username,
            is_active=db_user.is_active,
            is_staff=db_user.is_staff,
            is_admin=db_user.is_admin,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at,
        )
