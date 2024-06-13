import time
from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AddRequest(BaseModel):
    a: int
    b: int


@app.post("/add")
async def add(request: AddRequest) -> Dict[str, int]:
    result = request.a + request.b
    time.sleep(20)  # Wait for 2 seconds
    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
