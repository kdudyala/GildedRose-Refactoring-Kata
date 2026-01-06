from gilded_rose.item.constants import AGED_BRIE
from gilded_rose.updaters.aged_brie import AgedBrie

class ItemUpdaterFactory:

    @staticmethod
    def get_updater(item):
        if item.name == AGED_BRIE:
            return AgedBrie()
