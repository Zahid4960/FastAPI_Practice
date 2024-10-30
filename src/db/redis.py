import redis.asyncio as redis_asyncio_instance
from src.config import RedisConfig

JTI_EXPIRY = 3600

token_blocklist = redis_asyncio_instance.from_url(RedisConfig.REDIS_DATABASE_URL)

async def add_jti_to_blocklist(jti: str) -> None:
    await token_blocklist.set(name=jti, value='', ex=JTI_EXPIRY)

async def token_in_blocklist(jti: str) -> bool:
    jti = await token_blocklist.get(jti)

    return jti is not None
