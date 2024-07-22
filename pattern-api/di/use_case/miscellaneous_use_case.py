from domain.use_case.video import GetVideoUseCase
from ..repository import Repository


class MiscellaneousUseCase:
    def __init__(self):
        self.__repository = Repository.get_instance()

    @property
    def get_video(self) -> GetVideoUseCase:
        return GetVideoUseCase(repository=self.__repository.video_repository)
