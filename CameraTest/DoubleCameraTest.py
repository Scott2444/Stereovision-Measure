import cv2 as cv

# Open the default camera
leftCam = cv.VideoCapture(1)
rightCam = cv.VideoCapture(0)

# Get the default frame width and height
frame_width = int(rightCam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(rightCam.get(cv.CAP_PROP_FRAME_HEIGHT))

print(f"Width: {frame_width} px")
print(f"Height: {frame_height} px")

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
# out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    # Capture a frame and display it
    _, leftFrame = leftCam.read()
    cv.imshow('Left Camera', leftFrame)

    _, rightFrame = rightCam.read()
    cv.imshow('Right Camera', rightFrame)

    # Press 'q' to exit the loop
    if cv.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
leftCam.release()
rightCam.release()
# out.release()
cv.destroyAllWindows()