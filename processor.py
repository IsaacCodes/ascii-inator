import mimetypes
import cv2 as cv
import numpy as np

import utils

def get_frames(path: str):

  #Gets file type
  file_type = mimetypes.guess_file_type(path)[0]
  if file_type == None:
    raise SystemExit("File type not found")

  #Proccesses video
  if file_type.startswith("video"):
    #Open file
    text_frames = []
    cap = cv.VideoCapture(path)
    if not cap.isOpened():
      raise SystemExit("Failed to proccess video")

    # TODO: Mod for lower fps + frame_size
    print(cap.get(cv.CAP_PROP_FPS), cap.read()[1].shape)
    print("Processing video...")

    #Read through all frames
    frame_i = 0
    while cap.isOpened():
      ret, frame = cap.read()
      #When completed
      if not ret or frame_i == 20: break #DEBUG: breaking early
      #Proccess and add
      text_frames.append((frame, process_frame(frame)))

      frame_i += 1
      utils.progress_bar(frame_i/cap.get(cv.CAP_PROP_FRAME_COUNT))
      
    cap.release()

    return text_frames

  #Proccesses images
  elif file_type.startswith("image"):
    pass

  #On error
  else:
    raise SystemExit("File type not supported")
  


LETTER_MAP = np.array(list(" .,:;coPO0@#"))

def process_frame(bgr_frame: np.ndarray):
  #Split bgr_frame up
  b, g, r = bgr_frame[:, :, 0], bgr_frame[:, :, 1], bgr_frame[:, :, 2]
  #Perform ITU-R 601-2 luma transform
  luma = 0.299 * r + 0.587 * g + 0.114 * b
  #Normalize it into indicies
  normalized = (luma/255 * (len(LETTER_MAP) - 1)).astype(np.uint8)
  #Index for final characters
  chars = LETTER_MAP[normalized]

  #DEBUG: 
  #print(b.dtype, luma.dtype, normalized.dtype, chars.dtype)
  return chars