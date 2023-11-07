#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on October 30, 2023, at 09:00
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
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
    originPath='U:\\Desktop\\cpsc6120\\project\\exp\\project_no_ET_lastrun.py',
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
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='Laptop', color=[0,0,0], colorSpace='rgb',
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

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='Change Blindness', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

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
    
    trialDuration = 10
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
