from fastapi import APIRouter, Depends

api = APIRouter(prefix="/api/llm")
openapi_tags = {
    "name": "LLM",
    "description": "Create, update, delete, and retrieve LLM/user strings.",
}

# POST /api/productivity/
# Creates a new pomodoro timer.
# Note: This API will take in a request body. What type should this be?
# Expected return type: PomodoroTimer
@api.post("", response_model=String, tags=["LLM"])
def create_response(temp: String, ccService: ccService = Depends(),
) -> String:
    return ccService.create_string(temp)

# TODO: Implement the following API:
# GET /api/productivity/{id}
# Get a pomodoro timer by its ID.
# Expected return type: PomodoroTimer
@api.get("", response_model=String, tags=["LLM"])
def get_response(temp: String, ccService: ccService = Depends(),
) -> String:
    return ccService.get_response()