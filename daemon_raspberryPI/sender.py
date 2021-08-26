# importing the modules
import requests
import json
import cv2

def post_picture():

    # Opening JSON file
    with open('cfg/cfg.json','r') as json_file:
        data = json.load(json_file)

        secret=data['secret']
        url=data['url']
        id_house=data['id_house']
        time_frequency=data['time_frequency']

        cameras_info=data['cams']

        for cam_info in cameras_info:
            id_cam = cam_info['id_cam']
            type = cam_info['type']
            path_cam = cam_info['path_cam']

            cap= cv2.VideoCapture(path_cam)

            frame= cap.imread()

            cap.release()
        
        cv2.releaseAllWindows()

        
post_picture()

#url = 'http://localhost:5000'
#files = {'image': open('test.jpg', 'rb')}
#requests.post(url, files=files)