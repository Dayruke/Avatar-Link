# Avatar Link | Design Document

## Introduction

The Link serves as middleware, loosely coupling application software and its embodied agent, or avatar.

![Conceptual Diagram](https://raw.githubusercontent.com/Dayrook/Avatar-Link/master/Documentation/Images/BasicDiagram.png)

An **Avatar** is an embodied software representation. An Avatar's embodiment can be in the form of digital graphics or physical hardware. We'll refer to the software an Avatar embodies as an **App**.

Typically, an Avatar will operate entirely by its own bundled programming. It may also use communicate externally through API, but that interface is written into the Avatar's code. This is limiting because any capabilities desired for an Avatar must be specifically programmed, both in terms of the function of the App - or interface with the App - and the Avatar's behavior (movement, sounds, etc.).

The Link will interpret the interaction between User and App and then pass messages to an Avatar in a standard format output. Thereby, as more apps are implemented for the Link, and as each app becomes more capable, the associated Avatars will automatically benefit.

This first phase of development will implement enough functionality that a Linked Avatar knows when the App and User are actively communicating. Potential future developments are discussed in the last section.

## Requirements

1. Avatar can function agnostic of its embodied App
2. The Avatar will know when the App is **Speaking**
3. The Avatar will know when the App is **Listening**

## Implementation

We'll develop in Python -- its ease of use and extensive libraries increase the chances of getting a project up and running quickly.

Our initial focus for App interoperability with the Link are Virtual / voice assistants such as Alexa, Google Assistant, and Mycroft.

[Mycroft](https://mycroft.ai/) is the first App we will integrate with the Link. 


### App Channel

Mycroft's [Message Bus](https://mycroft.ai/documentation/message-bus/) employs web sockets to communicate between its client and server software. The Message Bus should provide enough data to serve as the App Channel. 

`recognizer_loop:audio_output_start` signals that the voice assistant is speaking

`recognizer_loop:record_begin` signals that the voice assistant is processing user utterances


### Avatar Channel Standard


The Link will run a socket.io server for message passing.

Using network communication for the Avatar channel allows the Link and Avatar to sit on separate machines. In a typical setup, the Link will be deployed on the user interface hardware along with the Avatar. 

The following are suggestions for how the Avatar should behave upon receiving messages in the Avatar Channel.

`speech:begin_speaking` Begin talking animation

`speech:end_speaking` End talking animation

`mood:listening` Animate to show attentive listening


## Looking Forward

In the current design, we the only mode of data we consider on the App Channel is network traffic. Realistically, the App Channel could include a variety of modes, such as phonemes of speech interaction or environmental sensor data from the user's platform.

Beyond Speaking and Listening, many states and processes within the App could be signaled by an Avatar. For example, Mycroft's `recognizer_loop:sleep` message could signal the avatar to appear preoccupied.

The avatar functions agnostic of the App it currently embodies. However, an Avatar designer may want the Avatar to signal incorporate that information. An Avatar might dress in outfits appropriate for the topic of discussion.

The Link relationship to the App Channel is currently a one-way street, pulling data out of the App Channel. We expect Avatars to know things about the user like location, attentive gaze, and mood. The Link could pass this or other information to the App. 

