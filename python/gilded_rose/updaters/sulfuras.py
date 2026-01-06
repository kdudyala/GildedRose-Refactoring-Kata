from .base import ItemUpdater
from gilded_rose.item.constants import SULFURAS_QUALITY

class Sulfuras(ItemUpdater):
    def update(self, item):
        item.quality = SULFURAS_QUALITY