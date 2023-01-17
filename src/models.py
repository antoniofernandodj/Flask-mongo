from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_login import UserMixin
from werkzeug.security import generate_password_hash as hash
from bcrypt import hashpw, checkpw, gensalt
from typing import Optional


params = 'retryWrites=true&w=majority'
password = 'Gl544632&'
username = 'antoniofernandodj'
MONGODB_URI = f"mongodb+srv://"  \
    + F"{username}:{password}@cluster0.agz8o1v.mongodb.net/?{params}"

client = MongoClient(MONGODB_URI)
db = client.database
user_collection = db.users


class User(UserMixin):
    def __init__(
        self, name=None, username=None, password=None,
        _id = None, id = None, salt = None,
    ):  
        self.name = name
        self.username = username
        self.password = password
        self.id = id if id else None
        self._id = _id if _id else None
        self.salt = salt if salt else None
        if id is None:
            try:
                self.id = User.last_id() + 1
            except IndexError:
                self.id = 1
    
    @classmethod
    def last_id(cls):
        all = User.find_all()
        last_item = all[-1]
        return last_item['id']    
        
    @classmethod
    def find_all(cls):
        all = list(user_collection.find({}))
        return all
    
    @classmethod
    def find(
        cls, id: Optional[int] = None,
        username: Optional[str] = None
    ):
        user = None
        if id:
            if isinstance(id, str):
                id = int(id)
            user = user_collection.find_one({'id': id})
        elif username:
            user = user_collection.find_one({'username': username})
        if user:
            user = User(**user)
            return user
    
    def save(self):
        dic = self.__dict__
        dic['salt'] = gensalt()
        password = hashpw(self.password.encode('utf-8'), dic['salt'])
        dic['password'] = password
        del dic['_id']
        user_collection.insert_one(dic)
        
    @classmethod
    def validate_credentials(cls, username, password):
        user = User.find(username=username)
        if user:
            password_ok = checkpw(
                password.encode('utf-8'),
                user.password
            )
            if password_ok:
                return user
        return None

    def __repr__(self) -> str:
        return f'User(id: {self.id}, name: {self.name})'
        
    def __str__(self) -> str:
        return f'<User {{ id: {self.id}, name: {self.name} }}>'
    
# user = User(
#     name='Antonio',
#     username='antoniofernandodj',
#     password='123456'
# )

# user.save()