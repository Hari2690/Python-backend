from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tests.test_google_gpt import test_google_gpt_api
from pydantic import BaseModel

app = FastAPI()

# Allow all CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    message: str

@app.post("/ask-gpt")
def ask_gpt(request: QueryRequest):
    print("api call reccived")
    response = test_google_gpt_api(request.message)
    return {"response": response}
