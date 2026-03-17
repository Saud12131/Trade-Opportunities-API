from fastapi import FastAPI
from app.routes.analyze import router as analyze_router
app = FastAPI(
    title="Trade Opportunities API",
    version="1.0"
)
app.include_router(analyze_router)

@app.get("/")
def root():
    return{
        "message":"FastApi working"
    }