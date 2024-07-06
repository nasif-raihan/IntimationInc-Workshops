from domain.use_case.blog import (
    AddBlogUseCase,
    DeleteBlogUseCase,
    GetBlogUseCase,
    UpdateBlogUseCase,
)
from domain.use_case.user import (
    AddUserUseCase,
    DeleteUserUseCase,
    GetUserUseCase,
    UpdateUserUseCase,
)
from .repository import Repository


class UseCase:
    def __init__(self):
        self._repository = Repository.get_instance()

    @property
    def add_blog(self) -> AddBlogUseCase:
        return AddBlogUseCase(blog_repository=self._repository.blog_repository)

    @property
    def get_blog(self) -> GetBlogUseCase:
        return GetBlogUseCase(blog_repository=self._repository.blog_repository)

    @property
    def update_blog(self) -> UpdateBlogUseCase:
        return UpdateBlogUseCase(blog_repository=self._repository.blog_repository)

    @property
    def delete_blog(self) -> DeleteBlogUseCase:
        return DeleteBlogUseCase(blog_repository=self._repository.blog_repository)

    @property
    def add_user(self) -> AddUserUseCase:
        return AddUserUseCase(user_repository=self._repository.user_repository)

    @property
    def get_user(self) -> GetUserUseCase:
        return GetUserUseCase(user_repository=self._repository.user_repository)

    @property
    def update_user(self) -> UpdateUserUseCase:
        return UpdateUserUseCase(user_repository=self._repository.user_repository)

    @property
    def delete_user(self) -> DeleteUserUseCase:
        return DeleteUserUseCase(user_repository=self._repository.user_repository)
