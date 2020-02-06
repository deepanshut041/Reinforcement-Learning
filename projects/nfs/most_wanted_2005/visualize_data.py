import numpy as np
import cv2

'''
Use this script to visualize the data captured along with the label.
'''

d = input('Enter the filename: ')  # along with '.npy' extension
train_data = np.load(d, allow_pickle=True)

for data in train_data:
    img = data[0]
    choice = data[1]

    cv2.imshow('test', img)
    print(choice)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break