from dataclasses import dataclass

from domain.model import UserScore
from domain.repository import UserScoreRepository


@dataclass
class AddUserReputationUseCase:
    repository: UserScoreRepository

    def invoke(self, user_score: UserScore) -> UserScore:
        return self.repository.add_reputation(user_score)
