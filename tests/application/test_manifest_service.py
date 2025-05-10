from src.application.services.manifest_service import ManifestService
from src.application.dtos.manifest_dto import ManifestRequestDTO
from src.domain.use_cases.generate_manifest import GenerateManifestUseCase
from src.infrastructure.serializers.yaml_serializer import YamlSerializer

def test_manifest_service_success():
    use_case = GenerateManifestUseCase()
    serializer = YamlSerializer()
    service = ManifestService(use_case, serializer)
    request = ManifestRequestDTO(
        model_name="testmodel",
        model_source_url="https://example.com",
        replicas=2,
        memory="100Mi",
    )
    result = service.generate_manifest(request)
    assert "kind: Model" in result
    assert "name: testmodel" in result