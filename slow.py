from uuid import uuid4
from requests import get
from json import dumps
import time

SLEEP = 5


def save(element: dict):
    file_name = uuid4()
    with open(f"./store/{file_name}.txt", "w") as f:
        json = dumps(element, indent=4)
        f.write(json)
        f.close()


def posts():
    time.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/posts")
    posts = res.json()
    for post in posts:
        save(post)


def comments():
    time.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/comments")
    comments = res.json()
    for comment in comments:
        save(comment)


def albums():
    time.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/albums")
    albums = res.json()
    for album in albums:
        save(album)


def photos():
    time.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/photos")
    photos = res.json()
    for photo in photos:
        save(photo)


def todos():
    time.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/todos")
    todos = res.json()
    for todo in todos:
        save(todo)


def users():
    time.sleep(SLEEP)
    res = get("https://jsonplaceholder.typicode.com/users")
    users = res.json()
    for user in users:
        save(user)


def main():
    fns = [posts, comments, albums, photos, todos, users]
    for fn in fns:
        fn()


if __name__ == "__main__":
    main()
