from dataclasses import dataclass

from domain.model import PostScore
from domain.repository import PostScoreRepository


@dataclass
class IncreasePostReputationUseCase:
    repository: PostScoreRepository

    def invoke(self, title: str, author_username: str) -> PostScore:
        return self.repository.increase_reputation(title, author_username)
