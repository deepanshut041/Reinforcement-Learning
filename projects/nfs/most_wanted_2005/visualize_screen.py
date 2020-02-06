import cv2
from grabscreen import grab_screen

'''
This script allows you to visualize the screen getting captured by cv2.
The region shown by this script is the input data for the CNN.
Make sure that your game window is seen by cv2.
'''

while True:
    # change the region=(x, y, width, height) according to your game window.
    screen = grab_screen(region=(264, 269, 565, 500))

    # uncomment the next line to see the resized image to be inputed.
    # screen = cv2.resize(screen, (86, 56))
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY))

    if cv2.waitKey(25) == ord('q'):
        cv2.destroyAllWindows()
        break