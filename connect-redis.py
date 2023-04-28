import asyncio
import aioredis
import nest_asyncio
nest_asyncio.apply()

async def main():
    
    redis = await aioredis.create_redis_pool('redis://localhost')
    #setting key value 
    await redis.set('my-key', 'value')
    #retrieving value
    value = await redis.get('my-key', encoding='utf-8')
    print(value)
    redis.close()
    await redis.wait_closed()

    asyncio.run(main())

    value
