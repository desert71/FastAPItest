import re
from fastapi import FastAPI, Request, HTTPException

head_app = FastAPI()

@head_app.get('/headers')
async def get_head(req: Request):
    if  "User-agent" not in req.headers:
        return HTTPException(status_code=400, detail="The User-Agent header not found!")
    elif "Accept-Language" not in req.headers:
        return HTTPException(status_code=400, detail="The Accept-Language header not found!")
    return {"User-agent": req.headers["User-agent"], "Accept-Language": req.headers["Accept-Language"]}