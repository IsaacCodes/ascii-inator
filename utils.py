from blessed import Terminal
import os

#To get npy ext
def get_file_ext(file_path: str):
  return os.path.splitext(file_path)[1].lstrip(".")

#For error logging
class Debug():
  def __init__(self, location, enabled):
    self.enabled = enabled
    self.file = open(location, 'a')
    self.file.truncate(0)

  def __del__(self):
    self.file.close()

  def print(self, *args, **kwargs):
    if self.enabled:
      print(*args, **kwargs, file=self.file, flush=True)

#Controls the terminal screen
class Screen():
  def __init__(self):
    self.term = Terminal()

  def home(self):
    print(scr.term.home, end="", flush=True)

  def clear(self):
    print(scr.term.home + scr.term.clear, end="", flush=True)

  def wait_for_enter(self):
    with self.term.cbreak():
      print("[ Press Enter to Continue ]")
      #Platform independent newline (hopefully)
      while self.term.inkey() not in (self.term.KEY_ENTER, "\n", "\r"): pass

  def progress_bar(self, completion: float, length=25):
    hashtags = round(completion * length)
    spaces = length - hashtags
    
    print("\r" + self.term.bold(f"{int(100*completion):>3}%"), end=" ")
    print("[" + hashtags*"#" + spaces*" " + "]", end="")
    if completion == 1: 
      print("\nDone!\n")

scr = Screen()
debug = Debug("debug.log", True)