from dataclasses import dataclass

from domain.model import Video
from domain.repository import VideoRepository


@dataclass
class GetVideoUseCase:
    repository: VideoRepository

    def invoke(self, video_id: str) -> Video:
        return self.repository.get_video(video_id)

    def get_all(self) -> list[Video]:
        return self.repository.get_all()
