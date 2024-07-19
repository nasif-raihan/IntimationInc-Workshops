from blog.models import User as DBUser, UserScore as DBUserScore
from domain.model import UserScore, User
from domain.repository import UserScoreRepository


class DBUserScoreRepository(UserScoreRepository):
    def add_reputation(self, user_score: UserScore) -> UserScore:
        try:
            db_user_score = DBUserScore.objects.get(
                user__username=user_score.user.username
            )
            db_user_score.reputation = user_score.reputation
            db_user_score.save()
            return self.to_user_score(db_user_score)
        except DBUserScore.DoesNotExist:
            db_user = DBUser.objects.get(username=user_score.user.username)
            db_user_score = DBUserScore(reputation=user_score.reputation, user=db_user)
            return self.to_user_score(db_user_score)
        except DBUser.DoesNotExist:
            raise RuntimeError("No such blog user is found!")

    def get_score(self, username: str) -> UserScore | None:
        try:
            db_user_score = DBUserScore.objects.get(user__username=username)
            return self.to_user_score(db_user_score)
        except DBUserScore.DoesNotExist:
            return None

    def increase_reputation(self, username: str) -> UserScore:
        try:
            db_user_score = DBUserScore.objects.get(user__username=username)
            db_user_score.reputation += 1
            db_user_score.save()
            return self.to_user_score(db_user_score)
        except DBUserScore.DoesNotExist:
            user_score = self.get_score(username)
            return self.add_reputation(user_score)

    def decrease_reputation(self, username: str) -> UserScore:
        try:
            db_user_score = DBUserScore.objects.get(user__username=username)
            db_user_score.reputation -= 1
            db_user_score.save()
            return self.to_user_score(db_user_score)
        except DBUserScore.DoesNotExist:
            db_user = DBUser.objects.get(username)
            db_user_score = DBUserScore(reputation=-1, user=db_user)
            db_user_score.save()
            return self.to_user_score(db_user_score)
        except DBUser.DoesNotExist:
            raise RuntimeError("No such blog user is found!")

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

    @classmethod
    def to_user_score(cls, db_user_score: DBUserScore) -> UserScore:
        user = cls.to_user(db_user_score.user)
        return UserScore(reputation=db_user_score.reputation, user=user)
