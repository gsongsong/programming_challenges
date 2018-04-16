#!/bin/python3

# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

import sys

def designerPdfViewer(h, word):
    # Complete this function
    h_used = [h[i] for i in range(len(h)) if chr(ord('a') + i) in word]
    return max(h_used) * len(word)

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
