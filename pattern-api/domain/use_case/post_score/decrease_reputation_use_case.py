from dataclasses import dataclass

from domain.model import PostScore
from domain.repository import PostScoreRepository


@dataclass
class DecreaseReputationUseCase:
    repository: PostScoreRepository

    def invoke(self, title: str) -> PostScore:
        return self.repository.decrease_reputation(title)
