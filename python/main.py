from gilded_rose.item.item import Item
from gilded_rose.service.gilded_rose import GildedRose
from gilded_rose.item.constants import AGED_BRIE, BACKSTAGE_PASSES, SULFURAS, SULFURAS_QUALITY

items = [
    Item(AGED_BRIE, 2, 0),
    Item(BACKSTAGE_PASSES, 15, 20),
    Item(SULFURAS, 0, 70),
]

app = GildedRose(items)

for day in range(10):
    print(f"\n--- Day {day} ---")
    for item in items:
        print(item)
        if item.name == SULFURAS:
            print(SULFURAS + " is a legendary item - never changes it quality and always has a quality of " + str(SULFURAS_QUALITY))
            continue
    app.update_quality()
