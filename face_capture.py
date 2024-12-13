import cv2
import face_recognition
import pickle
import os
import time

DATA_DIR = "User_Data"

def capture_user_face(username):
    video_capture = cv2.VideoCapture(0)
    print("[INFO] Capturing face. Look at the camera...")

    face_encoding = None
    start_time = time.time()
    while time.time() - start_time < 10:  # Allow 10 seconds to capture a face
        ret, frame = video_capture.read()
        if not ret:
            print("[ERROR] Unable to access the camera.")
            break

        face_locations = face_recognition.face_locations(frame)

        if len(face_locations) == 1:
            face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
            print("[INFO] Face detected.")
            cv2.imshow("Capture Face", frame)
            cv2.waitKey(2000)  # Wait for 2 seconds to confirm
            break
        else:
            print("[ERROR] Ensure only your face is visible!")

        cv2.imshow("Capture Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Capture cancelled.")
            break

    video_capture.release()
    cv2.destroyAllWindows()

    if face_encoding is None:
        print("[ERROR] Failed to capture a valid face.")
        return False

    user_data_path = os.path.join(DATA_DIR, f"{username}.pkl")
    try:
        with open(user_data_path, "wb") as f:
            pickle.dump(face_encoding, f)
        print(f"[INFO] Face captured and stored for user '{username}'.")
    except Exception as e:
        print(f"[ERROR] Failed to save face encoding: {e}")
        return False

    return True