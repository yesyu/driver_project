#_*_encoding:utf-8_*_

import json
import os

dirpath='/data/yff/project/openpose/examples/media_out/eat_something/no_hand/json/'

# get all json files;
def get_files(path):
    files_path=[]
    for root,dirs,files in os.walk(path):
        for filename in files:
            filepath = os.sep.join([root, filename])
            files_path.append(filepath)
            # print filepath
    return files_path
# path=get_files(dirpath)
# print path
fileObject = open('sampleList.txt', 'w')
def write_files(path):
    files_path=get_files(path)
    for iterm in files_path:
        # print iterm
        # print type(iterm)
        with open(iterm,'r') as f:
            data=json.load(f)
            print data
            index_11=data['people'][0]['pose_keypoints'][0:33]
            index_15=data['people'][0]['pose_keypoints'][42:]
            save_file=index_11+index_15
            for item in save_file:
                # print item
                fileObject.write(str(item)+' ')
        fileObject.write('\n')
write_files(dirpath)
