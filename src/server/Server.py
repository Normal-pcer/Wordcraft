from typing import List

from util import Identifier
from world import World


class Server:
    """
    Stores data of a server, or a save.

    Will save to dir: /saves/{saveName}
    """
    runningWorlds: List[World]
    serverName: str
    """Name of the server. Can be the same as other local serverName."""
    saveName: str
    """Name of the save. CANNOT be the same as other local saveName."""

    def get_dir(self) -> str:
        """Returns path of save directory.

        :return: The path.
        """
        return f"saves/{self.saveName}"
