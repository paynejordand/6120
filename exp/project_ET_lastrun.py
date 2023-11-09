﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on October 30, 2023, at 13:29
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'Change Blindness'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'task': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='U:\\Desktop\\cpsc6120\\project\\exp\\project_ET_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='LabMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='pix')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.gazepoint.gp3.EyeTracker'] = {
    'name': 'tracker',
    'network_settings': {
        'ip_address': '127.0.0.1',
        'port': 4242.0
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='Change Blindness', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "calib_instr" ---
calib_instr_text = visual.TextStim(win=win, name='calib_instr_text',
    text="We must first calibrate the eye tracker.\n\nKeep your eye on the calibration dot but don't anticipate its movement.\n\nPress space to continue.",
    font='Open Sans',
    pos=(0, 0), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
calib_instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "calib_cont" ---
# Run 'Begin Experiment' code from calib_code
calib_timeout = 10
ave_error = 0
valib_calib_points = 0
calib_text = visual.TextStim(win=win, name='calib_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
calib_resp = keyboard.Keyboard()

# --- Initialize components for Routine "trial_instr" ---
trail_instr_text = visual.TextStim(win=win, name='trail_instr_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
trial_instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "image_flicker" ---
visual_task = visual.TextBox2(
     win, text='Any text\n\nincluding line breaks', placeholder='Type here...', font='Arial',
     pos=(130, -450),units='pix',     letterHeight=18.0,
     size=(550,200), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=10.0, alignment='center-left',
     anchor='center', overflow='visible',
     fillColor=[-0.0667, 0.0667, 0.2000], borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='visual_task',
     depth=0, autoLog=True,
)
# Run 'Begin Experiment' code from trial_code
timeout = False
interrupt = False
original = visual.ImageStim(
    win=win,
    name='original', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
blank = visual.ImageStim(
    win=win,
    name='blank', 
    image='stimuli/1920x1080/gray_box.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
altered = visual.ImageStim(
    win=win,
    name='altered', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
key_resp_interrupt = keyboard.Keyboard()

# --- Initialize components for Routine "task_confidence" ---
confidence_slider = visual.Slider(win=win, name='confidence_slider',
    startValue=None, size=None, pos=(0,0), units='pix',
    labels=['not confident at all', 'slightly confident', 'somewhat confident', 'fairly confident', 'completely confident'], ticks=[1, 2, 3, 4, 5], granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=20.0,
    flip=False, ori=0.0, depth=-1, readOnly=False)
key_resp_confidence = keyboard.Keyboard()
confidence_text = visual.TextStim(win=win, name='confidence_text',
    text='Any text\n\nincluding line breaks',
    font='Open Sans',
    pos=(0, 200), height=20.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "task_questions" ---
task_question_text = visual.TextBox2(
     win, text='Any text\n\nincluding line breaks', placeholder='Type here...', font='Arial',
     pos=(0, 0),     letterHeight=30.0,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='task_question_text',
     depth=0, autoLog=True,
)
key_resp_questions = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "calib_instr" ---
continueRoutine = True
# update component parameters for each repeat
calib_instr_resp.keys = []
calib_instr_resp.rt = []
_calib_instr_resp_allKeys = []
# keep track of which components have finished
calib_instrComponents = [calib_instr_text, calib_instr_resp]
for thisComponent in calib_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "calib_instr" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *calib_instr_text* updates
    
    # if calib_instr_text is starting this frame...
    if calib_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calib_instr_text.frameNStart = frameN  # exact frame index
        calib_instr_text.tStart = t  # local t and not account for scr refresh
        calib_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calib_instr_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'calib_instr_text.started')
        # update status
        calib_instr_text.status = STARTED
        calib_instr_text.setAutoDraw(True)
    
    # if calib_instr_text is active this frame...
    if calib_instr_text.status == STARTED:
        # update params
        pass
    
    # *calib_instr_resp* updates
    waitOnFlip = False
    
    # if calib_instr_resp is starting this frame...
    if calib_instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calib_instr_resp.frameNStart = frameN  # exact frame index
        calib_instr_resp.tStart = t  # local t and not account for scr refresh
        calib_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calib_instr_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'calib_instr_resp.started')
        # update status
        calib_instr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(calib_instr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(calib_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if calib_instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = calib_instr_resp.getKeys(keyList=['space'], waitRelease=False)
        _calib_instr_resp_allKeys.extend(theseKeys)
        if len(_calib_instr_resp_allKeys):
            calib_instr_resp.keys = _calib_instr_resp_allKeys[-1].name  # just the last key pressed
            calib_instr_resp.rt = _calib_instr_resp_allKeys[-1].rt
            calib_instr_resp.duration = _calib_instr_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calib_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "calib_instr" ---
for thisComponent in calib_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if calib_instr_resp.keys in ['', [], None]:  # No response was made
    calib_instr_resp.keys = None
thisExp.addData('calib_instr_resp.keys',calib_instr_resp.keys)
if calib_instr_resp.keys != None:  # we had a response
    thisExp.addData('calib_instr_resp.rt', calib_instr_resp.rt)
    thisExp.addData('calib_instr_resp.duration', calib_instr_resp.duration)
thisExp.nextEntry()
# the Routine "calib_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
calib_loop = data.TrialHandler(nReps=calib_timeout, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='calib_loop')
thisExp.addLoop(calib_loop)  # add the loop to the experiment
thisCalib_loop = calib_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCalib_loop.rgb)
if thisCalib_loop != None:
    for paramName in thisCalib_loop:
        exec('{} = thisCalib_loop[paramName]'.format(paramName))

for thisCalib_loop in calib_loop:
    currentLoop = calib_loop
    # abbreviate parameter names if possible (e.g. rgb = thisCalib_loop.rgb)
    if thisCalib_loop != None:
        for paramName in thisCalib_loop:
            exec('{} = thisCalib_loop[paramName]'.format(paramName))
    # define target for calibration
    calibrationTarget = visual.TargetStim(win, 
        name='calibrationTarget',
        radius=10.0, fillColor='', borderColor='black', lineWidth=2.0,
        innerRadius=3.5, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
        colorSpace='rgb', units=None
    )
    # define parameters for calibration
    calibration = hardware.eyetracker.EyetrackerCalibration(win, 
        eyetracker, calibrationTarget,
        units=None, colorSpace='rgb',
        progressMode='time', targetDur=1.5, expandScale=1.5,
        targetLayout='FIVE_POINTS', randomisePos=True, textColor='white',
        movementAnimation=True, targetDelay=1.0
    )
    # run calibration
    calibration.run()
    # clear any keypresses from during calibration so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # define target for validation
    validationTarget = visual.TargetStim(win, 
        name='validationTarget',
        radius=10.0, fillColor='', borderColor='black', lineWidth=2.0,
        innerRadius=3.5, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
        colorSpace='rgb', units=None
    )
    # define parameters for validation
    validation = iohub.ValidationProcedure(win,
        target=validationTarget,
        gaze_cursor='green', 
        positions='FIVE_POINTS', randomize_positions=True,
        expand_scale=1.5, target_duration=1.5,
        enable_position_animation=True, target_delay=1.0,
        progress_on_key=None, text_color='auto',
        show_results_screen=True, save_results_screen=False,
        color_space='rgb', unit_type=None
    )
    # run validation
    validation.run()
    # clear any keypresses from during validation so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "validation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "calib_cont" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from calib_code
    ave_error = calibration.last['SUMMARY']['AVE_ERROR']
    valid_calib_points = calibration.last['SUMMARY']['VALID_POINTS']
    
    calib_query = f'Average error is: {ave_error}\n\nValid Points: {valid_calib_points}\n\nRecalibrate? (y/n)'
    calib_text.setText(calib_query)
    calib_resp.keys = []
    calib_resp.rt = []
    _calib_resp_allKeys = []
    # keep track of which components have finished
    calib_contComponents = [calib_text, calib_resp]
    for thisComponent in calib_contComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "calib_cont" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *calib_text* updates
        
        # if calib_text is starting this frame...
        if calib_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            calib_text.frameNStart = frameN  # exact frame index
            calib_text.tStart = t  # local t and not account for scr refresh
            calib_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calib_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calib_text.started')
            # update status
            calib_text.status = STARTED
            calib_text.setAutoDraw(True)
        
        # if calib_text is active this frame...
        if calib_text.status == STARTED:
            # update params
            pass
        
        # *calib_resp* updates
        waitOnFlip = False
        
        # if calib_resp is starting this frame...
        if calib_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            calib_resp.frameNStart = frameN  # exact frame index
            calib_resp.tStart = t  # local t and not account for scr refresh
            calib_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calib_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calib_resp.started')
            # update status
            calib_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(calib_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(calib_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if calib_resp.status == STARTED and not waitOnFlip:
            theseKeys = calib_resp.getKeys(keyList=['y','n'], waitRelease=False)
            _calib_resp_allKeys.extend(theseKeys)
            if len(_calib_resp_allKeys):
                calib_resp.keys = _calib_resp_allKeys[-1].name  # just the last key pressed
                calib_resp.rt = _calib_resp_allKeys[-1].rt
                calib_resp.duration = _calib_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in calib_contComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "calib_cont" ---
    for thisComponent in calib_contComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from calib_code
    if calib_resp is not None and 'n' in calib_resp.keys:
        calib_loop.finished = True
    # check responses
    if calib_resp.keys in ['', [], None]:  # No response was made
        calib_resp.keys = None
    calib_loop.addData('calib_resp.keys',calib_resp.keys)
    if calib_resp.keys != None:  # we had a response
        calib_loop.addData('calib_resp.rt', calib_resp.rt)
        calib_loop.addData('calib_resp.duration', calib_resp.duration)
    # the Routine "calib_cont" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed calib_timeout repeats of 'calib_loop'


# --- Prepare to start Routine "trial_instr" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from trial_instr_code
trial_instructions = 'You are going to be shown a series of flashing images.\n\n Scan the image as if you were driving in that scenario. If you notice something change press space.\n\n'

if int(expInfo['task']) == 1:
    trial_instructions += 'Read the passage at the bottom of the image as you scan the image. You will be asked three questions about the passage.\n\n'
elif int(expInfo['task']) == 2:
    trial_instructions += 'Listen to the passage being read to you as you can the image. You will be asked three questions about the passage.\n\n'

trial_instructions += 'Press space when you are ready to begin'
trail_instr_text.setText(trial_instructions)
trial_instr_resp.keys = []
trial_instr_resp.rt = []
_trial_instr_resp_allKeys = []
# keep track of which components have finished
trial_instrComponents = [trail_instr_text, trial_instr_resp]
for thisComponent in trial_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial_instr" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trail_instr_text* updates
    
    # if trail_instr_text is starting this frame...
    if trail_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trail_instr_text.frameNStart = frameN  # exact frame index
        trail_instr_text.tStart = t  # local t and not account for scr refresh
        trail_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trail_instr_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trail_instr_text.started')
        # update status
        trail_instr_text.status = STARTED
        trail_instr_text.setAutoDraw(True)
    
    # if trail_instr_text is active this frame...
    if trail_instr_text.status == STARTED:
        # update params
        pass
    
    # *trial_instr_resp* updates
    waitOnFlip = False
    
    # if trial_instr_resp is starting this frame...
    if trial_instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trial_instr_resp.frameNStart = frameN  # exact frame index
        trial_instr_resp.tStart = t  # local t and not account for scr refresh
        trial_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_instr_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_instr_resp.started')
        # update status
        trial_instr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trial_instr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trial_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trial_instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = trial_instr_resp.getKeys(keyList=['space'], waitRelease=False)
        _trial_instr_resp_allKeys.extend(theseKeys)
        if len(_trial_instr_resp_allKeys):
            trial_instr_resp.keys = _trial_instr_resp_allKeys[-1].name  # just the last key pressed
            trial_instr_resp.rt = _trial_instr_resp_allKeys[-1].rt
            trial_instr_resp.duration = _trial_instr_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial_instr" ---
for thisComponent in trial_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trial_instr_resp.keys in ['', [], None]:  # No response was made
    trial_instr_resp.keys = None
thisExp.addData('trial_instr_resp.keys',trial_instr_resp.keys)
if trial_instr_resp.keys != None:  # we had a response
    thisExp.addData('trial_instr_resp.rt', trial_instr_resp.rt)
    thisExp.addData('trial_instr_resp.duration', trial_instr_resp.duration)
thisExp.nextEntry()
# the Routine "trial_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim.csv'),
    seed=int(expInfo['participant']), name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "image_flicker" ---
    continueRoutine = True
    # update component parameters for each repeat
    visual_task.reset()
    # Run 'Begin Routine' code from trial_code
    timeout = False
    interrupt = False
    
    trialDuration = 45
    blankDurationF = 15 # ~0.25 seconds
    imageDurationF = 30 # ~0.5 seconds
    
    originalIsActive = True
    isBlanked = False
    
    activeImage = original
    
    visualTask = False
    audioTask = False
    task = int(expInfo['task'])
    if task == 1:
        visualTask = True
        visual_task.text = thisTrial['trial_visual']
        with open(thisTrial['trial_visual']) as f:
            visual_task.text = f.read().split('$$$')[0].strip()
    elif task == 2:
        audioTask = True
    
    imgs = thisTrial['trial_img'].split('$')
    original.image = imgs[0].strip()
    altered.image = imgs[1].strip()
    key_resp_interrupt.keys = []
    key_resp_interrupt.rt = []
    _key_resp_interrupt_allKeys = []
    # keep track of which components have finished
    image_flickerComponents = [visual_task, original, blank, altered, key_resp_interrupt]
    for thisComponent in image_flickerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "image_flicker" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *visual_task* updates
        
        # if visual_task is active this frame...
        if visual_task.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from trial_code
        # Timeout to end routine
        if t >= trialDuration:
            continueRoutine = False
            timeout = True
            continue
        
        # Add code for keyboard interrupt to end routine
        # continueRoutine = False
        # interrupt = True
        
        if frameN == 0:
            blank.tFlip = t
            blank.frameNFlip = frameN
            blank.tFlipRefresh = tThisFlipGlobal
            win.timeOnFlip(blank, 'tFlipRefresh')
            thisExp.timestampOnFlip(win, f'blank.paused')
            # image
            activeImage.frameNStart = frameN
            activeImage.tStart = t
            activeImage.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(activeImage, 'tStartRefresh')
            thisExp.timestampOnFlip(win, f'{activeImage.name}.started')
            activeImage.status = STARTED
            activeImage.draw()
            
            # task
            if visualTask:
                # keep track of start time/frame for later
                visual_task.frameNStart = frameN  # exact frame index
                visual_task.tStart = t  # local t and not account for scr refresh
                visual_task.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(visual_task, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'visual_task.started')
                # update status
                visual_task.status = STARTED
                visual_task.setAutoDraw(True)
            elif audioTask:
                pass
            continue
        
        
        # Image handling
        # should happen every 0.5 seconds (30 frames)
        #if tThisFlipGlobal >= activeImage.tStartRefresh + imageDuration-frameTolerance:
        if frameN >= activeImage.frameNStart + imageDurationF:
            activeImage.tStop = t
            activeImage.frameNStop = frameN
            thisExp.timestampOnFlip(win, f'{activeImage.name}.paused')
            activeImage.status = PAUSED
            if originalIsActive:
                original = activeImage
                activeImage = altered
            else:
                altered = activeImage
                activeImage = original
            originalIsActive = not originalIsActive
            activeImage.frameNStart = frameN
            activeImage.tStart = t
            activeImage.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(activeImage, 'tStartRefresh')
            thisExp.timestampOnFlip(win, f'{activeImage.name}.started')
            activeImage.status = STARTED
        
        # Blank handling
        # should happen every 0.25 seconds (15 frames)
        #if tThisFlipGlobal >= blank.tFlipRefresh + blankDuration - frameTolerance:
        if frameN >= blank.frameNFlip + blankDurationF:
            blank.tFlip = t
            blank.frameNFlip = frameN
            blank.tFlipRefresh = tThisFlipGlobal
            blank.status = PAUSED if isBlanked else STARTED
            status = 'paused' if isBlanked else 'started'
            win.timeOnFlip(blank, 'tFlipRefresh')
            thisExp.timestampOnFlip(win, f'blank.{status}')
                
            isBlanked = not isBlanked
        
        activeImage.draw()
        if isBlanked:
            blank.draw()
        
        # *original* updates
        
        # if original is active this frame...
        if original.status == STARTED:
            # update params
            pass
        
        # *blank* updates
        
        # if blank is active this frame...
        if blank.status == STARTED:
            # update params
            pass
        
        # *altered* updates
        
        # if altered is active this frame...
        if altered.status == STARTED:
            # update params
            pass
        
        # *key_resp_interrupt* updates
        waitOnFlip = False
        
        # if key_resp_interrupt is starting this frame...
        if key_resp_interrupt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_interrupt.frameNStart = frameN  # exact frame index
            key_resp_interrupt.tStart = t  # local t and not account for scr refresh
            key_resp_interrupt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_interrupt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_interrupt.started')
            # update status
            key_resp_interrupt.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_interrupt.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_interrupt.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_interrupt.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_interrupt.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_interrupt_allKeys.extend(theseKeys)
            if len(_key_resp_interrupt_allKeys):
                key_resp_interrupt.keys = _key_resp_interrupt_allKeys[-1].name  # just the last key pressed
                key_resp_interrupt.rt = _key_resp_interrupt_allKeys[-1].rt
                key_resp_interrupt.duration = _key_resp_interrupt_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in image_flickerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "image_flicker" ---
    for thisComponent in image_flickerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_interrupt.keys in ['', [], None]:  # No response was made
        key_resp_interrupt.keys = None
    trials.addData('key_resp_interrupt.keys',key_resp_interrupt.keys)
    if key_resp_interrupt.keys != None:  # we had a response
        trials.addData('key_resp_interrupt.rt', key_resp_interrupt.rt)
        trials.addData('key_resp_interrupt.duration', key_resp_interrupt.duration)
    # the Routine "image_flicker" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "task_confidence" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from confidence_code
    if timeout:
        confidence_text.text = f'How confident are you that there was no change in the scene?'
    else:
        confidence_text.text = 'How confident are you that there was a change in the scene?'
    
    confidence_text.text = confidence_text.text + ' \nClick on the line and then press Space or Enter to confirm.'
    confidence_slider.reset()
    key_resp_confidence.keys = []
    key_resp_confidence.rt = []
    _key_resp_confidence_allKeys = []
    # keep track of which components have finished
    task_confidenceComponents = [confidence_slider, key_resp_confidence, confidence_text]
    for thisComponent in task_confidenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "task_confidence" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *confidence_slider* updates
        
        # if confidence_slider is starting this frame...
        if confidence_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confidence_slider.frameNStart = frameN  # exact frame index
            confidence_slider.tStart = t  # local t and not account for scr refresh
            confidence_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidence_slider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confidence_slider.started')
            # update status
            confidence_slider.status = STARTED
            confidence_slider.setAutoDraw(True)
        
        # if confidence_slider is active this frame...
        if confidence_slider.status == STARTED:
            # update params
            pass
        
        # *key_resp_confidence* updates
        waitOnFlip = False
        
        # if key_resp_confidence is starting this frame...
        if key_resp_confidence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_confidence.frameNStart = frameN  # exact frame index
            key_resp_confidence.tStart = t  # local t and not account for scr refresh
            key_resp_confidence.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_confidence, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_confidence.started')
            # update status
            key_resp_confidence.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_confidence.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_confidence.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_confidence.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_confidence.getKeys(keyList=['enter','space'], waitRelease=False)
            _key_resp_confidence_allKeys.extend(theseKeys)
            if len(_key_resp_confidence_allKeys):
                key_resp_confidence.keys = _key_resp_confidence_allKeys[-1].name  # just the last key pressed
                key_resp_confidence.rt = _key_resp_confidence_allKeys[-1].rt
                key_resp_confidence.duration = _key_resp_confidence_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *confidence_text* updates
        
        # if confidence_text is starting this frame...
        if confidence_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confidence_text.frameNStart = frameN  # exact frame index
            confidence_text.tStart = t  # local t and not account for scr refresh
            confidence_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidence_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confidence_text.started')
            # update status
            confidence_text.status = STARTED
            confidence_text.setAutoDraw(True)
        
        # if confidence_text is active this frame...
        if confidence_text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in task_confidenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "task_confidence" ---
    for thisComponent in task_confidenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('confidence_slider.response', confidence_slider.getRating())
    trials.addData('confidence_slider.rt', confidence_slider.getRT())
    # check responses
    if key_resp_confidence.keys in ['', [], None]:  # No response was made
        key_resp_confidence.keys = None
    trials.addData('key_resp_confidence.keys',key_resp_confidence.keys)
    if key_resp_confidence.keys != None:  # we had a response
        trials.addData('key_resp_confidence.rt', key_resp_confidence.rt)
        trials.addData('key_resp_confidence.duration', key_resp_confidence.duration)
    # the Routine "task_confidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    questions = data.TrialHandler(nReps=3.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='questions')
    thisExp.addLoop(questions)  # add the loop to the experiment
    thisQuestion = questions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
    if thisQuestion != None:
        for paramName in thisQuestion:
            exec('{} = thisQuestion[paramName]'.format(paramName))
    
    for thisQuestion in questions:
        currentLoop = questions
        # abbreviate parameter names if possible (e.g. rgb = thisQuestion.rgb)
        if thisQuestion != None:
            for paramName in thisQuestion:
                exec('{} = thisQuestion[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "task_questions" ---
        continueRoutine = True
        # update component parameters for each repeat
        task_question_text.reset()
        # Run 'Begin Routine' code from questions_code
        if int(expInfo['task']) == 0:
            break
        with open(thisTrial['trial_visual']) as f:
            task_question_text.text = f.read().split('$$$')[1 + questions.thisN]
        key_resp_questions.keys = []
        key_resp_questions.rt = []
        _key_resp_questions_allKeys = []
        # keep track of which components have finished
        task_questionsComponents = [task_question_text, key_resp_questions]
        for thisComponent in task_questionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "task_questions" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *task_question_text* updates
            
            # if task_question_text is starting this frame...
            if task_question_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                task_question_text.frameNStart = frameN  # exact frame index
                task_question_text.tStart = t  # local t and not account for scr refresh
                task_question_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(task_question_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'task_question_text.started')
                # update status
                task_question_text.status = STARTED
                task_question_text.setAutoDraw(True)
            
            # if task_question_text is active this frame...
            if task_question_text.status == STARTED:
                # update params
                pass
            
            # *key_resp_questions* updates
            waitOnFlip = False
            
            # if key_resp_questions is starting this frame...
            if key_resp_questions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_questions.frameNStart = frameN  # exact frame index
                key_resp_questions.tStart = t  # local t and not account for scr refresh
                key_resp_questions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_questions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_questions.started')
                # update status
                key_resp_questions.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_questions.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_questions.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_questions.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_questions.getKeys(keyList=['a','b','c','d'], waitRelease=False)
                _key_resp_questions_allKeys.extend(theseKeys)
                if len(_key_resp_questions_allKeys):
                    key_resp_questions.keys = _key_resp_questions_allKeys[-1].name  # just the last key pressed
                    key_resp_questions.rt = _key_resp_questions_allKeys[-1].rt
                    key_resp_questions.duration = _key_resp_questions_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in task_questionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "task_questions" ---
        for thisComponent in task_questionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_questions.keys in ['', [], None]:  # No response was made
            key_resp_questions.keys = None
        questions.addData('key_resp_questions.keys',key_resp_questions.keys)
        if key_resp_questions.keys != None:  # we had a response
            questions.addData('key_resp_questions.rt', key_resp_questions.rt)
            questions.addData('key_resp_questions.duration', key_resp_questions.duration)
        # the Routine "task_questions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 3.0 repeats of 'questions'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()