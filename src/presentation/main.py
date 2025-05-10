from fastapi import FastAPI
from src.presentation.api.manifest_controller import router as manifest_router

app = FastAPI(
    title="Model Manifest API",
    description="API to generate Kubernetes model manifests",
    version="1.0.0",
)

app.include_router(manifest_router, prefix="/api/v1")