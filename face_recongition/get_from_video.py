import cv2
import os




class HassFace(): 
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('entities/haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier("entities/haarcascade_eye.xml")

    def face_video(self, name):
        video = cv2.VideoCapture(0)
        i = 0
        j = 0
        if not os.path.exists("faces/" + name):
            os.makedirs("faces/" + name)
        else:
            os.removedirs("faces/" + name)
            os.makedirs("faces/" + name)
        while(True):
            if j == 20:
                break
            if i%5 == 0: 
                ret, frame = video.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.3,
                    minNeighbors=3,
                    minSize=(10, 10)
                )
                if len(faces) != 0:
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        roi_color = frame[y:y + h, x:x + w]
                        roi_gray = gray[y:y+h, x:x+w]
                        eyes = self.eye_cascade.detectMultiScale(roi_gray)
                        if len(eyes) > 0:
                            print("Save data with: ", j+1)
                            cv2.imwrite("faces/"+name+"/"+str(w) + str(h) + '_faces.jpg', roi_color)
                            j += 1
            i+= 1
if __name__ == "__main__":

    name_in = str(input("Name: "))
    HassFace().face_video(name=name_in)
