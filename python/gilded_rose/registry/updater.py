from gilded_rose.item.constants import AGED_BRIE, BACKSTAGE_PASSES, SULFURAS
from gilded_rose.updaters.aged_brie import AgedBrie
from gilded_rose.updaters.backstage_passes import BackstagePass
from gilded_rose.updaters.sulfuras import Sulfuras

class ItemUpdaterFactory:

    @staticmethod
    def get_updater(item):
        if item.name == AGED_BRIE:
            return AgedBrie()
        if item.name == BACKSTAGE_PASSES:
            return BackstagePass()
        if item.name == SULFURAS:
            return Sulfuras()
