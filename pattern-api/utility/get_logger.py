import logging
from pathlib import Path
from typing import Self

from environs import Env

env = Env()
env.read_env()


class GetLogger:
    __instance = None

    def __init__(self, name: str = "custom"):
        if self.__instance:
            raise RuntimeError("An instance of CustomLogger is already running!")

        self.log_directory = Path("logs")
        self.log_directory.mkdir(exist_ok=True)
        self.log_filepath = self.log_directory / f"{name}.log"
        self.log_level = logging.DEBUG if env.bool("DEBUG") else logging.INFO
        self.formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(module)s.%(filename)s.%(funcName)s[%(lineno)d] %(message)s"
        )
        self.logger = logging.Logger(name)

    @classmethod
    def get_instance(cls) -> Self:
        if cls.__instance is None:
            cls.__instance = GetLogger()
        return cls.__instance

    def __call__(self, *args, **kwargs) -> logging.Logger:
        self.file_handler()
        self.console_handler()
        return self.logger

    def file_handler(self):
        file_handler = logging.FileHandler(filename=self.log_filepath, mode="a")
        file_handler.setFormatter(self.formatter)
        file_handler.setLevel(self.log_level)
        self.logger.addHandler(file_handler)

    def console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)
        console_handler.setLevel(self.log_level)
        self.logger.addHandler(console_handler)
