from di import Repository
from di.use_case import UserUseCase
from domain.use_case.post_score import (
    GetPostScoreUseCase,
    AddPostReputationUseCase,
    IncreasePostReputationUseCase,
    DecreasePostReputationUseCase,
)
from domain.use_case.user_score import (
    AddUserReputationUseCase,
    GetUserScoreUseCase,
    IncreaseUserReputationUseCase,
    DecreaseUserReputationUseCase,
)


class ScoreFactoryUseCase:
    def __init__(self, ):
        self.__repository = Repository.get_instance()
        self.__user_use_case = UserUseCase()

    def get_reputation(self, title: str, author_username: str) -> dict:
        post_reputation = self.get_post_reputation.invoke(title, author_username)
        user_reputation = self.get_user_reputation.invoke(author_username)

        reputation = {}
        if post_reputation:
            reputation["postReputation"] = {
                "postTitle": post_reputation.post.title,
                "reputation": post_reputation.reputation
            }

        if user_reputation:
            reputation["userReputation"] = {
                "username": user_reputation.user.username,
                "reputation": user_reputation.reputation
            }

        return reputation

    def update_reputation(
            self,
            title: str,
            author_username: str,
            reviewer_username: str,
            increase_reputation: bool
    ) -> dict:
        reviewer = self.__user_use_case.get_user.invoke(reviewer_username)
        if reviewer.is_admin:
            reputation = self.__update_user_reputation(increase_reputation, author_username)
        else:
            reputation = self.__update_post_reputation(increase_reputation, title, author_username)

        return reputation

    @property
    def add_post_reputation(self) -> AddPostReputationUseCase:
        return AddPostReputationUseCase(self.__repository.post_score_repository)

    @property
    def get_post_reputation(self) -> GetPostScoreUseCase:
        return GetPostScoreUseCase(self.__repository.post_score_repository)

    @property
    def increase_post_reputation(self) -> IncreasePostReputationUseCase:
        return IncreasePostReputationUseCase(self.__repository.post_score_repository)

    @property
    def decrease_post_reputation(self) -> DecreasePostReputationUseCase:
        return DecreasePostReputationUseCase(self.__repository.post_score_repository)

    @property
    def add_user_reputation(self) -> AddUserReputationUseCase:
        return AddUserReputationUseCase(self.__repository.user_score_repository)

    @property
    def get_user_reputation(self) -> GetUserScoreUseCase:
        return GetUserScoreUseCase(self.__repository.user_score_repository)

    @property
    def increase_user_reputation(self) -> IncreaseUserReputationUseCase:
        return IncreaseUserReputationUseCase(self.__repository.user_score_repository)

    @property
    def decrease_user_reputation(self) -> DecreaseUserReputationUseCase:
        return DecreaseUserReputationUseCase(self.__repository.user_score_repository)

    def __update_user_reputation(self, increase_reputation: bool, author_username: str) -> dict:
        if increase_reputation:
            user_reputation = self.increase_user_reputation.invoke(author_username)
        else:
            user_reputation = self.decrease_user_reputation.invoke(author_username)

        return {
            "userReputation": {
                "username": user_reputation.user.username,
                "reputation": user_reputation.reputation
            }
        }

    def __update_post_reputation(self, increase_reputation: bool, title: str, author_username: str) -> dict:
        if increase_reputation:
            post_reputation = self.increase_post_reputation.invoke(title, author_username)
        else:
            post_reputation = self.decrease_post_reputation.invoke(title, author_username)

        return {
            "postReputation": {
                "postTitle": post_reputation.post.title,
                "reputation": post_reputation.reputation
            },
        }
