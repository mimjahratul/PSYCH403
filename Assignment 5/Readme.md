# Assignment 5

## Experiment Structure Exercises
```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
#-import psychopy functions
#-import file save functions
#-(import other functions as necessary: os...)
import numpy as np
from psychopy import core, gui, visual, event
import json
import os 

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
#-stimulus names (and stimulus extensions, if images) *
#-stimulus properties like size, orientation, location, duration *
#-start message text *
trial = 10
block = 2

names = ['faces']*10
extensions = ['im1.jpg','im2.jpg','im3.jpg','im4.jpg','im5.jpg','im6.jpg','im7.jpg','im8.jpg','im9.jpg','im10.jpg']

size = [200,200]
#orientation = [10]
location= [0,0]
duration = 1
startText = "Welcome to the experiment"
endText = "wait for next image"

#===================== 
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
pics = []
for ix in range(1,11):
    if ix <10: 
        pics.append('face' + '0' + str(ix) + '.jpg')
    else: 
        pics.append('face' + str(ix) + '.jpg')
#print(pics)

ims_in_dir = sorted(os.listdir(image_dir))
#print(ims_in_dir)

for img in pics: 
    if pics == ims_in_dir:
        print(str(img)+' was found!')
    else:
        raise Exception("The image lists do not match up!")

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
#-create an empty list for response time collection *
#-create an empty list for recording the order of stimulus identities *
#-create an empty list for recording the order of stimulus properties *
correct_response = []
user_response = []
accuracy = []
response_time = []
stim_id = []
stim_propt = []

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for blocks in range(block):
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(pics)
    #-reset response time clock here
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trials in range(trial):
        print('trial: ' + str(trials +1))
```
## Import Exercises
```
import numpy as np
from psychopy import core, gui, visual, event
import json
import os 
```

## Directory Exercises

### 1,2
```
#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
#-stimulus names (and stimulus extensions, if images) *
#-stimulus properties like size, orientation, location, duration *
#-start message text *
trial = 10
block = 2

names = ['faces']*10
extensions = ['im1.jpg','im2.jpg','im3.jpg','im4.jpg','im5.jpg','im6.jpg','im7.jpg','im8.jpg','im9.jpg','im10.jpg']

size = [200,200]
#orientation = [10]
location= [0,0]
duration = 1
startText = "Welcome to the experiment"
endText = "wait for next image"

#===================== 
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
pics = []
for ix in range(1,11):
    if ix <10: 
        pics.append('face' + '0' + str(ix) + '.jpg')
    else: 
        pics.append('face' + str(ix) + '.jpg')
#print(pics)

ims_in_dir = sorted(os.listdir(image_dir))
#print(ims_in_dir)

for img in pics: 
    if pics == ims_in_dir:
        print(str(img)+' was found!')
    else:
        raise Exception("The image lists do not match up!")
```
### 3 
```
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
#-define the directory where you will save your data
#-if you will be presenting images, define the image directory
#-check that these directories exist
os.getcwd()
main_dir = os.getcwd()

image_dir = os.path.join(main_dir,'images')
data_dir = os.path.join(main_dir,'data')

print(image_dir)
print(data_dir)

if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
    
#===================== 
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
pics = []
for ix in range(1,11):
    if ix <10: 
        pics.append('face' + '0' + str(ix) + '.jpg')
    else: 
        pics.append('face' + str(ix) + '.jpg')
#print(pics)

ims_in_dir = sorted(os.listdir(image_dir))
#print(ims_in_dir)

for img in pics: 
    if pics == ims_in_dir:
        print(str(img)+' was found!')
    else:
        raise Exception("The image lists do not match up!")
```
