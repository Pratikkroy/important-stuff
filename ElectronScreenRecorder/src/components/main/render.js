const {desktopCapturer, remote} = require('electron')
const {dialog, Menu} = remote;
const {writeFile} = require('fs');
const {ScreenRecorderState} = require('./screenRecorder.js');
const {states} = require('../../constants/constants.js').CONSTANTS;

window.onload = main

var videoElement = null;
var videoSelectionButton = null;
var startButton = null;
var pauseButton = null;
var stopButton = null;
var saveButton = null;
var deleteButton = null;
var mediaRecorder = null;
var recordedChunks = [];
var buffer = null;
var screenRecorderState = null;

function main(){
    videoElement = document.getElementsByTagName("video")[0];
    videoSelectionButton = document.getElementById("videoSelectionButton");
    startButton = document.getElementById("startButton");
    pauseButton = document.getElementById("pauseButton");
    stopButton = document.getElementById("stopButton");
    saveButton = document.getElementById("saveButton");
    deleteButton = document.getElementById("deleteButton");
    
    screenRecorderState = new ScreenRecorderState(videoSelectionButton, startButton, pauseButton, stopButton, saveButton, deleteButton);

    videoSelectionButton.onclick = getVideoSources;
    startButton.onclick = startButtonClick;
    pauseButton.onclick = pauseButtonClick;
    stopButton.onclick = stopButtonClick;
    saveButton.onclick = saveButtonClick;
    deleteButton.onclick = deleteButtonClick;
}

async function startButtonClick(){
    if(screenRecorderState.state == states.READY){
        mediaRecorder.start();
        startButton.classList.add("is-danger");
        startButton.innerText = "Recording";
        screenRecorderState.startRecording();
    }
}

async function pauseButtonClick(){
    if(screenRecorderState.state == states.RECORDING){
        mediaRecorder.pause();
        startButton.innerText = "Paused";
        pauseButton.innerText = "Resume";
        screenRecorderState.pauseRecording();
    }
    else if(screenRecorderState.state == states.PAUSED){
        mediaRecorder.resume();
        startButton.innerText = "Recording";
        pauseButton.innerText = "Pause";
        screenRecorderState.resumeRecording();
    }
}

async function stopButtonClick(){
    if(screenRecorderState.state == states.RECORDING || screenRecorderState.state == states.PAUSED){
        mediaRecorder.stop();
        startButton.classList.remove("is-danger");
        startButton.innerText = "Start";
        screenRecorderState.stopRecording();
    }
}

async function saveButtonClick(){
    if(screenRecorderState.state == states.STOP){
        if(buffer != null){
            const {filepath} = await dialog.showSaveDialog({
                buttonLabel: " Save video",
                defaultPath: `vid-${Date.now().webm}`
            });
            
            if(filepath === undefined){
                console.log("Saving video cancelled");
                return;
            }
            console.log("Writing to ...... ",filepath);
        
            writeFile(filepath, buffer, () => console.log(" Video saved successfully"));
        }
        else{
            console.log("Cannot save video. Buffer is null")
        }   
    }
}

async function deleteButtonClick(){
    // location.reload();
    reset();
    videoElement.srcObject = null;
    main();
}

function reset(){
    mediaRecorder = null;
    recordedChunks = [];
    buffer = null;
}

async function getVideoSources(){

    // list all the available video sources
    const inputSources = await desktopCapturer.getSources({
        types: ["window", "screen"]
    });

    const videoOptionsMenu = Menu.buildFromTemplate(
        inputSources.map(source => {
            return {
                label: source.name,
                click: () => selectSource(source)
            };
        })
    );

    videoOptionsMenu.popup();
    
}

async function selectSource(source) {
    
    videoSelectionButton.innerText = source.name;
    screenRecorderState.readyScreen();

    const constraints = {
        audio: false,
        video: {
            mandatory: {
                chromeMediaSource: "desktop",
                chromeMediaSourceId: source.id
            }
        }
    };

    // create a stream
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    videoElement.srcObject = stream;
    videoElement.play();

    // create the media recorder
    const options = {mimeType: "video/webm; codecs=vp9"};
    mediaRecorder = new MediaRecorder(stream, options);

    
    // register event handlers
    mediaRecorder.ondataavailable = handleDataAvailable;
    mediaRecorder.onstop = handleStop;


}

function handleDataAvailable(event){
    console.log("video data available");
    recordedChunks.push(event.data);
}

async function handleStop(event){
    const blob = new Blob(recordedChunks, {
        type: "video/webm; codecsvp9"
    });

    buffer = Buffer.from(await blob.arrayBuffer());
}




