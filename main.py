from PIL import Image
import numpy as np

FILE_NAME = "example.jpg"
#Account for height of chars being greater than width by //2
IMG_SIZE = IMG_W, IMG_H = 380, 190 // 2
CORRECTION_FACTOR = 10
INVERSION = False

img = Image.open(FILE_NAME).resize(IMG_SIZE).convert("L")
arr = np.array(img)

letter_map = " .,:;coPO0@#"

for y in range(IMG_H):
  for x in range(IMG_W):
    L = int(arr[y, x]) - CORRECTION_FACTOR
    if L < 0: L = 0
    if L > 255: L = 255
    char_val = L/255 * (len(letter_map) - 1)
    if INVERSION: char_val = len(letter_map) - char_val - 1

    char = letter_map[int(char_val)]
    print(char, end="")
  print()
