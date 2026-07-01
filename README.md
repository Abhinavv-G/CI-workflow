# Continuous Integration Pipeline with GitHub Actions

Automated Continuous Integration (CI) pipeline that builds, tests, and publishes a Dockerized Flask application to Docker Hub on every push to the `main` branch.

## Architecture

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/2c226416-7678-49b3-8b0b-ec22e9ef4b5f" />


```
Push to main
      │
      ▼
GitHub Actions
      │
      ▼
Checkout Repository
      │
      ▼
Build Docker Image
      │
      ▼
Run Pytest
      │
      ▼
Docker Hub Login
      │
      ▼
Push Versioned Docker Images
```

## Tech Stack

- GitHub Actions
- Docker
- Docker Hub
- Python
- Flask
- Pytest

## Pipeline Workflow

- Triggers automatically on every push to the `main` branch or via manual workflow dispatch.
- Checks out the latest repository source code.
- Builds a Docker image tagged with the Git commit SHA.
- Executes the application's Pytest test suite inside the Docker container.
- Authenticates securely with Docker Hub using GitHub Secrets.
- Publishes Docker images tagged as both `latest` and the commit SHA.

## Run Locally

```bash
docker build -t devops-app .
docker run -p 5000:5000 devops-app
```

Visit:

```
http://localhost:5000/health
```
