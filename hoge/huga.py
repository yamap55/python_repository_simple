"""sample"""

from logging import getLogger

logger = getLogger(__name__)


class Huga:
    """
    Huga class
    """

    def piyo(self) -> str:
        """return piyo"""
        logger.info("piyo")
        return "piyo"
