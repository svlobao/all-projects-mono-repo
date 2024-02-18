This project provides a script for blurring faces all faces in real time.

The face-detection algorithm used was the Haar Cascades, which is quite lightweight, but considerably limited:

- It fails detecting tilted and rotated faces
- Also, it won't detect faces that appear partially in the camera

The first milestone was to be able to access the notebooks camera, detect and blur all faces - which was successfuly achieved. Now, the next steps for this project are:

1. Use a more robust face-detection algorithm that does not bottleneck my Macbook M1's resources
2. Insert a feature so that the script does not blur known faces
