import cv2
import time
import mediapipe as mp


class handDetector:
    def __init__(self, mode=False, maxhand=2, detectionCon=int(0.1), trackingCon=int(0.1)):
        self.mode = mode
        self.maxhands = maxhand
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxhands, self.detectionCon, self.trackingCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findhands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS
                    )
        return img


    def findposition(self, img,handno = 0 ,draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handno]


            for id ,lm in enumerate(myhand.landmark):
                print(id,lm)
                h,w,c = img.shape
                cx , cy = int(lm.x*w),int(lm.y*h)
                # print(id,cx,cy)
                lmlist.append([id,cx,cy])
                # if id == 4 :
                #     cv2.circle(img,(cx,cy),9,(255,0,255),cv2.FILLED)

        return lmlist


def main():
    pTIME = 0
    cTIME = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()


    while True:
        success, img = cap.read()
        img = detector.findhands(img)
        lst = detector.findposition(img)
        if len(lst)!=0:
            print(lst[4])

        cTIME = time.time()
        fps = 1 / (cTIME - pTIME)
        pTIME = cTIME

        cv2.putText(
            img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
        )

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
