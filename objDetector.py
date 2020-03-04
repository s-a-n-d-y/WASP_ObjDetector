import cv2
import numpy as np
import os

class ObjDetector:
    def __init__(self, file_dir='', file_name='', show_inp_video=True):
        self.model = []
        self.show_inp_video = show_inp_video
        self.file_name = file_name
        self.file_dir = os.path.join(os.getcwd(), file_dir)
        self.file_path = os.path.join(self.file_dir, self.file_name)
    # Do inferencing on the frames using the trained NN model
    def process_frame(self, frame):
        # Work on the frame here by applying different model
        print (frame)

    # Read the camera data from webcam/file
    def open_video_stream(self): 
        if os.path.isfile(self.file_path):
            cap = cv2.VideoCapture(self.file_path)
        
        else:
            cap = cv2.VideoCapture(0)

        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            #color = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            self.process_frame(frame)

            if self.show_inp_video:
                # Display the resulting frame
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

# Just a simple example
o = ObjDetector(True)
o.open_video_stream()
