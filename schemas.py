from typing import List, Optional
from pydantic import BaseModel

#Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    publish: bool
    class Config():
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    items : List[Article] = []
    class Config():
        from_attributes = True

# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    class Config():
        from_attributes = True
        
class ArticleBase(BaseModel):
    title: str
    content: str 
    publish: bool
    creator_id: int
    
class ArticleDisplay(BaseModel):
    title: str
    content: str 
    publish: bool 
    user: Optional[User] = None
    class Config():
        from_attributes = True