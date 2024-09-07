from uuid import uuid4

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def server_two():
    uid = uuid4()
    return {"message": "server two", "random_id": uid}


def main():
    uvicorn.run(app="main:app", host="0.0.0.0", port=8002, reload=True)


if __name__ == "__main__":
    main()
