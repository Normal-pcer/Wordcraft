from enum import Enum


class Node:
    """
    wordcraft.network.Node
    """
    
    class NodeType(Enum):
        """
        wordcraft.network.Node.NodeType
        """
        SERVER = 0x3D27C9
        CLIENT = 0xEF10C6