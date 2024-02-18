import cv2


def detect_face(frame):
    cascade_classifier = cv2.CascadeClassifier(
        filename=cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    gray_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY,
    )

    faces = cascade_classifier.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    for x, y, w, h in faces:

        face_roi = frame[y : y + h, x : x + w]
        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)
        frame[y : y + blurred_face.shape[0], x : x + blurred_face.shape[1]] = (
            blurred_face
        )

        cv2.rectangle(
            img=frame,
            pt1=(x, y),
            pt2=(x + w, y + h),
            color=(255, 0, 0),
            thickness=2,
        )


"""
1. Compare the script readability between having the parameters explicit and not

"""
