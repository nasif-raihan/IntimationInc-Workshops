from blog.models import Video as DBVideo
from domain.model import Video
from domain.repository import VideoRepository
from ..mapper import Mapper


class DBVideoRepository(VideoRepository):
    def __init__(self):
        self.__mapper = Mapper.get_instance()

    def get_video(self, video_id: str) -> Video | None:
        try:
            db_video = DBVideo.objects.get(video_id=video_id)
            return self.__mapper.to_video(db_video)
        except DBVideo.DoesNotExist:
            return None

    def get_all(self) -> list[Video]:
        try:
            db_videos = DBVideo.objects.all()
            return [self.__mapper.to_video(db_video) for db_video in db_videos]
        except DBVideo.DoesNotExist:
            return []
