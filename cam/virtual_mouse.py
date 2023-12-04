import cv2
import mediapipe as mp
import pyautogui

camera = cv2.VideoCapture(0)
capture_hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils
screen_width,screen_height = pyautogui.size()
x1=x2=y1=y2=0

while True:
    _,img = camera.read()
    img = cv2.flip(img,1)
    rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    output_hand = capture_hands.process(rgb_img)
    all_hands = output_hand.multi_hand_landmarks

    if all_hands:
        for hand in all_hands:
            draw.draw_landmarks(img,hand)
            one_hand_landmarks = hand.landmark
            for id ,lm in enumerate(one_hand_landmarks):
                h,w,_ = img.shape
                x,y = int(lm.x*w),int(lm.y*h)
                if id == 8:
                    cv2.circle(img,(x,y),9,(0,0,255),cv2.FILLED)
                    mouse_x = int(screen_width/w*x)
                    mouse_y = int(screen_height/h*y)
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y
                    cv2.circle(img,(x,y),9,(0,0,255),cv2.FILLED)

        dist_y = y2-y1
        dist_x = x2-x1
        print(dist_y)
        if dist_y<27:
            pyautogui.doubleClick()

        if dist_x > 100:
            pyautogui.moveTo(None)




    cv2.imshow("Virtual Mouse",img)
    key = cv2.waitKey(100)
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()