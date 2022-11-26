from typing import List
from pydantic import BaseModel


class ShioriBookmarkTags(BaseModel):
    id: int
    name: str


class ShioriBookmark(BaseModel):
    id: int
    url: str
    title: str
    excerpt: str
    author: str
    public: int
    modified: str
    imageURL: str
    hasContent: bool
    hasArchive: bool
    tags: List[ShioriBookmarkTags]
    createArchive: bool


class ShioriBookmarks(BaseModel):
    bookmarks: List[ShioriBookmark]
    maxPage: int
    page: int


class ShioriLoginAccount(BaseModel):
    id: int
    username: str
    owner: bool


class ShioriLogin(BaseModel):
    session: str
    account: ShioriLoginAccount


class ShioriConfig(BaseModel):
    username: str
    password: str
    base_url: str


class Account(BaseModel):
    id: int
    username: str
    owner: bool
