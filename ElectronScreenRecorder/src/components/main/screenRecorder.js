"use strict"
/* 
 * state 
 * = inactive when screen is not being chosen
 * = ready when screen is rendered 
 * = recording when recording
 * = paused when screen recording is being paused
 * = stop when screen recording is stopped
 * = saving when file is being saved
 */

// const states = { 
//     INACTIVE: "inactive",
//     READY: "ready",
//     RECORDING: "recording",
//     PAUSED: "paused",
//     STOP: "stop",
//     SAVING: "saving"
// }
const {states} = require('../../constants/constants.js').CONSTANTS;
class ScreenRecorderState{
    state;
    startButton; 
    pauseButton; 
    stopButton; 
    saveButton; 
    deleteButton;

    constructor(videoSelectionButton, startButton, pauseButton, stopButton, saveButton, deleteButton){
        this.state = states.INACTIVE;
        this.videoSelectionButton = videoSelectionButton;
        this.startButton = startButton;
        this.pauseButton = pauseButton;
        this.stopButton = stopButton;
        this.saveButton = saveButton;
        this.deleteButton = deleteButton;
        this.initialiseScreenRecorder();
    }

    initialiseScreenRecorder(){
        this.videoSelectionButton.disabled = false;
        this.startButton.disabled = true;
        this.pauseButton.disabled = true;
        this.stopButton.disabled = true;
        this.saveButton.disabled = true;
        this.deleteButton.disabled = true;
    }

    readyScreen(){
        this.state = states.READY;
        this.startButton.disabled = false;
    }

    startRecording(){
        this.state = states.RECORDING;
        this.startButton.disabled = true;
        this.pauseButton.disabled = false;
        this.stopButton.disabled = false;
        this.videoSelectionButton.disabled = true;
    }

    pauseRecording(){
        this.state = states.PAUSED;
    }

    resumeRecording(){
        this.state = states.RECORDING;
    }

    stopRecording(){
        this.state = states.STOP;
        this.pauseButton.disabled = true;
        this.stopButton.disabled = true;
        this.saveButton.disabled = false;
        this.deleteButton.disabled = false;
    }
    
}

exports.ScreenRecorderState = ScreenRecorderState;