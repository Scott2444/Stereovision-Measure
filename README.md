# Stereovision-Measure

This project aims to determine the length of an object using stereoscopic vision and object detection computer vision. Two cameras are mounted at a fixed distance apart.

## Camera Hardware

This system uses two cameras connected via USB. Their resolution is 640px x 480px (claimed to be 1280x720) .
Purchased Here: https://www.amazon.com/Camera-HBV-W202012HD-Interface-Android-1280x720P/dp/B08MXVDY2B?crid=3Q1IAQ62IC93F&dib=eyJ2IjoiMSJ9.RgUYGGfxLjT6FQvWXXfSqbrqpfmlkBigr1Dyy3h5DQD44Y_1mnZ_ozgAiOioQKtAORxXrPG9HruZbJ5LDbQ5WFs7mtGiolylkHhPY-3FDK22GWPCwoEyCy-Dv2fvJt-k1V34qYDEdRdjTaqhBirfYIJJJRiPU5V262XC5mtd0V3Nc7Eu3TbV0iXBNMK_NPuxMiMJPNUmALe_9P9FQIM9rEzG_FlgNFogY_6JE3zmx6s.RahhUnVq3AR1SyRR3RkPe5LFk4WvWe_AVu1-jvbrhVI&dib_tag=se&keywords=miniature+camera+usb&qid=1732990694&sprefix=miniature+camera+usb%2Caps%2C107&sr=8-15

The FOV of the camera is 29.1 degrees.
This is found by holding an object in front of the camera until the object's edges are barely seen. If the object is held x distance away and the object is y distance across, FOV = 2 arctan (0.5 \* y / x).

The CAD Design folder contains the camera and 3D printed mount that is used for fixing the cameras. The foci of the cameras are 192.50mm apart.

## Software

The cameras will be differentiated as the left camera and the right camera. This is the left and right from the camera POV _not_ the object's POV.

### Stereoscopic Vision

#### Stereoscopic Vision Conceptually

#### Steroscopic Vision Math

##### Finding the Angle of a Point

With a camera, there is a point on it where we want to find the angle it makes line orthogonal to the camera's center line.

Since we know the camera's FOV (FOV), total horizontal pixels (N), and the x-coordinate of the point (x), we can find this angle (θ). The x-coordinate is the number of pixels from the left side of the camera.

xCenter = N / 2

θPerPixel = FOV / N

θFromCenter = (x - xCenter) \* θPerPixel

We want to form a triangle between the two cameras and the point, so we want the 2 interior angles along the cameras.

For the Left Camera:

θL = 90 + θFromCenter

For the Right Camera:

θR = 90 - θFromCenter

##### Finding the Distance of a Point

Using the triangle formed in the previous step between the two cameras and the point, we can find the distance of the point away from the cameras (d).

Since the cameras are separated at a known distance (s) and we have the two interior angles along that line, we will find d. This is the Angle-Side-Angle Thereom.

d = s / ((1 / tan(θL)) + (1 / tan(θR)))

##### Finding the Offset of an Point

Now that the orthogonal distance of a point is known, we can find the offset of a point from the center line. This is the distance between the point and the center line (orthogonally).

We can draw a triangle between these three sides:

1. Camera to the Point
2. Camera center line
3. Point to center line

We know the angle between the 2 and 3 is a right angle. We also know the angle between 1 and 2 (θFromCenter from an earlier step).
Using this we can find the length (offset) of 3 using the Angle-Side-Angle Thereom.

offset = d / ((1 / tan(θFromCenter)) + (1 / tan(90)))

##### Finding the Length of an Object

Now that the we know the perpendicular distance a point is from the camera and the offset a point is from the camera's centerline, we can find the length of an object.

If we create a right triangle with the length of the object as the hypotenuse, the lengths of the other sides have already been found. Point 2 is the left side of the object. Point 1 is the right side of the object

sideA = |offset2 - offset1|
sideB = |distance2 - distance1|
length = sqrt(sideA ^ 2 + side ^ 2)

### Computer Vision
