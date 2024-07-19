from dataclasses import dataclass

from domain.model import PostScore
from domain.repository import PostScoreRepository


@dataclass
class AddReputationUseCase:
    repository: PostScoreRepository

    def invoke(self, post_score: PostScore) -> PostScore:
        return self.repository.add_reputation(post_score)
