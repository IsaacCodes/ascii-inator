from PIL import Image
import numpy as np
import os

FILE_NAME = "example.jpg"
#Account for height of chars being greater than width by //2
IMG_SIZE = IMG_W, IMG_H = 380, 190 // 2
CORRECTION_FACTOR = -10
INVERSION = False

img_rgb = Image.open(FILE_NAME).resize(IMG_SIZE).convert("RGB")
img_l = img_rgb.convert("L")
arr_rgb = np.array(img_rgb)
arr_l = np.array(img_l)

letter_map = " .,:;coPO0@#"

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

clear()

for y in range(IMG_H):
  for x in range(IMG_W):
    L = int(arr_l[y, x]) - CORRECTION_FACTOR
    if L < 0: L = 0
    if L > 255: L = 255
    char_val = L/255 * (len(letter_map) - 1)
    if INVERSION: char_val = len(letter_map) - char_val - 1

    r, g, b = map(int, arr_rgb[y, x])

    char = letter_map[int(char_val)]
    print(f"\x1b[38;2;{r};{g};{b}m" + char, end="")
  print()
