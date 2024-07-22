from enum import Enum


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
    