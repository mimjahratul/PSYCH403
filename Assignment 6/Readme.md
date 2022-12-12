# Assignment 6


## Dialoge box exc 
1. 
```
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':('male','female','other','prefer not to say'),
            'session': '1'}

print(exp_info)
```
2. 
```
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':('male','female','other','prefer not to say')}
```

### Using DlgFromDict:
1.
```
#Create the dialogue box
my_dlg = gui.DlgFromDict(exp_info, title='Subject info')
```

2. 
If I set the "session" variable as fixed in the "exp_info" dictionary, it means that the user will not be able to edit the value of this variable in the dialogue box. The default value that was specified in the dictionary will be used, 
and the user will not be able to change it.
```
my_dlg = gui.DlgFromDict(exp_info, title='Subject info', fixed=['session'])
```

3. 
```
#Create the exp_info dictionary with default values
exp_info = {
    'session': '1',
    'subject_nr': 0,
    'age': 0,
    'gender': '',
    'handedness': ('right','left','ambi')
}

#Create the dialogue box
my_dlg = gui.DlgFromDict(exp_info, title='Subject info', order=['session', 'subject_nr', 'age', 'gender', 'handedness'])
```
4. 
```
#Create the dialogue box
my_dlg = gui.DlgFromDict(exp_info, title='Subject info', order=['session', 'subject_nr', 'age', 'gender', 'handedness'])

#Print a message
print("All variables have been created! Now ready to show the dialog box!")

#Show the dialogue box and wait for the user to respond
if my_dlg.show():
    # Save the data
    exp_info_results = my_dlg.data
else:
    # Cancel was pressed
    exp_info_results = None
```    
5. 
```
#Import necessary modules 
from psychopy import gui, core
import datetime

#Create a dialogue box with the specified fields
exp_info = {'subject_nr':0, 
            'age':0, 
            'handedness':('right','left','ambi'), 
            'gender':('male','female','other','prefer not to say')
            }

info_dlg = gui.DlgFromDict(dictionary=info_dict, title='Participant Info')

#Get the current date and time
now = datetime.datetime.now()

#Create a unique filename based on the current date and time
filename = f"data_{now.strftime('%Y%m%d_%H%M%S')}.csv"
```

## Monitor and Window Exercise
1. 
The units parameter determines the units in which the size of the window is defined. If the units are set to "pix", the window size will be defined in pixels. If the units are set to "deg", the window size will be defined in degrees of visual angle. Changing the units will affect how the window size is defined, as the size will be interpreted differently depending on the units chosen. For example, if the units are set to "pix" and the window size is defined as (800, 600), the window will have a width of 800 pixels and a height of 600 pixels. However, if the units are set to "deg" and the window size is defined as (5, 5), the window will have a width and height of 5 degrees of visual angle. It is important to choose the appropriate units and define the window size accordingly in order to ensure that the window is displayed correctly.

2. 
Changing the color space in PsychoPy can affect how you define the color of your window.
Different color spaces represent colors in different ways.
When defining the color of your window, you can specify colors by name or by numeric values.
The specific method you use to define colors will depend on the color space you are using.

3.
```
#Import the modules
from psychopy import visual, core

#Define the monitor settings
monitor = visual.Monitor('MyMonitor')
monitor.setSizePix((1920, 1080))
monitor.setWidth(30)
monitor.setDistance(60)

#Create the window
window = visual.Window(
    size=(1920, 1080),
    color=(1, 1, 1),
    units='deg',
    fullscr=True,
    monitor=monitor
)
```

## Stimulus exercises
1.
This script will display the face images at 400x400 pixels in size. However, this will distort the aspect ratio of the images, making them appear stretched or squished.  To keep the proper image dimensions and still change the size, I can use the units parameter when creating the ImageStim object. For example, I could set the units parameter to 'pix' to specify that the size is in pixels, or I could set it to 'norm' to specify that the size is relative to the size of the window.
from psychopy import visual
```
#Create the window
win = visual.Window(size=(800, 600), color=(0, 0, 0))

#Load the images
image1 = visual.ImageStim(win, image='face1.png', size=(400, 400), units='pix')
image2 = visual.ImageStim(win, image='face2.png', size=(400, 400), units='pix')
image3 = visual.ImageStim(win, image='face3.png', size=(400, 400), units='pix')

#Display the images
image1.draw()
win.flip()

image2.draw()
win.flip()

image3.draw()
win.flip()

#Close the window
win.close()
```
2. 
```
from psychopy import visual

#Create the window
win = visual.Window(size=(800, 600), color=(0, 0, 0), fullscr=True)

#Calculate the window locations for each quadrant
half_width = win.size[0] / 2
half_height = win.size[1] / 2

quad1 = (-half_width, half_height)
quad2 = (half_width, half_height)
quad3 = (-half_width, -half_height)
quad4 = (half_width, -half_height)

#Load the images
image1 = visual.ImageStim(win, image='face1.png')
image2 = visual.ImageStim(win, image='face2.png')
image3 = visual.ImageStim(win, image='face3.png')
image4 = visual.ImageStim(win, image='face4.png')

#Set the locations of the images
face1.pos = quad1
face2.pos = quad2
face3.pos = quad3
face4.pos = quad4

#Display the images
face1.draw()
win.flip()

face2.draw()
win.flip()

face3.draw()
win.flip()

face4.draw()
win.flip()

#Close the window
win.close()
```

3. 
```
#Create the fixation cross stimulus
fixation_cross = visual.TextStim(win, text="+")
```

4. 
```
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================

# Define the window
from psychopy import visual
win = visual.Window(size=(800, 600), color=(0, 0, 0))

# Define the experiment start text
start_text = visual.TextStim(win, text='Experiment starting...')

# Define the block start/end text
block_text = visual.TextStim(win, text='Block starting/ending...')

# Define the stimuli
fixation_cross = visual.TextStim(win, text="+")
image1 = visual.ImageStim(win, image='face1.png')
image2 = visual.ImageStim(win, image='face2.png')

#=====================
#START EXPERIMENT
#=====================

# Present the start message text
start_text.draw()
win.flip()

# Wait for the participant to press a button to begin the experiment
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================

# Set the number of blocks
nBlocks = 10

# Loop through the blocks
for iBlock in range(nBlocks):
    # Present the block start message
    block_text.draw()
    win.flip()
    
    # Randomize the order of the trials
    trial_order = list(range(nTrials))
    random.shuffle(trial_order)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    

    # Set the number of trials
    nTrials = 10
    
    # Loop through the trials
    for iTrial in range(nTrials):
        # Set the stimuli and stimulus properties for the current trial
        curr_image = images[trial_order[iTrial]]
        curr_image.setPos((0, 0))
        curr_image.setSize((400, 400))
        
        #=====================
        #START TRIAL
        #=====================
        
        # Draw the fixation cross
        fixation_cross.draw()
        win.flip()
        
        # Wait for the stimulus duration
        core.wait(0.5)
        
        # Draw the image
        curr_image.draw()
        win.flip()
        
        # Wait for the stimulus duration
        core.wait(0.5)
        
        # Draw the end trial text
        end_trial_text.draw()
        win.flip()
        
        # Wait for the stimulus duration
        core.wait(0.5)

#======================
# END OF EXPERIMENT
#======================

# Close the window
win.close()
```
