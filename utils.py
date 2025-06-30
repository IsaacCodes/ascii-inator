from blessed import Terminal

#TODO: maybe turn this into a class + do some reorganizing

#For error logging
class Debug():
  def __init__(self, location):
    self.file = open(location, 'a')
    self.file.truncate(0)

  def __del__(self):
    self.file.close()

  def print(self, *args, **kwargs):
    print(*args, **kwargs, file=self.file)

#Controls the terminal screen
class Screen():
  def __init__(self):
    self.term = Terminal()

  def erase(self):
    print(scr.term.clear, end="", flush=True)

  def wait_for_enter(self):
    with self.term.cbreak():
      #Platform independent newline (hopefully)
      while self.term.inkey() not in (self.term.KEY_ENTER, "\n", "\r"):
        print("[ Press Enter to Continue ]")

  def progress_bar(self, completion: float, length=20):
    hashtags = round(completion * length)
    spaces = length - hashtags
    
    return

    self.print("\r[" + hashtags*"#" + spaces*" " + "]")
    if completion == 1: self.print("\nDone!\n")


scr = Screen()
debug = Debug("debug.log")

  # #TODO: myb use addch for message of length 1
  # #Prints and flushes message, no "\n" included
  # def print(self, message="", flush=True):
  #   self.stdscr.addstr(message)
  #   if flush: self.stdscr.refresh()

  # #Gets user input with curses
  # def input(self, message=""):
  #   self.print(message)

  #   curses.echo()
  #   response = self.stdscr.getstr().decode("utf-8")
  #   curses.noecho()

  #   return response

  # #Prints a progress bar for completion percent
  # def progress_bar(self, completion: float, length=20):
  #   hashtags = round(completion * length)
  #   spaces = length - hashtags
    
  #   self.print("\r[" + hashtags*"#" + spaces*" " + "]")
  #   if completion == 1: self.print("\nDone!\n")

  # #Waits for the enter key to be pressed
  # def wait_for_enter(self):
  #   curses.flushinp()
  #   #Platform independent newline, "\n" = 10, "\r" = 13, KEY_ENTER
  #   while self.stdscr.getch() not in (10, 13, curses.KEY_ENTER):
  #     self.print("\r[ Press Enter to Continue ]")