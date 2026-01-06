from gilded_rose.item.item import Item
from gilded_rose.service.gilded_rose import GildedRose
from gilded_rose.item.constants import AGED_BRIE, BACKSTAGE_PASSES

items = [
    Item(AGED_BRIE, 2, 0),
    Item(BACKSTAGE_PASSES, 15, 20),
]

app = GildedRose(items)

for day in range(10):
    print(f"\n--- Day {day} ---")
    for item in items:
        print(item)
    app.update_quality()
