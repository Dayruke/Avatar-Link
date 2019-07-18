#!/usr/bin/env python

# WS client example

import asyncio
import websockets

connectedClients = set()

async def broadcast(websocket, msg):
   
    # await websocket.send(msg) #old

    # send message to all connected clients
    if connectedClients:  # asyncio.wait doesn't accept an empty list
        broadcastMsg = msg # f"broadcasting |> {msg}" # reformat message from map here
        await asyncio.wait([user.send(broadcastMsg) for user in connectedClients])
        print(broadcastMsg)


async def listen(websocket):
    msg = await websocket.recv()
    print(f"avatar-server heard : {msg}")
    return msg



async def myServer(websocket, path):

    # Register client as connected
    connectedClients.add(websocket)
    try:
        # queue listening task
        taskListen = asyncio.create_task(
        listen(websocket))

        msgToBroadcast = await taskListen

        # now that it has a message, queue broadcast task 
        taskBroadcast = asyncio.create_task(
            broadcast(websocket, msgToBroadcast))

        await taskBroadcast


    finally:
        # Unregister.
        connectedClients.remove(websocket)





# create server
start_server = websockets.serve(myServer, "localhost", 9494)

# event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


