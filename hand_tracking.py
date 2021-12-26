from cvzone.HandTrackingModule import HandDetector
import cv2

# Video resolution
wCam = 1280
hCam = 720

# Declaration of capture device
cap = cv2.VideoCapture(0)

# Set resolution of the processed video
cap.set(3, wCam)
cap.set(4, hCam)

# Hand detector
detector = HandDetector(detectionCon=0.7, maxHands=1)


class CvHand:
    # Hand position from the previous frame
    # On declaration is initialized with 'w'
    oldHandPoint = 'w'

    # Mirror video
    flip = False

    # Declaration of variables containing center coordinates
    cx = 0.0
    cy = 0.0

    # Function to transform coordinates to one of the 4 sides:
    # Up - w
    # Down - s
    # Left - a
    # Right - d
    def process_position(self, centerPoint):
        # Flip frame
        if self.flip is False:
            self.cx = (wCam - centerPoint[0]) / wCam
        else:
            self.cx = centerPoint[0] / wCam
        self.cy = centerPoint[1] / hCam
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
            hand1 = hands[0]
            centerPoint1 = hand1['center']  # center of the hand cx,cy
            self.oldHandPoint = self.process_position(centerPoint1)
            return self.oldHandPoint
        else:
            return self.oldHandPoint


# End program with this method
def release_capture():
    cap.release()