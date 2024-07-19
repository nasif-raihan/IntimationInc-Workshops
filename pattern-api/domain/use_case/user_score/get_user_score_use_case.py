from dataclasses import dataclass

from domain.model import UserScore
from domain.repository import UserScoreRepository


@dataclass
class GetUserScoreUseCase:
    repository: UserScoreRepository

    def invoke(self, username: str) -> UserScore | None:
        return self.repository.get_score(username)
