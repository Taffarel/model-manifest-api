from src.domain.entities.model_manifest import ModelManifest

class GenerateManifestUseCase:
    def execute(self, name: str, storage_uri: str, replicas: int, memory: str) -> ModelManifest:
        if not name.isalnum():
            raise ValueError("Model name must be alphanumeric")
        if replicas < 1 or replicas > 10:
            raise ValueError("Replicas must be between 1 and 10")
        if not memory or not memory.endswith(("Ki", "Mi", "Gi")):
            raise ValueError("Memory must be in format <number>(Ki|Mi|Gi)")
        return ModelManifest(
            name=name,
            storage_uri=storage_uri,
            replicas=replicas,
            memory=memory,
            requirements=["sklearn"],
        )