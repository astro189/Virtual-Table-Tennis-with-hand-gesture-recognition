import mediapipe as mp
import numpy as np
import cv2 as cv
import socket

mp_drawing=mp.solutions.drawing_utils

mp_hands=mp.solutions.hands

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ServerPort=("127.0.0.1",2345)

video=cv.VideoCapture(0)

height,width=1280,720
video.set(3,width)
video.set(4,height)


def get_label(index, hand, results):
    output = None
    for idx, classification in enumerate(results.multi_handedness):
        if classification.classification[0].index == index:
            
            # Process results
            label = classification.classification[0].label
            score = classification.classification[0].score
            text = '{} {}'.format(label, round(score, 2))
            
            # Extract Coordinates
            coords = tuple(np.multiply(
                np.array((hand.landmark[mp_hands.HandLandmark.WRIST].x, hand.landmark[mp_hands.HandLandmark.WRIST].y)),
            [width,height]).astype(int))
            
            output = text, coords
            
    return output

def get_landmarks(hand):
    landmarks=[]
    for id,landmark in enumerate(hand.landmark):
        cx,cy,cz=int(landmark.x*width),int(landmark.y*height),int(landmark.z*width)
        landmarks.append([cx,cy,cz])
    return landmarks

with mp_hands.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while True:
        isTrure,frame=video.read()

        #converting from BGR TO RGB
        img=cv.cvtColor(frame,cv.COLOR_BGR2RGB)

        #Flipping image horizontally
        #img = cv.flip(img, 1)

        #Setting writable to false
        img.flags.writeable=False

        #detecting the image
        results=hands.process(img)

        #coverting back to BGR
        img=cv.cvtColor(img,cv.COLOR_RGB2BGR)

        #Rendering results

        #Additional changes to the draw_landamrks functions of the drawings
        #For color: mp_drawing.DrawingSpec(color(R,G,B),thickness=k,circle_radius=z)
        
        if results.multi_hand_landmarks:
            for num,hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(img,hand,mp_hands.HAND_CONNECTIONS)

                # if get_label(num, hand, results):
                #         text, coord = get_label(num, hand, results)
                #         cv.putText(img, text, coord, cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
                #         #print(text)
                
                #creating data
                if get_landmarks(hand):
                    landmarks=get_landmarks(hand)
                
                    data=(round((landmarks[0][0]/600)*(5)-2.5,2)) #,height-landmarks[0][1],landmarks[0][2]])
                    # for lmd in landmarks:
                    #     data.extend([lmd[0],height-lmd[1],lmd[2]])
                
                #sending data to unity
                sock.sendto(str.encode(str(data)),ServerPort)




            #print(results.multi_hand_landmarks[1])
        cv.resize(img,(1280,620),interpolation=cv.INTER_AREA)

        cv.imshow('Video',img)
        if cv.waitKey(20) & 0XFF==ord('d'):
            break

video.release()
cv.destroyAllWindows()
cv.imshow()
