from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Endpoint to fetch blogs
@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    """
    Fetch blogs based on query parameters.
    - `limit`: Number of blogs to fetch.
    - `published`: Whether to fetch published blogs only.
    - `sort`: Sorting order (optional).
    """
    if published:
        return {'data': f'{limit} published blogs from the database'}
    else:
        return {'data': f'{limit} blogs from the database'}

# Endpoint to fetch unpublished blogs
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'All unpublished blogs'}

# Endpoint to fetch a blog by ID
@app.get('/blog/{id}')
def show(id: int):
    """
    Fetch a specific blog by its ID.
    """
    return {'data': f'Blog with ID {id}'}

# Endpoint to fetch comments for a specific blog
@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10):
    """
    Fetch comments for a blog with a given ID.
    - `id`: Blog ID.
    - `limit`: Number of comments to fetch (default is 10).
    """
    return {'data': [f'Comment {i}' for i in range(1, limit + 1)]}

# Data model for creating a blog
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True

# Endpoint to create a new blog
@app.post('/blog')
def create_blog(blog: Blog):
    """
    Create a new blog.
    - `blog`: Blog data from the request body.
    """
    return {'data': f"Blog is created with title as {blog.title}"}

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port = 9000)