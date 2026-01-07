from .base import ItemUpdater

class NormalItem(ItemUpdater):
    def update(self, item):
        self.decrease_quality(item, 1)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item, 1)
