# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item_before_sell_date(self):
        item = Item("Normal Item", sell_in=10, quality=20)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)

    def test_normal_item_on_sell_date(self):
        item = Item("Normal Item", sell_in=0, quality=20)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 18)  # quality degrades twice as fast

    def test_normal_item_after_sell_date(self):
        item = Item("Normal Item", sell_in=-1, quality=20)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 18)

    def test_quality_never_negative(self):
        item = Item("Normal Item", sell_in=5, quality=0)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality, 0)

    def test_aged_brie_increases_quality(self):
        item = Item("Aged Brie", sell_in=5, quality=10)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality, 11)

    def test_quality_never_more_than_50(self):
        item = Item("Aged Brie", sell_in=5, quality=50)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality, 50)

    def test_sulfuras_never_changes(self):
        item = Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=30)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 30)

    def test_backstage_pass_increase_quality(self):
        item = Item("Backstage passes", sell_in=15, quality=20)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality, 21)

    def test_backstage_pass_10_days_or_less(self):
        item = Item("Backstage passes", sell_in=10, quality=20)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality, 22)

    def test_backstage_pass_5_days_or_less(self):
        item = Item("Backstage passes", sell_in=5, quality=20)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality, 23)

    def test_backstage_pass_after_concert(self):
        item = Item("Backstage passes", sell_in=0, quality=20)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality, 0)

    def test_conjured_item_degrades_twice_as_fast(self):
        item = Item("Conjured Mana Cake", sell_in=3, quality=6)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality, 4)

    def test_conjured_item_after_sell_date(self):
        item = Item("Conjured Mana Cake", sell_in=0, quality=6)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(item.quality, 2)

        
if __name__ == '__main__':
    unittest.main()
