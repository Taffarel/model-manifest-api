from pydantic import BaseModel, HttpUrl, Field, ConfigDict

class ManifestRequestDTO(BaseModel):
    model_name: str = Field(..., min_length=1, max_length=100)
    model_source_url: HttpUrl
    replicas: int = Field(..., ge=1, le=10)
    memory: str = Field(..., pattern=r"^\d+(Ki|Mi|Gi)$")

    model_config = ConfigDict(protected_namespaces=())