#!/usr/bin/env python

# WS client example

import asyncio
import websockets

'''
Echos the Avatar Server
'''

async def HeyListen():
    # uri = "ws://localhost:8765" # ws_server.py
    uri = "ws://localhost:9494" # Avatar Channel Server
    async with websockets.connect(uri) as websocket:
        while True:
            print(f"||| I am Listening")
          #  await websocket.send('Listeno ')
            
            broadcastMsg = await websocket.recv()
            print(f"||| I heard {broadcastMsg}")


# asyncio.get_event_loop().run_until_complete(HeyListen())
asyncio.ensure_future(HeyListen())
asyncio.get_event_loop().run_forever()


