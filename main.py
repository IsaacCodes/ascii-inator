import time

from utils import scr, debug
import processor

def main():
  #examples/example.mp4 or examples/example.jpg
  scr.home()
  path = input("File path: ")
  is_colored = input("Would you like to display in color? [y/n] ").lower() in ("y", "yes")
  print()

  target_fps = 10
  start_time = time.time()

  #Processes the image into frames
  with scr.term.cbreak(), scr.term.hidden_cursor():
    frames = processor.get_frames(path, target_fps)

  #Compilation info
  print(f"{len(frames)} frame(s) compiled in {time.time() - start_time} s")
  scr.wait_for_enter()
  scr.clear()

  debug.print(f"Screen Size (H,W): ({scr.term.height}, {scr.term.width})")

  #Hides the cursor
  with scr.term.cbreak(), scr.term.hidden_cursor():
    #Loops through frames and displays them
    for frame in frames:
      scr.home()
      debug.print(frame)
      bgr_frame, char_frame = frame

      debug.print(f"Frame Size (H,W): {char_frame.shape}")

      for y in range(len(char_frame)):
        for x in range(len(char_frame[0])):
          if is_colored:
            b, g, r = bgr_frame[y, x]
            print(scr.term.color_rgb(r, g, b), end="")

          print(char_frame[y, x], end="")
        print()

      #time.sleep(1/target_fps)

  print(scr.term.normal, end="")
  scr.wait_for_enter()

#Run main in fullscreen
debug.print("Program started")
with scr.term.fullscreen():
  main()
debug.print("Program stopped")

#TODO:
# Try to make color look better in general 
# Color is ridiculuosly slow for video, speed it up
# See if there are any other general performance optimizations
# Account for printing time in time.sleep, could help smooth color performance
# Caching would be neat
# Would like to supress key codes in input() for scrolling + arrow keys