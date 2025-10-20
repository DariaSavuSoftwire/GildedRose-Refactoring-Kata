# -*- coding: utf-8 -*-
from unittest import case

class GildedRose(object):
    CONJURED_MULTIPLIER = 2
    STANDARD_MULTIPLIER = 1

    def __init__(self, items):
        self.items = items

    def get_multiplier(self, item):
        return GildedRose.CONJURED_MULTIPLIER if item.name.startswith("Conjured") else GildedRose.STANDARD_MULTIPLIER

    def update_standard_item(self, item, multiplier, is_backstage_pass=False, sign=1):
        if is_backstage_pass:
            item.quality = 0 if item.sell_in <= 0 else item.quality + (
                3 if item.sell_in <= 5 else 2 if item.sell_in <= 10 else 1) * multiplier
        else:
            if item.sell_in <= 0:
                item.quality += 1 * sign * multiplier
            item.quality += 1 * sign * multiplier
        item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            match item.name:
                case name if "Aged Brie" in name:
                    self.update_standard_item(item, self.get_multiplier(item), False, 1)
                case name if "Sulfuras" in name:
                    continue
                case name if "Backstage passes" in name:
                    self.update_standard_item(item, self.get_multiplier(item), True, 1)
                case _:
                    self.update_standard_item(item, self.get_multiplier(item), False, -1)
            item.quality = min(max(item.quality, 0), 50)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
