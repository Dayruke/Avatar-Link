#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import mycroft_map

'''
    IP = "10.0.0.17"
    uri = f"ws://{IP}:8181/core"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"||| I heard {message}")
            '''

async def ProcessMycroftMB():
    
    # MycroftIP = "127.0.0.1" # mycroft instance IP
    MycroftIP = "10.0.0.17"
    uri_Mycroft = f"ws://{MycroftIP}:8181/core"
    ListenToAppChannel = asyncio.create_task(
    listen(uri_Mycroft))
    await ListenToAppChannel



async def listen(uri_Mycroft):
    async with websockets.connect(uri_Mycroft) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Heard {message}")

            messageToForward = mycroft_map.MycroftMap().translate(message)

            if (messageToForward != ''):
                print(f"will forward : {messageToForward}")

                uri_AvatarServer = "ws://127.0.0.1:9494"
                ForwardToAvatarChannel = asyncio.create_task(
                forward(uri_AvatarServer, messageToForward))

                await ForwardToAvatarChannel

                print('>>> Message Forwarded')
            else:
                print('--- Irrelevant message')
        


async def forward(uri_AvatarServer,msg):
    async with websockets.connect(uri_AvatarServer) as websocket:
        await websocket.send(msg)
        print("Sent {msg} to Avatar_Server")


# Event Loop

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(ProcessMycroftMB())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally: 
    print("closing Loop")
    loop.close()



'''

# WS client example

import asyncio
import websockets

async def hello():
    uri = "ws://10.0.0.17:8181/core"
    async with websockets.connect(uri) as websocket:
        #MyType = input("What's your name? ")
        #MyData = input("data")

    # '{"name": "value"}' 
    #MyType = 'speak'
    #MyData = '{"utterance": "Yo dude"}' 
        
    #message = '{"type": "' + MyType + '", "data": ' + MyData +'}'  

        
        # say somethign to mycroft
        command = "what time is it"
        message = "{\"data\": {\"utterances\": [\""+command+"\"]}, \"type\": \"recognizer_loop:utterance\", \"context\": null}"
        # message = 'enclosure.eyes.narrow'

        await websocket.send(message)
        print(f"> {message}")

        MycroftResponse = await websocket.recv()
        print(f"< {MycroftResponse}")


asyncio.get_event_loop().run_until_complete(hello())

'''