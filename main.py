import time

from utils import scr, debug
import processor

def main():
  #examples/example.mp4 or examples/example.jpg
  scr.erase()
  path = input("File path: ")

  target_fps = 10
  start_time = time.time()

  frames = processor.get_frames(path, target_fps)

  #Compilation info
  print(f"{len(frames)} frame(s) compiled in {time.time() - start_time} s")
  scr.wait_for_enter()

  debug.print(f"width: {scr.term.width} height: {scr.term.height}")

  with scr.term.hidden_cursor():
    #Loops through frames and displays them
    for frame in frames:
      scr.erase()
      rgb_frame, char_frame = frame

      debug.print(char_frame.shape)

      for y in range(len(char_frame)):
        for x in range(len(char_frame[0])):
          b, g, r = rgb_frame[y, x]
          char = char_frame[y, x]
          
          #forcing ansi kinda works, but super hacky and not intended. Maybe just need to abandon curses, idk
          #TODO: add color-256 / truecolor/ 24-bit color support somehow
          print(char, end="")
        print()

      time.sleep(1/target_fps)

  scr.wait_for_enter()

#Run main (safely)
debug.print("Program started")
with scr.term.fullscreen():
  main()
debug.print("Execution successfully completed")