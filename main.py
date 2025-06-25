import time
import curses

import utils
import processor

def main(stdscr: curses.window):

  scr = utils.screen(stdscr)

  #examples/example.mp4 or examples/example.jpg
  path = scr.input("File path: ")
  target_fps = 10
  t0 = time.time()

  frames = processor.get_frames(scr, path, target_fps)

  #Compilation info
  scr.print(f"{len(frames)} frame(s) compiled in {time.time() - t0} s\n")
  scr.wait_for_enter()
  curses.curs_set(0)

  utils.log_error(stdscr.getmaxyx())

  #Loops through frames and displays them
  for frame in frames:
    stdscr.erase()
    rgb_frame, char_frame = frame

    for row in char_frame:
      utils.log_error(f"y, x: {str(stdscr.getyx()).ljust(10)} {"".join(row)}")
      scr.print("".join(row) + "\n", False)

    stdscr.refresh()
    time.sleep(1/target_fps)

  curses.curs_set(1)
  scr.wait_for_enter()

#Run main (safely)
utils.log_clear()
utils.log_error("Program started")
curses.wrapper(main)
utils.log_error("Execution successfully completed")