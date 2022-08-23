from tkinter import image_names
import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    #intializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image in storagedevice
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time()
        result = False
    return image_name
    print("snapshot taken")

    #release the camera
    videoCaptureObject.release()

    #close all windows
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token = 'sl.BN6n6uM0vlubbE7VNepMGz2OvCut0N4hRf0xVMlvWR3Cij2iSyIpfcPYOPE-I2Wj1jDj-XeS3mC97xKK4RW5HierWbIGrc6j1h4csj9xMBa2f118ud0WKKFQ3D_I6ulfOAA2VLI'
    file = image_name
    file_from = file
    file_to = "/newFolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 3):
            name = take_snapshot()
            upload_file(name)

main()