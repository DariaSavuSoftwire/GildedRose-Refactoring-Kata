# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def get_item_category(self,item):
        special_object_names = ["Aged Brie", "Sulfuras", "Backstage passes", "Conjured"]
        for special_name in special_object_names:
            if item.name.startswith(special_name):
                return special_name
        return "Normal"

    def update_normal_item(self,item):
        if item.sell_in<=0:
            item.quality-=1
        item.quality-=1
        item.sell_in-=1

    def update_aged_brie(self,item):
        if item.sell_in <= 0:
            item.quality+=1
        item.quality+=1
        item.sell_in-=1

    def update_backstage_passes(self,item):
        if item.sell_in <= 0:
            item.quality=0
        elif item.sell_in <= 5:
            item.quality+=3
        elif item.sell_in <= 10:
            item.quality+=2
        else:
            item.quality+=1
        item.sell_in-=1

    def update_conjured(self,item):
        if item.sell_in <= 0:
            item.quality-=2
        item.quality-=2
        item.sell_in-=1

    def update_quality(self):
        for item in self.items:
            item_category=self.get_item_category(item)
            if item_category == "Sulfuras":
                continue
            elif item_category == "Normal":
                self.update_normal_item(item)
            elif item_category == "Aged Brie":
                self.update_aged_brie(item)
            elif item_category == "Backstage passes":
                self.update_backstage_passes(item)
            elif item_category == "Conjured":
                self.update_conjured(item)
            item.quality=min(max(item.quality,0),50)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
