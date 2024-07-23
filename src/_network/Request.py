from enum import Enum
from uuid import UUID, uuid4


class Request:
    """
    wordcraft.network.Request
    """
    
    class RequestType(Enum):
        """
        wordcraft.network.Request.RequestType
        """

        GET = 0x752803
        SET = 0x8C5268
    
    requestType: RequestType
    requestId: UUID
    datapack: dict
    """Temporary solution, should be a class"""
    
    def __init__(self, requestType: RequestType, datapack: dict):
        self.requestType = requestType
        self.requestId = uuid4()
        self.datapack = datapack
    
    