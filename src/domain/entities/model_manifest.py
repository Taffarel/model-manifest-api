from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ModelManifest:
    name: str
    storage_uri: str
    replicas: int
    memory: str
    requirements: List[str]

    def to_dict(self) -> dict:
        return {
            "kind": "Model",
            "metadata": {"name": self.name},
            "spec": {
                "storageUri": self.storage_uri,
                "requirements": self.requirements,
                "memory": self.memory,
                "replicas": self.replicas,
            },
        }