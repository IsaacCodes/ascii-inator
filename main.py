from time import sleep

import utils
import processor

frames = processor.get_frames("examples/example.mp4")
print()
print(len(frames), "frames compiled")
sleep(0.5)
utils.clear()
for frame in frames:
  rgb_frame, char_frame = frame

  for row in char_frame[450:520]:
    print("".join(row)[:650])

  sleep(0.5)
  utils.clear()