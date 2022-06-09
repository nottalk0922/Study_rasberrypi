import cv2

def main():
    camera = cv2.VideoCapture(-1)
    camera.set(3,640)
    camera.set(4,480)

    while(camera.isOpened() ):
        _, image = camera.read()
        image = cv2.flip(image,0)
        cv2.imshow(' camera test',image)

        if cv2.waitKey(1) == ord('q'):
            break
    camera.release()
    cv2.destoryAllWindows()

if __name__ == '__main__':
        main()
