# -*- coding: utf-8 -*-
from unittest import case


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def isConjured(self, item):
        return 2 if item.name.find("Conjured") != -1 else 1

    def get_item_category(self, item):
        match item.name:
            case name if "Aged Brie" in name:
                return "Aged Brie"
            case name if "Sulfuras" in name:
                return "Sulfuras"
            case name if "Backstage passes" in name:
                return "Backstage passes"
            case _:
                return "Normal"

    def update_standard_item(self, item, is_conjured, sign=1):
        if item.sell_in <= 0:
            item.quality += 1 * sign * is_conjured
        item.quality += 1 * sign * is_conjured
        item.sell_in -= 1

    def update_backstage_passes(self, item, is_conjured):
        item.quality = 0 if item.sell_in <= 0 else item.quality + (
            3 if item.sell_in <= 5 else 2 if item.sell_in <= 10 else 1) * is_conjured
        item.sell_in -= 1

    def update_conjured(self, item, is_conjured):
        if item.sell_in <= 0:
            item.quality -= 2
        item.quality -= 2
        item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            item_category = self.get_item_category(item)
            is_conjured = self.isConjured(item)
            if item_category == "Sulfuras":
                continue
            elif item_category == "Normal":
                self.update_standard_item(item, is_conjured, -1)
            elif item_category == "Aged Brie":
                self.update_standard_item(item, is_conjured, 1)
            elif item_category == "Backstage passes":
                self.update_backstage_passes(item, is_conjured)
            elif item_category == "Conjured":
                self.update_conjured(item, is_conjured)
            item.quality = min(max(item.quality, 0), 50)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
