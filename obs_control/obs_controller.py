import simpleobsws
import tracemalloc
import asyncio
tracemalloc.start()

class OBS:
    def __init__(self,port=4444):
        self.server = simpleobsws.WebSocketClient(
            url=f"ws://localhost:{port}",identification_parameters=simpleobsws.IdentificationParameters())
        async def connection():
            print(await self.server.connect())
            await self.server.wait_until_identified()
            
        asyncio.get_event_loop().run_until_complete(connection())

    def start_stream(self):
        async def start():
            turn_on = simpleobsws.Request("StartStream")
            print(await self.server.call(turn_on))
        asyncio.get_event_loop().run_until_complete(start())

    def stop_stream(self):
        async def start():
            turn_on = simpleobsws.Request("StopStream")
            print(await self.server.call(turn_on))
        asyncio.get_event_loop().run_until_complete(start())

    def print_text(self,text):
        async def start():
            turn_on = simpleobsws.Request("SendStreamCaption",requestData={"captionText":text})
            print(await self.server.call(turn_on))
        asyncio.get_event_loop().run_until_complete(start())

if __name__ == "__main__":
    obs_controller = OBS()
    obs_controller.print_text("test")