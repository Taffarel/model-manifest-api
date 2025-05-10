import pytest
from src.domain.use_cases.generate_manifest import GenerateManifestUseCase
from src.domain.entities.model_manifest import ModelManifest

def test_generate_manifest_success():
    use_case = GenerateManifestUseCase()
    manifest = use_case.execute("testmodel", "https://example.com", 2, "100Mi")
    assert isinstance(manifest, ModelManifest)
    assert manifest.name == "testmodel"
    assert manifest.replicas == 2
    assert manifest.memory == "100Mi"

def test_generate_manifest_invalid_name():
    use_case = GenerateManifestUseCase()
    with pytest.raises(ValueError, match="Model name must be alphanumeric"):
        use_case.execute("test-model", "https://example.com", 2, "100Mi")

def test_generate_manifest_invalid_memory():
    use_case = GenerateManifestUseCase()
    with pytest.raises(ValueError, match="Memory must be in format"):
        use_case.execute("testmodel", "https://example.com", 2, "100MB")