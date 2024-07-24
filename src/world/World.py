from os import path
from typing import TypeVar, Generic

from util import Identifier

ServerType = TypeVar('ServerType')


class World(Generic[ServerType]):
    """
    Stores data of a world (or dimension in Minecraft).

    Will save in dir /saves/hostServer.saveName/worlds/worldId.__str__ .

    ServerType should be inputted as a type of server.Server .
    """
    hostServer: ServerType
    worldId: Identifier

    def __init__(self, host_server: ServerType, world_id: Identifier):
        self.hostServer = host_server
        self.worldId = world_id

    def get_server(self) -> ServerType:
        return self.hostServer

    def get_dir(self) -> str:
        """ Returns path which stores data of this world.
        :return: The path.
        """
        return path.join(self.hostServer.get_dir(), "worlds", str(self.worldId))
