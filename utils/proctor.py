import cv2
import mediapipe as mp


class AIProctor:

    def __init__(self):

        # MediaPipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # Drawing utility
        self.drawer = mp.solutions.drawing_utils

    def analyze(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.face_mesh.process(rgb)

        status = {
            "face_detected": False,
            "confidence": 0,
            "message": "❌ No Face Detected"
        }

        if results.multi_face_landmarks:

            face_landmarks = results.multi_face_landmarks[0]

            h, w, _ = frame.shape

            # Draw Face Mesh
            self.drawer.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None
            )

            # -------------------------------
            # Simple Head Direction Detection
            # -------------------------------

            nose = face_landmarks.landmark[1]

            nose_x = int(nose.x * w)

            center_x = w // 2

            difference = nose_x - center_x

            if difference < -40:
                direction = "⬅️ Looking Left"

            elif difference > 40:
                direction = "➡️ Looking Right"

            else:
                direction = "👀 Looking Center"

            cv2.putText(
                frame,
                direction,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            status = {
                "face_detected": True,
                "confidence": 100,
                "message": direction
            }

        else:

            cv2.putText(
                frame,
                "❌ No Face Detected",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        return frame, status