# =====================================================
# FastAPI App Initialization
# =====================================================
from fastapi import FastAPI
from backend.routes import router

app = FastAPI(title='Leave Management API')

# Include all routes
app.include_router(router)
