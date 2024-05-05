from fastapi import	FastAPI, Body
from pydantic import BaseModel
#uvicorn body_fastapi:app --reload
#curl -X POST "http://localhost:8000/login/" -H "Content-Type: application/json" -d '{"username":"john", "rol":"Developer"}'
app = FastAPI()

class UserLogin(BaseModel):
    username: str
    rol: str

@app.post("/login/")
async def login(user: UserLogin = Body(...)):
    return user.model_dump()