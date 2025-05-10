from src.domain.use_cases.generate_manifest import GenerateManifestUseCase
from src.application.dtos.manifest_dto import ManifestRequestDTO
from src.infrastructure.serializers.yaml_serializer import YamlSerializer

class ManifestService:
    def __init__(self, generate_manifest_use_case: GenerateManifestUseCase, serializer: YamlSerializer):
        self.generate_manifest_use_case = generate_manifest_use_case
        self.serializer = serializer

    def generate_manifest(self, request: ManifestRequestDTO) -> str:
        manifest = self.generate_manifest_use_case.execute(
            name=request.model_name,
            storage_uri=str(request.model_source_url),
            replicas=request.replicas,
            memory=request.memory,
        )
        return self.serializer.serialize(manifest.to_dict())