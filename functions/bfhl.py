from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/bfhl")
async def handle_post(data: dict):
    # Add your POST logic here
    return JSONResponse(content={"is_success": True})

@app.get("/bfhl")
async def handle_get():
    return JSONResponse(content={"operation_code": 1})
