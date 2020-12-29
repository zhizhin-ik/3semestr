from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service):
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as resp:
            json_resp= await resp.json()
            ip = json_resp[service.ip_attr]
            return '{} finished with result: {}'.format(service.name, ip)


async def asynchronous():
    fut = [fetch_ip(service) for service in SERVICES]
    done, pending =await asyncio.wait(fut, return_when=FIRST_COMPLETED)
    print(done.pop().result())

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())