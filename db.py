import pymongo

client = pymongo.MongoClient("mongodb+srv://dangduylan:lJCJiSpJuNpzDatG@cluster0-noolz.mongodb.net/test?retryWrites=true")
db = client.users
db1 = client.posts

def add_user(username,nick_name,password):
    return  db.users.insert_one({
            "username":username,
            "nick_name":nick_name,
            "password":password
            })
    

def find_username(username):
    return db.users.find_one({"username":username})

def add_post(content):
        return db1.posts.insert_one({
                "content" : content
        })

def get_all():
    return list(db.users.find({}))

def get_allposts():
        return list(db1.posts.find({}))