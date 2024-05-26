// Make sure to install the necessary dependencies
const { CallClient, VideoStreamRenderer, LocalVideoStream } = require('@azure/communication-calling');
const { AzureCommunicationTokenCredential } = require('@azure/communication-common');
const { AzureLogger, setLogLevel } = require("@azure/logger");
// Set the log level and output
setLogLevel('verbose');
AzureLogger.log = (...args) => {
    console.log(...args);
};
var ringtone = document.getElementById('ringtone');
let isUserInteracted = false;

document.body.addEventListener('click', () => {
    isUserInteracted = true;
});
// Calling web sdk objects
let callAgent;
let deviceManager;
let call;
let incomingCall;
let localVideoStream;
let localVideoStreamRenderer;
let isVideoOn = true;
let isMicroOn = true;
// UI widgets
let userAccessToken = document.getElementById('user-access-token');
let calleeAcsUserId = document.getElementById('callee-acs-user-id');
let initializeCallAgentButton = document.getElementById('initialize-call-agent');
let startCallButton = document.getElementById('start-call-button');
let startCallIcon = document.getElementById('start-call-icon');
let hangUpCallButton = document.getElementById('hangup-call-button');
let acceptCallButton = document.getElementById('accept-call-button');
let hangUpCallIcon = document.getElementById('hangup-call-icon');
let acceptCallIcon = document.getElementById('accept-call-icon');
// let startVideoButton = document.getElementById('start-video-button');
// let stopVideoButton = document.getElementById('stop-video-button');
let toggleMicroButton = document.getElementById('toggle-micro-button');
let toggleMicroIcon = document.getElementById('toggle-micro-icon');
let toggleVideoIcon = document.getElementById('toggle-video-icon');
let toggleVideoButton = document.getElementById('toggle-video-button');
let connectedLabel = document.getElementById('connectedLabel');
let remoteVideosGallery = document.getElementById('remoteVideosGallery');
let localVideoContainer = document.getElementById('localVideoContainer');

/**
 * Using the CallClient, initialize a CallAgent instance with a CommunicationUserCredential which will enable us to make outgoing calls and receive incoming calls. 
 * You can then use the CallClient.getDeviceManager() API instance to get the DeviceManager.
 */
async function initializeCallAgent(token) {
    try {
        const callClient = new CallClient(); 
        tokenCredential = new AzureCommunicationTokenCredential(token);
        callAgent = await callClient.createCallAgent(tokenCredential)
        // Set up a camera device to use.
        deviceManager = await callClient.getDeviceManager();
        await deviceManager.askDevicePermission({ video: true });
        await deviceManager.askDevicePermission({ audio: true });
        // Listen for an incoming call to accept.
        callAgent.on('incomingCall', async (args) => {
            try {
                incomingCall = args.incomingCall;
                acceptCallButton.disabled = false;
                acceptCallIcon.src = '/icon/accept_call.png';
                startCallButton.disabled = true;
                startCallIcon.src = '/icon/start_call_dis.png';
                if (isUserInteracted) {
                    ringtone.play();
                }
            } catch (error) {
                console.error(error);
            }
        });

        startCallButton.disabled = false;
        startCallIcon.src = '/icon/start_call.png';
    } catch(error) {
        console.error(error);
    }
}
document.getElementById('theme-toggle').addEventListener('change', function() {
    document.body.classList.toggle('dark-mode');
    document.body.classList.toggle('light-mode');
});
fetch('token_data.json')
    .then(response => response.json())
    .then(data => {
        const userAccessToken = data.token;
        const displayName = data.display_name;
        document.getElementById('user-display-name').innerHTML = `Authenticated as <span>${displayName}</span>`;
        initializeCallAgent(userAccessToken);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

fetch('display_names.json')
    .then(response => response.json())
    .then(data => {
        const select = document.getElementById('callee-acs-user-id');
        data.forEach(item => {
            const option = document.createElement('option');
            option.value = item.id;
            option.text = item.display_name;
            select.appendChild(option);
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
/**
 * Place a 1:1 outgoing video call to a user
 * Add an event listener to initiate a call when the `startCallButton` is clicked:
 * First you have to enumerate local cameras using the deviceManager `getCameraList` API.
 * In this quickstart we're using the first camera in the collection. Once the desired camera is selected, a
 * LocalVideoStream instance will be constructed and passed within `videoOptions` as an item within the
 * localVideoStream array to the call method. Once your call connects it will automatically start sending a video stream to the other participant. 
 */
startCallButton.onclick = async () => {
    try {
        const localVideoStream = await createLocalVideoStream();
        const videoOptions = localVideoStream ? { localVideoStreams: [localVideoStream] } : undefined;
        const calleeId = document.getElementById('callee-acs-user-id').value;
        call = callAgent.startCall([{ communicationUserId: calleeId }], { videoOptions });
        // Subscribe to the call's properties and events.
        subscribeToCall(call);
    } catch (error) {
        console.error(error);
    }
}

/**
 * Accepting an incoming call with video
 * Add an event listener to accept a call when the `acceptCallButton` is clicked:
 * After subscribing to the `CallAgent.on('incomingCall')` event, you can accept the incoming call.
 * You can pass the local video stream which you want to use to accept the call with.
 */
acceptCallButton.onclick = async () => {
    try {
        const localVideoStream = await createLocalVideoStream();
        const videoOptions = localVideoStream ? { localVideoStreams: [localVideoStream] } : undefined;
        call = await incomingCall.accept({ videoOptions });
        // Subscribe to the call's properties and events.
        ringtone.pause();
        ringtone.currentTime = 0;
        subscribeToCall(call);
    } catch (error) {
        console.error(error);
    }
}

/**
 * Subscribe to a call obj.
 * Listen for property changes and collection updates.
 */
subscribeToCall = (call) => {
    try {
        // Inspect the initial call.id value.
        console.log(`Call Id: ${call.id}`);
        //Subscribe to call's 'idChanged' event for value changes.
        call.on('idChanged', () => {
            console.log(`Call Id changed: ${call.id}`); 
        });

        // Inspect the initial call.state value.
        console.log(`Call state: ${call.state}`);
        // Subscribe to call's 'stateChanged' event for value changes.
        call.on('stateChanged', async () => {
            console.log(`Call state changed: ${call.state}`);
            if(call.state === 'Connected') {
                connectedLabel.hidden = false;
                acceptCallButton.disabled = true;
                acceptCallIcon.src = '/icon/accept_call_dis.png';
                startCallButton.disabled = true;
                startCallIcon.src = '/icon/start_call_dis.png';
                hangUpCallButton.disabled = false;
                hangUpCallIcon.src = '/icon/hangup.png';
                // startVideoButton.disabled = false;
                // stopVideoButton.disabled = false;
                toggleVideoButton.disabled = false;
                toggleVideoIcon.src = '/icon/video_on.png';
                toggleMicroButton.disabled = false;
                toggleMicroIcon.src = '/icon/mic_on.png';
                remoteVideosGallery.hidden = false;
                document.getElementById('connectedLabel').style.display = 'block';
            } else if (call.state === 'Disconnected') {
                connectedLabel.hidden = true;
                acceptCallIcon.src = '/icon/accept_call_dis.png';
                startCallButton.disabled = false;
                startCallIcon.src = '/icon/start_call.png';
                hangUpCallButton.disabled = true;
                hangUpCallIcon.src = '/icon/hangup_dis.png';
                // startVideoButton.disabled = true;
                // stopVideoButton.disabled = true;
                toggleVideoButton.disabled = true;
                toggleVideoIcon.src = '/icon/video_dis.png';
                toggleMicroButton.disabled = true;
                toggleMicroIcon.src = '/icon/mic_dis.png';
                document.getElementById('connectedLabel').style.display = 'none';
                console.log(`Call ended, call end reason={code=${call.callEndReason.code}, subCode=${call.callEndReason.subCode}}`);
            }   
        });

        call.on('isLocalVideoStartedChanged', () => {
            console.log(`isLocalVideoStarted changed: ${call.isLocalVideoStarted}`);
        });
        console.log(`isLocalVideoStarted: ${call.isLocalVideoStarted}`);
        call.localVideoStreams.forEach(async (lvs) => {
            localVideoStream = lvs;
            await displayLocalVideoStream();
        });
        call.on('localVideoStreamsUpdated', e => {
            e.added.forEach(async (lvs) => {
                localVideoStream = lvs;
                await displayLocalVideoStream();
            });
            e.removed.forEach(lvs => {
               removeLocalVideoStream();
            });
        });
        
        // Inspect the call's current remote participants and subscribe to them.
        call.remoteParticipants.forEach(remoteParticipant => {
            subscribeToRemoteParticipant(remoteParticipant);
        });
        // Subscribe to the call's 'remoteParticipantsUpdated' event to be
        // notified when new participants are added to the call or removed from the call.
        call.on('remoteParticipantsUpdated', e => {
            // Subscribe to new remote participants that are added to the call.
            e.added.forEach(remoteParticipant => {
                subscribeToRemoteParticipant(remoteParticipant)
            });
            // Unsubscribe from participants that are removed from the call
            e.removed.forEach(remoteParticipant => {
                console.log('Remote participant removed from the call.');
            });
        });
    } catch (error) {
        console.error(error);
    }
}

/**
 * Subscribe to a remote participant obj.
 * Listen for property changes and collection udpates.
 */
subscribeToRemoteParticipant = (remoteParticipant) => {
    try {
        // Inspect the initial remoteParticipant.state value.
        console.log(`Remote participant state: ${remoteParticipant.state}`);
        // Subscribe to remoteParticipant's 'stateChanged' event for value changes.
        remoteParticipant.on('stateChanged', () => {
            console.log(`Remote participant state changed: ${remoteParticipant.state}`);
        });

        // Inspect the remoteParticipants's current videoStreams and subscribe to them.
        remoteParticipant.videoStreams.forEach(remoteVideoStream => {
            subscribeToRemoteVideoStream(remoteVideoStream)
        });
        // Subscribe to the remoteParticipant's 'videoStreamsUpdated' event to be
        // notified when the remoteParticiapant adds new videoStreams and removes video streams.
        remoteParticipant.on('videoStreamsUpdated', e => {
            // Subscribe to new remote participant's video streams that were added.
            e.added.forEach(remoteVideoStream => {
                subscribeToRemoteVideoStream(remoteVideoStream)
            });
            // Unsubscribe from remote participant's video streams that were removed.
            e.removed.forEach(remoteVideoStream => {
                console.log('Remote participant video stream was removed.');
            })
        });
    } catch (error) {
        console.error(error);
    }
}

/**
 * Subscribe to a remote participant's remote video stream obj.
 * You have to subscribe to the 'isAvailableChanged' event to render the remoteVideoStream. If the 'isAvailable' property
 * changes to 'true', a remote participant is sending a stream. Whenever availability of a remote stream changes
 * you can choose to destroy the whole 'Renderer', a specific 'RendererView' or keep them, but this will result in displaying blank video frame.
 */
subscribeToRemoteVideoStream = async (remoteVideoStream) => {
    let renderer = new VideoStreamRenderer(remoteVideoStream);
    let view;
    let remoteVideoContainer = document.createElement('div');
    remoteVideoContainer.className = 'remote-video-container';

    let loadingSpinner = document.createElement('div');
    loadingSpinner.className = 'loading-spinner';
    remoteVideoStream.on('isReceivingChanged', () => {
        try {
            if (remoteVideoStream.isAvailable) {
                const isReceiving = remoteVideoStream.isReceiving;
                const isLoadingSpinnerActive = remoteVideoContainer.contains(loadingSpinner);
                if (!isReceiving && !isLoadingSpinnerActive) {
                    remoteVideoContainer.appendChild(loadingSpinner);
                    document.getElementById('connectedLabel').style.display = 'none';
                } else if (isReceiving && isLoadingSpinnerActive) {
                    remoteVideoContainer.removeChild(loadingSpinner);
                    document.getElementById('connectedLabel').style.display = 'block';
                }
            }
        } catch (e) {
            console.error(e);
        }
    });

    const createView = async () => {
        // Create a renderer view for the remote video stream.
        view = await renderer.createView();
        // Attach the renderer view to the UI.
        remoteVideoContainer.appendChild(view.target);
        remoteVideosGallery.appendChild(remoteVideoContainer);
    }

    // Remote participant has switched video on/off
    remoteVideoStream.on('isAvailableChanged', async () => {
        try {
            if (remoteVideoStream.isAvailable) {
                await createView();
            } else {
                view.dispose();
                remoteVideosGallery.removeChild(remoteVideoContainer);
            }
        } catch (e) {
            console.error(e);
        }
    });

    // Remote participant has video on initially.
    if (remoteVideoStream.isAvailable) {
        try {
            await createView();
        } catch (e) {
            console.error(e);
        }
    }
}

/**
 * Start your local video stream.
 * This will send your local video stream to remote participants so they can view it.
 */
// startVideoButton.onclick = async () => {
//     try {
//         const localVideoStream = await createLocalVideoStream();
//         await call.startVideo(localVideoStream);
//     } catch (error) {
//         console.error(error);
//     }
// }

/**
 * Stop your local video stream.
 * This will stop your local video stream from being sent to remote participants.
 */
// stopVideoButton.onclick = async () => {
//     try {
//         await call.stopVideo(localVideoStream);
//     } catch (error) {
//         console.error(error);
//     }
// }
toggleVideoButton.onclick = async () => {
    try {
        if (isVideoOn) {
            await call.stopVideo(localVideoStream);
            isVideoOn = false;
            toggleVideoIcon.src = '/icon/video_off.png'; 
        } else {
            const localVideoStream = await createLocalVideoStream();
            await call.startVideo(localVideoStream);
            isVideoOn = true;
            toggleVideoIcon.src = '/icon/video_on.png'; 
        }
    } catch (error) {
        console.error(error);
    }
};

toggleMicroButton.onclick = async () => {
    try {
        if (isMicroOn) {
            await call.mute();
            isMicroOn = false;
            toggleMicroIcon.src = '/icon/mic_off.png'; 
        } else {
            await call.unmute();
            isMicroOn = true;
            toggleMicroIcon.src = '/icon/mic_on.png'; 
        }
    } catch (error) {
        console.error(error);
    }
};
/**
 * To render a LocalVideoStream, you need to create a new instance of VideoStreamRenderer, and then
 * create a new VideoStreamRendererView instance using the asynchronous createView() method.
 * You may then attach view.target to any UI element. 
 */
createLocalVideoStream = async () => {
    const camera = (await deviceManager.getCameras())[0];
    if (camera) {
        return new LocalVideoStream(camera);
    } else {
        console.error(`No camera device found on the system`);
    }
}

/**
 * Display your local video stream preview in your UI
 */
displayLocalVideoStream = async () => {
    try {
        localVideoStreamRenderer = new VideoStreamRenderer(localVideoStream);
        const view = await localVideoStreamRenderer.createView();
        localVideoContainer.hidden = false;
        localVideoContainer.appendChild(view.target);
    } catch (error) {
        console.error(error);
    } 
}

/**
 * Remove your local video stream preview from your UI
 */
removeLocalVideoStream = async() => {
    try {
        localVideoStreamRenderer.dispose();
        localVideoContainer.hidden = true;
    } catch (error) {
        console.error(error);
    } 
}

/**
 * End current call
 */
// function resetCallUI() {
//     acceptCallButton.disabled = true;
//     acceptCallIcon.src = '/icon/accept_call_dis.png';
//     startCallButton.disabled = false;
//     startCallIcon.src = '/icon/start_call.png';
//     toggleVideoButton.disabled = true;
//     toggleVideoIcon.src = '/icon/video_dis.png';
//     toggleMicroButton.disabled = true;
//     toggleMicroIcon.src = '/icon/mic_dis.png';
// }
// hangUpCallButton.addEventListener("click", async () => {
//     if (isUserInteracted) {
//         if (incomingCall.state == 'Ringing') {
//             await call.hangUp({ forEveryone: true });
//             resetCallUI();
//         } else if (call) {
//             await call.hangUp({ forEveryone: true });
//             call = null;
//             resetCallUI();
//         }
//         ringtone.pause();
//         ringtone.currentTime = 0;
//     }
// });
hangUpCallButton.addEventListener("click", async () => {
    // end the current call
    await call.hangUp();
});