# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:04:38 2017

@author: LANG
"""

def BinarySearch(array,t):
    low = 4
    height = 7
    while low < height:
        mid = int((low+height)/2)
        if array[mid] < t:
            low = mid + 1

        elif array[mid] > t:
            height = mid - 1

        else:
            return array[mid]

    return -1


if __name__ == "__main__":
    print(BinarySearch([1,2,3,34,56,57,78,87],57))