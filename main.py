import cv2
import mediapipe as mp

# Initialize Mediapipe Hand Detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Load video or webcam
cap = cv2.VideoCapture('C:/Users/klaus/Downloads/Compressed/Web Developer Bootcamp/1. Introduction [Day 1]/video.mp4')  # Replace with 0 for webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB as Mediapipe works with RGB images
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks and bounding boxes if hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the frame
    cv2.imshow('Hand Detection', frame)
    if cv2.waitKey(30) & 0xFF == 27:  # Press ESC to quit
        break

cap.release()
cv2.destroyAllWindows()



