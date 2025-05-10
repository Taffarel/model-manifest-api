# Model Manifest API

The **Model Manifest API** is a FastAPI-based service for generating Kubernetes-compatible YAML manifests for machine learning models. It is designed with **Clean Architecture** principles and supports secure, scalable deployments, CI/CD automation, and Kubernetes/ArgoCD integration.

---

## Features

- **YAML Manifest Generation**: Create model manifests via the `/api/v1/manifest` POST endpoint.
- **Clean Architecture**: Structured into Domain, Application, Presentation, and Infrastructure layers.
- **Secure Authentication**: Token-based access with configurable allowed tokens.
- **Comprehensive Testing**: Unit tests and coverage reporting across all layers.
- **Containerized**: Dockerized for consistency across environments.
- **CI/CD Pipeline**: Automated testing, building, and deployment using GitHub Actions.
- **Kubernetes Integration**: Designed for use with ArgoCD in production clusters.


## Prerequisites

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)  
  Verify: `docker --version`

- **Python 3.11+**  
  Verify: `python --version`


## Setup

### Clone the Repository

```bash
git clone https://github.com/your-org/model-manifest-api.git
cd model-manifest-api
```


## Set Up Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
pip install -r requirements.txt
```

## Running the API with Docker

### Build and Run

```bash
docker build -t model-manifest-api .
docker run -d -p 8000:8000 --name model-manifest-api model-manifest-api
```

## Testing the API

### Generate a Manifest

```bash
curl -H "Authorization: Bearer token1" \
     -H "Content-Type: application/json" \
     -X POST http://localhost:8000/api/v1/manifest \
     -d '{"model_name":"testmodel","model_source_url":"https://example.com/model","replicas":2,"memory":"100Mi"}'
```

### Expected Response

```json
{"manifest":"kind: Model\nmetadata:\n  name: testmodel\nspec:\n  storageUri: https://example.com/model\n  requirements:\n sklearn\n  memory: 100Mi\n  replicas: 2\n"}
```

### Save the Manifest to File

```json
curl -H "Authorization: Bearer token1" \
     -H "Content-Type: application/json" \
     -X POST http://localhost:8000/api/v1/manifest \
     -d '{"model_name":"testmodel","model_source_url":"https://example.com/model","replicas":2,"memory":"100Mi"}' \
     | jq -r .manifest > testmodel.yaml
```

## Running Unit Tests

```bash
pip install -r requirements.txt
pip install pytest-cov
pytest --cov=src --cov-report=html
```

View results in htmlcov/index.html

## CI/CD Pipeline

GitHub Actions automatically:

* Runs tests and uploads coverage reports
* Builds and pushes Docker images to Docker Hub
* Updates Kubernetes manifests