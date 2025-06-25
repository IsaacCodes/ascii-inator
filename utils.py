import curses

#For error logging
def log_error(message):
  with open("debug.log", "a") as f:
    print(message, file=f)

def log_clear():
  with open('debug.log', 'w'): 
    pass

class screen():
  def __init__(self, stdscr: curses.window):
    self.stdscr = stdscr

  #Prints and flushes message, no "\n" included
  def print(self, message="", flush=True):
    self.stdscr.addstr(message)
    if flush: self.stdscr.refresh()

  #Gets user input with curses
  def input(self, message=""):
    self.print(message)

    curses.echo()
    response = self.stdscr.getstr().decode("utf-8")
    curses.noecho()

    return response

  #Prints a progress bar for completion percent
  def progress_bar(self, completion: float, length=20):
    hashtags = round(completion * length)
    spaces = length - hashtags
    
    self.print("\r[" + hashtags*"#" + spaces*" " + "]")
    if completion == 1: self.print("\nDone!\n")

  #Waits for the enter key to be pressed
  def wait_for_enter(self):
    curses.flushinp()
    #Platform independent newline, "\n" = 10, "\r" = 13, KEY_ENTER
    while self.stdscr.getch() not in (10, 13, curses.KEY_ENTER):
      self.print("\r[ Press Enter to Continue ]")