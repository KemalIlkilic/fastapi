from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

#title str, content str
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None


my_posts = [{"title": "Post 1", "content": "This is the content of the first post", "published": True, "rating": 4, "id" : 1},
            {"title": "Post 2", "content": "This is the content of the second post", "published": True, "rating": 5, "id" : 2}]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post



@app.get("/")
def root():
    return {"message": "anan"}

@app.get("/posts")  
def get_posts():
    return {"data" : my_posts}

@app.post("/posts")
def create_posts(post: Post ):
    post_dict = post.model_dump()
    #post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"post" : post_dict} #goes back to client as HTTP response $

@app.get("/posts/{id}")
def get_post(id : int):
    post = find_post(id)
    return {"post" : post}
