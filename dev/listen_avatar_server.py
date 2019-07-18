#!/usr/bin/env python

# WS client example


import asyncio
import websockets

async def HeyListen():
    # uri = "ws://localhost:8765" # ws_server.py
    uri = "ws://localhost:9494" # Avatar Channel Server
    async with websockets.connect(uri) as websocket:
        while True:
            print(f"||| I am Listening")
          #  await websocket.send('Listeno ')
            
            greeting = await websocket.recv()
            print(f"||| I heard {greeting}")


# asyncio.get_event_loop().run_until_complete(HeyListen())
asyncio.ensure_future(HeyListen())
asyncio.get_event_loop().run_forever()


'''

async def hello(websocket, path):
    name = await websocket.recv() 
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
'''
