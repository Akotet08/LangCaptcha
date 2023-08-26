from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from app.api.endpoints import router as endpoint_router

def init_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(endpoint_router)

    return app

app = init_app()


@app.get("/")
def root():
    return "Team Bytes language captcha backend"
