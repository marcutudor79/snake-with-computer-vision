from cvzone.HandTrackingModule import HandDetector
import cv2
import time
import mediapipe as mp

# Video resolution - Changed to optimal resolution
wCam = 640
hCam = 480

# Declaration of capture device
cap = cv2.VideoCapture(0)

# Set resolution of the processed video
cap.set(3, wCam)
cap.set(4, hCam)

# Hand detector
detector = HandDetector(detectionCon=0.7, maxHands=1)


class CvHand:
    # Hand side from the previous frame
    # On declaration is initialized with 'w'
    oldHandSide = 'w'

    # Mirror video
    flip = False

    # Declaration of variables containing center coordinates
    cx = 0.0
    cy = 0.0

    # Fps counter
    pTime = 0
    cTime = 0
    fps = 0

    # Function to transform coordinates to one of the 4 sides:
    # Up - w
    # Down - s
    # Left - a
    # Right - d
    def process_position(self, point):
        # Mirror frame if self.flip is True
        if self.flip is False:
            self.cx = (wCam - point[0]) / wCam
        else:
            self.cx = point[0] / wCam
        self.cy = point[1] / hCam

        # Over main diagonal
        if self.cx >= self.cy:
            # Over minor diagonal -> Up
            if self.cx + self.cy <= 1:
                return 'w'
            # Under minor diagonal -> Right
            else:
                return 'd'
        # Under main diagonal
        else:
            # Over minor diagonal -> Left
            if self.cx + self.cy <= 1:
                return 'a'
            # Under minor diagonal -> Down
            else:
                return 's'

    # Capture frame and return hand side if it is detected or previous hand side
    def current_hand_side(self):
        # Get image frame
        success, img = cap.read()
        # Find the hand and its landmarks
        hands = detector.findHands(img, draw=False)  # No Draw
        # If hand is detected
        if hands:
            # First hand detected
            hand_center_point = hands[0]['center']  # center of the hand cx,cy
            self.oldHandSide = self.process_position(hand_center_point)

            # Fps counter update
            self.cTime = time.time()
            self.fps = 1 / (self.cTime - self.pTime)
            self.pTime = self.cTime

            return self.oldHandSide
        else:
            # Fps counter update
            self.cTime = time.time()
            self.fps = 1 / (self.cTime - self.pTime)
            self.pTime = self.cTime

            return self.oldHandSide

    # Returns fps
    def fps_counter(self):
        return self.fps

    # Shows image with the hand
    def show_image(self):
        success, img = cap.read()
        cv2.imshow("handtraking", img)

# End program with this method
def release_capture():
    cap.release()