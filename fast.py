import asyncio
from uuid import uuid4
from requests import get
from json import dumps

SLEEP = 5


async def save(element: dict):
    file_name = uuid4()
    with open(f"./store/{file_name}.txt", "w") as f:
        json = dumps(element, indent=4)
        f.write(json)
        f.close()


async def posts():
    await asyncio.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/posts")
    posts = res.json()
    await asyncio.gather(*[save(post) for post in posts])


async def comments():
    await asyncio.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/comments")
    comments = res.json()
    await asyncio.gather(*[save(comment) for comment in comments])


async def albums():
    await asyncio.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/albums")
    albums = res.json()
    await asyncio.gather(*[save(album) for album in albums])


async def photos():
    await asyncio.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/photos")
    photos = res.json()
    await asyncio.gather(*[save(photo) for photo in photos])


async def todos():
    await asyncio.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/todos")
    todos = res.json()
    await asyncio.gather(*[save(todo) for todo in todos])


async def users():
    await asyncio.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/users")
    users = res.json()
    await asyncio.gather(*[save(user) for user in users])


async def main():
    workers = [posts(), comments(), albums(), photos(), todos(), users()]
    await asyncio.gather(*workers)


if __name__ == "__main__":
    asyncio.run(main())
