from domain.use_case.blog_post import (
    AddBlogPostUseCase,
    DeleteBlogPostUseCase,
    GetBlogPostUseCase,
    UpdateBlogPostUseCase,
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
    def add_blog_post(self) -> AddBlogPostUseCase:
        return AddBlogPostUseCase(
            blog_post_repository=self._repository.blog_post_repository
        )

    @property
    def get_blog_post(self) -> GetBlogPostUseCase:
        return GetBlogPostUseCase(
            blog_post_repository=self._repository.blog_post_repository
        )

    @property
    def update_blog_post(self) -> UpdateBlogPostUseCase:
        return UpdateBlogPostUseCase(
            blog_post_repository=self._repository.blog_post_repository
        )

    @property
    def delete_blog_post(self) -> DeleteBlogPostUseCase:
        return DeleteBlogPostUseCase(
            blog_post_repository=self._repository.blog_post_repository
        )

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
