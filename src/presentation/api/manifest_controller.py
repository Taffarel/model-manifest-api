from fastapi import APIRouter, Depends, HTTPException
from src.application.dtos.manifest_dto import ManifestRequestDTO
from src.application.services.manifest_service import ManifestService
from src.infrastructure.security.auth import verify_token
from src.domain.use_cases.generate_manifest import GenerateManifestUseCase
from src.infrastructure.serializers.yaml_serializer import YamlSerializer

router = APIRouter()

def get_manifest_service():
    use_case = GenerateManifestUseCase()
    serializer = YamlSerializer()
    return ManifestService(use_case, serializer)

@router.post("/manifest", response_model=dict, dependencies=[Depends(verify_token)])
async def generate_manifest(request: ManifestRequestDTO, service: ManifestService = Depends(get_manifest_service)):
    try:
        yaml_manifest = service.generate_manifest(request)
        return {"manifest": yaml_manifest}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")