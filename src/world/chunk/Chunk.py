from typing import TypeVar, Generic, List, Tuple
from math import floor

from block import Block

WorldType = TypeVar('WorldType')


class Chunk(Generic[WorldType]):
    """
    Stores data of a chunk, which is a 16(x)*INF(y) zone of the world.
    
    Will save in dir {worldDir}/chunks/{chunkPos}

    TypeVar WorldType should be inputted as a type of world.World
    """
    minGridHeight: int
    """The minimum height of the grid (min limit of building)."""
    maxGridHeight: int
    """The maximum height of the grid (max limit of building)."""
    grid: List[List[Block]]
    chunkPos: int
    """minX = 16*chunkPos"""

    def get_inits(self) -> Tuple[int, int]:
        """Returns minimum and maximum X position (block position) of the chunk, based in chunkPos.

        :return: A tuple of two integers (minX, maxX)
        """

        return (16*self.chunkPos, 16*self.chunkPos+15)
    
    @staticmethod
    def get_chunk_pos_of_block(block_pos_x: int) -> int:
        """Returns the chunkPos of a block position.

        :param block_pos_x: The X position of the block
        :return: The chunkPos of the block
        """
        
        return int(floor(block_pos_x/16))

