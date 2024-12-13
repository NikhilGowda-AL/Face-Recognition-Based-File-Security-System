
import cv2
import face_recognition
import pickle
import os
import time

DATA_DIR = "User_Data"

def authenticate_user():
    video_capture = cv2.VideoCapture(0)
    print("[INFO] Authenticating. Look at the camera...")

    start_time = time.time()
    while time.time() - start_time < 10:  # Allow 10 seconds for authentication
        ret, frame = video_capture.read()
        if not ret:
            print("[ERROR] Unable to access the camera.")
            break

        face_locations = face_recognition.face_locations(frame)

        if len(face_locations) == 1:
            face_encoding = face_recognition.face_encodings(frame, face_locations)[0]

            for user_file in os.listdir(DATA_DIR):
                user_file_path = os.path.join(DATA_DIR, user_file)
                if not user_file.endswith(".pkl"):
                    continue

                try:
                    with open(user_file_path, "rb") as f:
                        saved_encoding = pickle.load(f)
                    match = face_recognition.compare_faces([saved_encoding], face_encoding, tolerance=0.6)
                    if match[0]:
                        print(f"[INFO] Authentication successful for user {user_file.split('.')[0]}.")
                        video_capture.release()
                        cv2.destroyAllWindows()
                        return True
                except Exception as e:
                    print(f"[ERROR] Failed to load encoding: {e}")

        cv2.imshow("Authenticate", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Authentication cancelled.")
            break

    print("[ERROR] Authentication failed.")
    video_capture.release()
    cv2.destroyAllWindows()
    return False
