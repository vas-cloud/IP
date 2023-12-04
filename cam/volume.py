import cv2
import mediapipe as mp
import pyautogui

x1=0
x2=0
y1=0
y2=0
web_cam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

while True:
    _, img = web_cam.read()
    img = cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = my_hands.process(imgRGB)
    # hands = results.multi_hand_landmarks
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id ,lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c = img.shape
                x , y = int(lm.x*w),int(lm.y*h)
                # print(id,cx,cy)
                if id == 4 :
                    cv2.circle(img,(x,y),9,(0,0,255),cv2.FILLED)
                    x1=x
                    y1=y
                if id == 8 :
                    cv2.circle(img,(x,y),9,(255,0,0),cv2.FILLED)
                    x2=x
                    y2=y

        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),7)
        distance = ((x2-x1)**2 + (y2-y1)**2)**(0.5)//4
        if distance>40:
            pyautogui.press("volumeup")
        
        else:
            pyautogui.press("volumedown")
        draw.draw_landmarks(img, handLms)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
 