from abc import ABC, abstractmethod

from domain.model import Video


class VideoRepository(ABC):
    @abstractmethod
    def get_video(self, video_id: str) -> Video | None:
        raise NotImplementedError("Implement get_video method")

    @abstractmethod
    def get_all(self) -> list[Video]:
        raise NotImplementedError("Implement get_all method")
