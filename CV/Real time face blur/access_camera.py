import cv2
import platform
from face_detection import detect_face


class UnsupportedOSException(Exception):
    def __init__(self, os_name: str) -> None:
        self.os_name = os_name
        super().__init__(
            f"Unsupported OS: {os_name}. Currently, this script supports only macOS.\n"
        )


def get_os():
    system = platform.system()
    if (
        system == "Darwin"
    ):  # Write a different OS name if you wish to test your exception
        return True
    raise UnsupportedOSException(os_name=system)


def access_camera():
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        raise Exception("Error: camera was not found or could not be opened.\n")

    frame_was_read = True
    while True and frame_was_read:
        frame_was_read, frame = capture.read()
        detect_face(frame=frame)
        cv2.imshow("Camera", mat=frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    if get_os():
        access_camera()


"""
Set of questions:

1. How do I raise an exception? 
2. What if I want to raise a reusable custom exception?
3. Does Python treat exceptions as a "False"? 
4. What would happen if I used "cv2.waitKey(-1)" or "cv2.waitKey(0)"?
5. What is 0xFF?
6. What is __name__?

"""
