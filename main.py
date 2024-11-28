import asyncio
from driver import drive

async def main():
    await drive()


if __name__ == "__main__":
    asyncio.run(main())