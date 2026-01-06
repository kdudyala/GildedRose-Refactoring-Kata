from abc import ABC, abstractmethod

class ItemUpdater(ABC):

    @abstractmethod
    def update(self, item):
        pass

    def increase_quality(self, item, amount=1, max_quality=50):
        item.quality = min(max_quality, item.quality + amount)

    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)
