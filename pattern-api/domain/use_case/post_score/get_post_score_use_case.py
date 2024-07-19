from dataclasses import dataclass

from domain.model import PostScore
from domain.repository import PostScoreRepository


@dataclass
class GetPostScoreUseCase:
    repository: PostScoreRepository

    def invoke(self, title: str) -> PostScore | None:
        return self.repository.get_score(title)
