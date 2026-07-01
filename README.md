# CI Pipeline with GitHub Actions & Docker

Automated CI pipeline that tests, builds, and ships a Dockerized 
Python application to Docker Hub on every push to main — zero manual steps.

## Architecture

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/3ac9a1dd-2dfb-4f63-a906-559170904a49" />



## Tech Stack
- GitHub Actions (CI/CD automation)
- Docker + Docker Hub (containerization & registry)
- Python + pytest (application & testing)

## What the Pipeline Does
1. Triggers on push to `main` or manual dispatch
2. Checks out repository code
3. Builds Docker image
4. Runs pytest inside the container
5. Authenticates with Docker Hub via GitHub Secrets
6. Pushes image to Docker Hub

## Run Locally
docker build -t myapp .
docker run myapp







