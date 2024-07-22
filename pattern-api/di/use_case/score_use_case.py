from di import Repository
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


class ScoreUseCase:
    def __init__(self):
        self.__repository = Repository.get_instance()

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
