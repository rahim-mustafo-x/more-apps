from uvicorn import Server, Config
from apis import app
from asyncio import run

async def main():
    config = Config(app=app, host="0.0.0.0", port=6767)
    server = Server(config=config)
    await server.serve()

if __name__ == "__main__":
    run(main())