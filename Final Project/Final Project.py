# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:01:30 2022

@author: mimja
"""
#Final 403 Project by Jahratul Mim 
#This is a reaction based memory task that can be used to study the speed and retrieval of memory processes
#It uses the psychopy module to create the visual stimuli, collect user input, and measure reaction times. It also uses the csv module to save the datas to CSV files, and the os module to handle file paths.
#The stimuli: words are presented in a random order to the user for 0.5 seconds 
#The participant then has to type out as many words as they can remember

#IMPORT MODULES
from psychopy import visual, monitors, core, event, gui
import random
import csv
import os

#PATH SETTINGS
path = os.path.join(os.getcwd(), 'memory_data.csv') # get current working directory

#COLLECT PARTICIPANT INFO 
info = {"ID": "", "Age": "", "Gender": ["Male", "Female", "Other"]} # create dictionary to store participant information
infoDlg = gui.DlgFromDict(info, title="Participant Info")

#STIMULUS AND TRIAL SETTINGS
stimuli = ['apple', 'banana', 'car', 'dog', 'elephant', 'flower'] # create list of stimuli
nTrials = 3 # number of trials in the experiment

#PREPARE CONDITION LISTS
random.shuffle(stimuli) # shuffle stimuli


#PREPARE DATA COLLECTION LISTS
data = [] # create empty list to store trial data
reaction_times = [] # create an empty list to store reaction times

#CREATION OF WINDOW AND STIMULI
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(
    fullscr=False, 
    monitor=mon, 
    size=(600,600), 
    color='grey', 
    units='pix'
) # create window to display stimuli

#START EXPERIMENT
# Display instructions to the participant
instructions = visual.TextStim(win, text='In this experiment, you will be shown a list of words. Please remember as many words as you can. Press any key to start the experiment.')
instructions.draw()
win.flip()
event.waitKeys()

clock = core.Clock()

for trial in range(nTrials): # start experiment
    for stimulus in stimuli:
        visual.TextStim(win, text=stimulus).draw()
        win.flip()
        core.wait(0.5) # display each stimulus for half a second
        #clock.reset() # reset the clock
        #event.waitKeys() # wait for the participant to respond
        reaction_time = clock.getTime() # get the elapsed time
        reaction_times.append(reaction_time) # add the reaction time to the list

    # Ask user to enter the stimuli they remember from the list
    response = input('Please enter the stimuli you remember from the list, separated by commas: ')

    # Save trial data
    data.append([info['ID'], info['Age'], info['Gender'], response])

#SAVE DATA TO A CSV FILE
with open('memory_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',') # specify the delimiter as a comma
    writer.writerow(["ID", "Age", "Gender", "Response", "Reaction Time"])
    writer.writerows(data)
    
#SAVE REACTION TIMES TO A CSV FILE
with open('reaction_times.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["ID", "Age", "Gender", "Trial"]) # write the header row
    for i in range(len(reaction_times)):
        id = info['ID']
        age = info['Age']
        gender = info['Gender']
        trial = i+1 # trial number, starting from 1
        rt = reaction_times[i] # reaction time for the trial
        writer.writerow([id, age, gender, trial, rt]) # write the data row

    
#END OF EXPERIMENT
win.close()
