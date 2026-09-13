from fastapi import FastAPI

from app.api.routes.tasks import router as tasks_router

app = FastAPI(title="Tasks API", version="1.0.0")

app.include_router(tasks_router)


@app.get("/")
def root():
    return {"message": "Tasks API"}


@app.get("/health")
def health():
    return {"status": "ok"}
