from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello yooo"}

@app.get("/posts")
async def get_posts():
    return {"posts":"this is your posts"}

@app.post("/pasts")
def get_pasts(payload: dict= Body(...)):
    print(payload)
    return {"new":f"title {payload['title']} content {payload['content']}"}