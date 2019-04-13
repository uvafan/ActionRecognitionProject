import cv2, os

# Splits a video at location "file_path" + "/" + "filename" into "frames" equally spaced frames and outputs them to "output_path"
def split_video(file_path, filename, output_path, frames=10):
  video = cv2.VideoCapture(file_path + filename)
  total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  interval = total_frames // frames
  count = 0
  for i in range(0, total_frames):
    success, image = video.read()
    if i % interval == 0 and count < frames:
      cv2.imwrite(output_path + filename[:-4] + "_frame%d.jpg" % count, image)
      count += 1

# Where the UCF-101 data is saved and extracted to
# The dataset can be downloaded from here:  https://www.crcv.ucf.edu/data/UCF101/UCF101.rar
raw_data_path = "C:/Users/Patrick/Desktop/vision_project/UCF-101/"

# Where to output the split videos
output_path = "data/"

category_directories = os.listdir(r'' + raw_data_path)

for category in category_directories:
  videos = os.listdir(r'' + raw_data_path + category)
  print(category)
  if not os.path.exists("data/" + category):
    os.makedirs("data/" + category)
  for video in videos:
    if not os.path.exists("data/" + category + "/" + video[-11:-4]):
      os.makedirs("data/" + category + "/" + video[-11:-4])
    split_video(raw_data_path + category + "/", video, "data/" + category + "/" + video[-11:-4] + "/")