from .base import ItemUpdater
from gilded_rose.item.constants import MAX_QUALITY

class BackstagePass(ItemUpdater):
    def update(self, item):
        self.increase_quality(item, 1, MAX_QUALITY)
        
        if item.sell_in < 11:
            self.increase_quality(item, 1, MAX_QUALITY)
        
        if item.sell_in < 6:
            self.increase_quality(item, 1, MAX_QUALITY)
        
        item.sell_in -= 1
        
        if item.sell_in < 0:
            item.quality = 0
