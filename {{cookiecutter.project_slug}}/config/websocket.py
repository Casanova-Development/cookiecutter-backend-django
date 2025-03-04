"""Websocket use example."""


async def websocket_application(scope, receive, send):
    """Wait for an event and perform an action according to the event type."""
    while True:
        event = await receive()

        if event['type'] == 'websocket.connect':
            await send({'type': 'websocket.accept'})

        if event['type'] == 'websocket.disconnect':
            break

        if event['type'] == 'websocket.receive':
            if event['text'] == 'ping':
                await send({'type': 'websocket.send', 'text': 'pong!'})
