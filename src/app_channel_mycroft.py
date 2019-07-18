#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import mycroft_map

'''
1 Monitors Mycroft App Channel
2 Translates Messages for Avatar Channel
3 Forwards Translated Message to Server for Broadcast
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


