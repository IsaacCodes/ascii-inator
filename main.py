import time
import numpy as np

from utils import scr, debug
import processor

def main():
  #examples/example.mp4 or examples/example.jpg
  scr.home()
  src_path = input("Source location: ")
  save_path = input("Save location (enter for none): ")
  is_colored = input("Display in color [y/n]: ").lower() in ("y", "yes")
  print()

  target_fps = 10
  process_start_time = time.time()

  #Processes the image into frames
  with scr.term.cbreak(), scr.term.hidden_cursor():
    frames_arr = processor.get_frames(src_path, save_path, target_fps)
    #Turns the [[color, char], [color, char], ...] frames_arr into [str, str, ...] frames
    if not is_colored:
      frames = [frame[1] for frame in frames_arr]
    else:
      frames = []
      for bgr_frame, char_frame in frames_arr:
        #Turns g, b, r int values into one ansi code str
        #Signature tells it to operate on the groups of 3 (1d subarrays) instead of on the individual ints
        color_vec = np.vectorize((lambda bgr: scr.term.color_rgb(bgr[2], bgr[1], bgr[0])), signature="(3)->()", otypes=[object])
        #Combines the colors with their respective chars
        colored_char_frame = color_vec(bgr_frame) + char_frame
        frames.append(colored_char_frame)

  #Compilation info
  print(f"{len(frames)} frame(s) compiled in {time.time() - process_start_time} s")
  scr.wait_for_enter()
  scr.clear()

  debug_times = []
  debug.print(f"Screen Size (H,W): ({scr.term.height}, {scr.term.width})")
  debug.print(f"Frame Size (H,W): {frames[0][1].shape}")

  #Hides the cursor
  with scr.term.cbreak(), scr.term.hidden_cursor():
    #Loops through frames and displays them
    for frame in frames:
      frame_start_time = time.time()
      scr.home()

      print("\n".join("".join(row) for row in frame))

      delta_time = time.time() - frame_start_time
      sleep_time = max(0, 1/target_fps - delta_time)

      debug_times.append((time.time() - frame_start_time) * 1000)
      debug.print(f"Time to print frame {debug_times[-1]} ms")

      time.sleep(sleep_time)

  debug.print(f"Total Time to print frame {sum(debug_times)} ms")
  debug.print(f"AVG Time to print frame {sum(debug_times)/len(debug_times)} ms")
  print(scr.term.normal, end="")
  scr.wait_for_enter()

#Run main in fullscreen
debug.print("Program started")
with scr.term.fullscreen():
  main()
debug.print("Program stopped")

#TODO:
# Try to make color look better in general (styles?)
# Color is ridiculuosly slow for video, speed it up (imbed codes in char_frame? avoid so many prints?)
# See if there are any other general performance optimizations
# Account for printing time in time.sleep, could help smooth color performance
# Would like to supress key codes in input() for scrolling + arrow keys
# Better screen size management