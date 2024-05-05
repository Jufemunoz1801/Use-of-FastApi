from fastapi import FastAPI, Query
#uvicorn query_fastapi:app --reload

app = FastAPI()

@app.get("/login/")
async def login(username: str = Query(None, title="Username", description="Your username"),
                rol: str = Query(None, title="rol", description="Your rol")):
    return {"Username": username, "Rol": rol}