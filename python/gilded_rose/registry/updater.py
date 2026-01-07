from gilded_rose.item.constants import AGED_BRIE, BACKSTAGE_PASSES, SULFURAS, CONJURED
from gilded_rose.updaters.aged_brie import AgedBrie
from gilded_rose.updaters.backstage_passes import BackstagePass
from gilded_rose.updaters.sulfuras import Sulfuras
from gilded_rose.updaters.conjured import ConjuredItem
from gilded_rose.updaters.normal import NormalItem

class ItemUpdaterFactory:

    @staticmethod
    def get_updater(item):
        if item.name == AGED_BRIE:
            return AgedBrie()
        if item.name == BACKSTAGE_PASSES:
            return BackstagePass()
        if item.name == SULFURAS:
            return Sulfuras()
        if item.name == CONJURED:
            return ConjuredItem()
        return NormalItem()