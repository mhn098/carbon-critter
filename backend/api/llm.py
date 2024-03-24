import string
from fastapi import APIRouter, Depends
from ..services.llm import ccService

api = APIRouter(prefix="/api/llm")
openapi_tags = {
    "name": "LLM",
    "description": "Create, update, delete, and retrieve LLM/user strings.",
}

# POST /api/productivity/
# Creates a new pomodoro timer.
# Note: This API will take in a request body. What type should this be?
# Expected return type: PomodoroTimer
@api.post("", response_model=string, tags=["LLM"])
def create_user(temp: string, ccService: ccService = Depends(),
) -> None:
    return ccService.create_user(temp)

# TODO: Implement the following API:
# GET /api/productivity/{id}
# Get a pomodoro timer by its ID.
# Expected return type: PomodoroTimer
@api.get("", response_model=string, tags=["LLM"])
def get_answer(temp: string, ccService: ccService = Depends(),
) -> string:
    return ccService.get_answer()