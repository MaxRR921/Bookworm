from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple POST Example", version="0.1.0")


class Payload(BaseModel):
    """Shape of the JSON body the POST endpoint accepts."""

    text: str


class Response(BaseModel):
    """Structure returned by the POST endpoint."""

    success: bool
    received: str
    length: int


@app.get("/")
def read_root() -> Any:  # simple health check available via GET /
    return {"status": "ok", "message": "Send a POST to /run to invoke the handler"}


@app.post("/run", response_model=Response)
def run_job(payload: Payload) -> Response:
    """Example POST route callable from Postman."""

    transformed = payload.text.strip()
    return Response(
        success=True,
        received=transformed,
        length=len(transformed),
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("fast-api:app", host="0.0.0.0", port=8000, reload=True)
