from dataclasses import dataclass

from domain.model import UserScore
from domain.repository import UserScoreRepository


@dataclass
class DecreaseUserReputationUseCase:
    repository: UserScoreRepository

    def invoke(self, username: str) -> UserScore:
        return self.repository.decrease_reputation(username)
