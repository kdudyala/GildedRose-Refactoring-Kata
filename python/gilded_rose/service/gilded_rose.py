from gilded_rose.registry.updater import ItemUpdaterFactory

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = ItemUpdaterFactory.get_updater(item)
            updater.update(item)
