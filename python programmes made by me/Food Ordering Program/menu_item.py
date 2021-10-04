# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 02:20:16 2020

@author: admin
"""

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count

        if count >= 3:
            total_price *= 0.9

        return round(total_price)
