import os
from typing import List, Any

from nonebot import get_driver, logger
from nonebot.config import BaseConfig
from pydantic import AnyHttpUrl, Extra


class ELFConfig(BaseConfig):
    class Config:
        extra = Extra.allow

    rss_proxy: str = ""
    rsshub: AnyHttpUrl = "https://rsshub.app"
    rsshub_backup: List[AnyHttpUrl] = []
    db_cache_expire = 30
    limit = 50

    zip_size: int = 2 * 1024

    gif_zip_size: int = 6 * 1024

    blockquote: bool = True
    black_word: List[str] = []

    baidu_id: str = ""
    baidu_key: str = ""

    is_linux: bool = os.name != "nt"

    close_pixiv_cat: bool = False

    is_open_auto_down_torrent: bool = False
    qb_web_url: str = "http://127.0.0.1:8081"
    qb_down_path: str = ""  # qb的文件下载地址，这个地址必须是 go-cqhttp能访问到的
    down_status_msg_group: List[int] = []
    down_status_msg_date: int = 10

    max_length: int = 0  # 正文长度限制，防止消息太长刷屏

    version: str = ""

    def __getattr__(self, name: str) -> Any:
        data = self.dict()
        for k, v in data.items():
            if k.casefold() == name.casefold():
                return v
        return None


config = ELFConfig(**get_driver().config.dict())
logger.debug(f"RSS Config loaded: {config!r}")
