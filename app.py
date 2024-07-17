import os
import json
import sqlite3

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict
import uvicorn

from utils import create_logger

app = FastAPI()

class KeyValue(BaseModel):
    key: str
    value: Dict[str, Any]


@app.post("/set")
async def set_value(kv: KeyValue):
    try:
        cursor.execute("""
            INSERT INTO cache (key, value)
            VALUES (?, ?)
            """, (kv.key, json.dumps(kv.value)))
        
        return JSONResponse(
            status_code=201,
            content={
                "message": "value set",
                "key": kv.key
            }
        )
    except:
        logger.error(f"Exception {os.sys.exc_info()}")
        return JSONResponse(
            status_code=500,
            content={
                "message": "an error occured!"
            }
        )


@app.get("/get")
async def get_value(key: str):
    try:
        res = cursor.execute("""
            SELECT key, value FROM cache WHERE key = ?
            """, (key,))
        
        value = res.fetchone()[1]
        
        return JSONResponse(
            status_code=201,
            content={
                "value": json.loads(value)
            }
        )
    except:
        logger.error(f"Exception {os.sys.exc_info()}")
        return JSONResponse(
            status_code=500,
            content={
                "message": "an error occured!"
            }
        )


logger = create_logger()

if __name__ == "__main__":
    with open("./config.json", "r") as file:
        conf = json.load(file)

    con = sqlite3.connect(":memory:")
    cursor = con.cursor()

    # create a table
    cursor.execute("""
        CREATE TABLE cache (
            key TEXT PRIMARY KEY, 
            value TEXT)"""
        )

    uvicorn.run(app, host=conf["host"], port=conf["port"])