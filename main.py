from  fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/")
async def all_messages():
	     return  {"status": 200,  "messages": [ {"messageid":12132,"message":"This is a Hello Endpoint!" }]}

@app.get("/message/{messageid}")
async def get_message(messageid: int):
	     return  {"status": 200,  "message": { "messageid":messageid,"message":"This is a Hello Endpoint using message ID!" }}

@app.post("/message/")
async def create_message(message: Message):
	     return message