
import cv2
import numpy
import pyautogui

class recordVideo:
   def __init__(self, durataVideo):
      self.durata = durataVideo
      screenSize = pyautogui.size()
      outCodec = cv2.VideoWriter_fourcc(*"XVID")
      fps = 24.0
      minuto = 1440 # a 24 fps un minuto di video dura 1440 fps
      ora = 86400 # minuto * 60 -> in fps
      out = cv2.VideoWriter("output.avi", outCodec, fps, screenSize)
      i = 0
      for i in range( ora * self.durata ):
         img = pyautogui.screenshot()
         frame = numpy.array(img)
         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         out.write(frame)
         cv2.imshow("screenshot", frame)

      cv2.destroyAllWindows()
      out.release()

video = recordVideo(3)

