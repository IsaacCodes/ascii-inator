import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def progress_bar(completion: float, length=20):
  hashtags = round(completion * length)
  spaces = length - hashtags
  print("\r[" + hashtags*"#" + spaces*" " + "]", end="")
  if completion == 1:
    print("\nDone!")