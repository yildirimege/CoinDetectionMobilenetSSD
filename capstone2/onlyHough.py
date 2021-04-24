import cv2
import numpy as np
import os
coins = os.listdir("Frames")

def detect_coins(coins_list):

    for coins_img in coins_list:
        coins = cv2.imread(f"Frames/{coins_img}")
        gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(gray, 11)
        circles = cv2.HoughCircles(
            img,  # source image
            cv2.HOUGH_GRADIENT,  # type of detection
            1,
            50,
            param1=100,
            param2=50,
            minRadius=10,  # minimal radius
            maxRadius=380,  # max radius
        )

        coins_copy = coins.copy()


        for detected_circle in circles[0]:
            x_coor, y_coor, detected_radius = detected_circle
            coins_detected = cv2.circle(
                coins_copy,
                (int(x_coor), int(y_coor)),
                int(detected_radius),
                (0, 255, 0),
                4,
            )
        coins_detected = cv2.resize(coins_detected, (360,640))
        cv2.imshow("detected", coins_detected)
        cv2.waitKey(0)

        #return circles


if __name__ == '__main__':
    detect_coins(coins)