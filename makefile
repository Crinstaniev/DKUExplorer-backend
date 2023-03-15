# Docker image names and tags
IMAGE1_NAME = dkuar-frontend
IMAGE1_TAG = latest
IMAGE2_NAME = dkuar-backend
IMAGE2_TAG = latest
IMAGE1_PATH = docker/frontend.dockerfile
IMAGE2_PATH = docker/backend.dockerfile

# Docker registry
REGISTRY = dockerhub.io

docker: build push

# Build and tag Docker images
build:
    # docker build -t $(REGISTRY)/$(IMAGE1_NAME):$(IMAGE1_TAG) -f $(IMAGE1_PATH) .
	docker build -t $(REGISTRY)/$(IMAGE2_NAME):$(IMAGE2_TAG) -f $(IMAGE2_PATH) .

# Push Docker images to registry
push:
    # docker push $(REGISTRY)/$(IMAGE1_NAME):$(IMAGE1_TAG)
	docker push $(REGISTRY)/$(IMAGE2_NAME):$(IMAGE2_TAG)

test:
	pytest -s -v

run:
	python backend/app.py

requirements:
	pip freeze > requirements.txt