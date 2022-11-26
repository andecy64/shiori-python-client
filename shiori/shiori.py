from uplink import (
        Consumer,
        json,
        post,
        get,
        Field
        )

from .models import (
        ShioriBookmarks,
        ShioriLogin,
        )


class ShioriClient(Consumer):

    def __init__(self, base_url: str, username: str, password: str):

        super(ShioriClient, self).__init__(base_url=base_url)
        user_info = self.__login(username=username, password=password)
        self.session.headers["X-Session-Id"] = user_info.session

    @json
    @post("/api/login")
    def __login(self, username: Field, password: Field) -> ShioriLogin:
        """ Get session id """

    @json
    @get("/api/version")
    def get_version(self):
        """ Get version """

    @post("/api/logout")
    def logout(self):
        """ Logout """

    @get("/api/bookmarks")
    def get_bookmarks(self) -> ShioriBookmarks:
        """ Get bookmarks from server """

    @get("/api/accounts")
    def get_accounts(self):
        """ Get a list of user accounts """
