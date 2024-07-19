from dataclasses import dataclass

from domain.model import UserScore
from domain.repository import UserScoreRepository


@dataclass
class IncreaseUserReputationUseCase:
    repository: UserScoreRepository

    def invoke(self, username: str) -> UserScore:
        return self.repository.increase_reputation(username)
