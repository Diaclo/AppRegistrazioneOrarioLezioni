
import cv2
import numpy
import pyautogui

class recordVideo:
   def __init__(self, durataVideo, nomeVideo):

      # tengo per ora variabili intermedie per testing,
      # alla fine sarà presente solo la conversione in ora e
      # si passerà come durata direttamente la durata in ore
      # minuto = 1440 # a 24 fps un minuto di video dura 1440 fps
      # ora = 86400 # minuto * 60 -> in fps
      # self.durata = durataVideo * ora

      fps = 24.0
      self.durata = durataVideo * int(fps)
      self.nome = nomeVideo + ".mp4"
      screenSize = pyautogui.size()
      outCodec = cv2.VideoWriter_fourcc(*'mp4v')
      out = cv2.VideoWriter(self.nome, outCodec, fps, screenSize)

      for i in range( self.durata ):
         img = pyautogui.screenshot()
         frame = numpy.array(img)
         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         out.write(frame)

      cv2.destroyAllWindows()
      out.release()
      print('...registrazione completata...')

video = recordVideo(20, 'prova')
