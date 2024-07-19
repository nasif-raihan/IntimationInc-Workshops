from dataclasses import dataclass

from domain.model import PostScore
from domain.repository import PostScoreRepository


@dataclass
class IncreasePostReputationUseCase:
    repository: PostScoreRepository

    def invoke(self, title: str) -> PostScore:
        return self.repository.increase_reputation(title)
