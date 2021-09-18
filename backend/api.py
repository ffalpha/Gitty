from fastapi import FastAPI
from pydriller import Repository
app=FastAPI()

inventory ={

    1:{
        "name":"MILK"
    }
}

@app.get('/')
def home():
    return{"Data":"Test"}

@app.get('/api/v1/{git_url:path}')
def url(git_url:str):
    a=[]
    for commit in Repository(git_url).traverse_commits():
        a.append(commit.hash)
   

    return{"Data":a}

@app.get("/api/v2/commiters/{git_url:path}")
def url(git_url:str):
    a=[]
    for commit in Repository(git_url).traverse_commits():
        a.append(commit.committer.name)
    myset = set(a)
    return{"Data":myset}