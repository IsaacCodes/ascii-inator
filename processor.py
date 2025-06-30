import mimetypes
import os
import cv2 as cv
import numpy as np

from utils import scr, debug

#Gets frames from given video/image
def get_frames(src_path: str, save_path: str, target_fps: int):

  #Gets file type
  file_type = mimetypes.guess_file_type(src_path)[0] or os.path.splitext(src_path)[1].lstrip(".")

  #Proccesses video
  if file_type.startswith("video"):
    #Open file
    text_frames = []
    cap = cv.VideoCapture(src_path)
    if not cap.isOpened():
      raise SystemExit("Error: Failed to load video")

    #Used to lower fps to target_fps
    fps_stabilizer = 0
    src_fps = cap.get(cv.CAP_PROP_FPS)
    if target_fps == 0: 
      target_fps = src_fps

    #Read through all frames
    print("Processing video...")
    frame_i = 0
    while cap.isOpened():
      ret, frame = cap.read()
      #When completed
      if not ret: break

      #Only process every target_fps / src_fps frames so as to reach target_fps
      fps_stabilizer += target_fps / src_fps
      if fps_stabilizer >= 1:
        text_frames.append(process_frame(frame))
        fps_stabilizer -= 1

      frame_i += 1
      scr.progress_bar(frame_i/cap.get(cv.CAP_PROP_FRAME_COUNT))
      
    cap.release()

  #Processes images
  elif file_type.startswith("image"):
    frame = cv.imread(src_path)

    if frame is None:
      raise SystemExit("Error: Failed to proccess image")
    
    text_frames = [process_frame(frame)]

  elif file_type == "npy":
    text_frames = np.load(src_path, allow_pickle=True)

  #On error
  else:
    raise SystemExit(f"Error: File type {file_type} not supported")
  
  if save_path:
    data_obj = np.empty(len(text_frames), dtype=object)
    for i, pair in enumerate(text_frames):
      data_obj[i] = pair

    np.save(save_path, data_obj, allow_pickle=True)

  return text_frames


LETTER_MAP = np.array(list(" .,-:;coaPO0@#"))

#Proccesses a frame into a np arr of characters
def process_frame(bgr_frame: np.ndarray):

  aspect_ratio = bgr_frame.shape[1] / bgr_frame.shape[0]
  height = 70
  bgr_frame = cv.resize(bgr_frame, (int(2*aspect_ratio*height), height))

  #Perform ITU-R 601-2 luma transform
  luma = cv.cvtColor(bgr_frame, cv.COLOR_BGR2GRAY)
  #Normalize into indicies
  normalized = (luma/255 * (len(LETTER_MAP) - 1)).astype(np.uint8)
  #Index for final characters
  chars = LETTER_MAP[normalized]

  return bgr_frame, chars