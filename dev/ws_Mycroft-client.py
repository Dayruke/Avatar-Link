#!/usr/bin/env python

import asyncio
import websockets

'''
Listen Test
----------
Connects to the Message Bus (web socket) 
of a running instance of Mycroft
Echos all emitted messages
'''

async def ListenMycroftMB():
    IP = "127.0.0.1" # Mycroft instance IP address
    uri = f"ws://{IP}:8181/core"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"||| I heard {message}")

# Event Loop

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(ListenMycroftMB())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally: 
    print("closing Loop")
    loop.close()
