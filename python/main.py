from gilded_rose.item.item import Item
from gilded_rose.service.gilded_rose import GildedRose

items = [
    Item("Aged Brie", 2, 0),
]

app = GildedRose(items)

for day in range(10):
    print(f"\n--- Day {day} ---")
    for item in items:
        print(item)
    app.update_quality()
