import time

import utils
import processor

t0 = time.time()
target_fps = 10
frames = processor.get_frames("examples/example.mp4", target_fps)
print(len(frames), "frames compiled in", time.time() - t0, "s")
time.sleep(2)

for frame in frames:
  utils.clear()
  rgb_frame, char_frame = frame

  for row in char_frame:
    print("".join(row))

  time.sleep(1/target_fps)