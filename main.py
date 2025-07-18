import time

from utils import scr, debug, get_file_ext
import processor

def main():
  #Get info about the file to process
  scr.home()
  src_path = input("Source location: ")
  #These options can be skipped for .npy save files as they are already configured
  if get_file_ext(src_path) == "npy":
    save_path, is_colored = "", True
  else:
    save_path = input("Save location (enter for none): ")
    is_colored = get_file_ext(src_path) == "npy" or input("Display in color [y/n]: ").lower() in ("y", "yes")
  print()

  target_fps = 10
  process_start_time = time.time()

  #Processes the image into frames
  with scr.term.cbreak(), scr.term.hidden_cursor():
    frames = processor.get_frames(src_path, save_path, target_fps, is_colored)

  #Compilation info
  compile_time = time.time() - process_start_time
  print(f"{len(frames)} frame(s) compiled in {compile_time} s")
  scr.wait_for_enter()
  scr.clear()

  debug.print(f"Compile time: {compile_time} s")
  debug.print(f"Screen Size (H,W): ({scr.term.height}, {scr.term.width})")
  debug.print(f"Frame Size (H,W): {frames[0].shape}")
  debug_times = []

  #Hides the cursor
  with scr.term.cbreak(), scr.term.hidden_cursor():
    #Loops through frames and displays them
    for frame in frames:
      frame_start_time = time.time()

      #Print new frame
      scr.home()
      print("\n".join("".join(row) for row in frame))

      #Calculate time to sleep
      delta_time = time.time() - frame_start_time
      sleep_time = max(0, 1/target_fps - delta_time)

      debug_times.append((time.time() - frame_start_time) * 1000)
      debug.print(f"Time to print frame {debug_times[-1]} ms")

      time.sleep(sleep_time)

  debug.print(f"Total Time to print frame {sum(debug_times)} ms")
  debug.print(f"AVG Time to print frame {sum(debug_times)/len(debug_times)} ms")

  #Clean up
  print(scr.term.normal, end="")
  scr.wait_for_enter()

#Run main in fullscreen
debug.print("Program started")
with scr.term.fullscreen():
  main()
debug.print("Program stopped")

#TODO:
# Try to make color look better in general (styles?)

# Better screen size management
# Custom fps?
# CLI flags instead of / along with inputs

# Suppress key codes in input() for scrolling + arrow keys?
# Test on windows?