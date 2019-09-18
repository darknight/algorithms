#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    index = range(len(price))
    price_with_index = list(zip(price, index))
    price_with_index.sort(key=lambda x: x[0])
    min_loss = 10 ** 16
    for i in range(len(price)-1):
        # if price is lower but original index is larger
        if price_with_index[i][1] > price_with_index[i+1][1]:
            min_loss = min(min_loss, price_with_index[i+1][0] - price_with_index[i][0])

    return min_loss

if __name__ == '__main__':
    assert minimumLoss([5, 10, 3]) == 2
    assert minimumLoss([20, 7, 8, 2, 5]) == 2
