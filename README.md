# Continuous Integration Pipeline with GitHub Actions

Automated Continuous Integration (CI) pipeline that builds, tests, validates, and publishes a Dockerized Flask System Diagnostics API to Docker Hub on every push to the `main` branch.

---

## Architecture

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/937b66cb-1500-4024-b3b8-a74a5fc93ee8" />

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
Verify Application Health
      │
      ▼
Docker Hub Login
      │
      ▼
Push Versioned Docker Images
```

---

## Tech Stack

- Python
- Flask
- Pytest
- Docker
- Docker Hub
- GitHub Actions
---

## Pipeline Workflow

- Triggers automatically on every push to the `main` branch or via manual workflow dispatch.
- Checks out the latest repository source code.
- Builds a Docker image tagged with the Git commit SHA.
- Executes the Pytest test suite inside the Docker container.
- Starts the container and verifies the `/health` endpoint before publishing the image.
- Authenticates securely with Docker Hub using GitHub Secrets.
- Publishes Docker images tagged as both `latest` and the Git commit SHA.

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Returns application status |
| `/health` | Health check endpoint |
| `/system` | Displays host operating system and runtime information |
| `/app-info` | Displays application metadata |
| `/environment` | Displays container environment information |
| `/uptime` | Returns application uptime since startup |

---

## Run Locally

```bash
docker build -t devops-system-api .
docker run -d -p 5000:5000 devops-system-api
```

Visit:

```
http://localhost:5000/
```

Example endpoints:

```
http://localhost:5000/health
http://localhost:5000/system
http://localhost:5000/app-info
http://localhost:5000/environment
http://localhost:5000/uptime
```

## Features

- Automated CI workflow using GitHub Actions
- Dockerized Flask application
- Automated Pytest execution
- Health check validation
- Secure Docker Hub authentication using GitHub Secrets
- Versioned Docker image publishing (`latest` and Git commit SHA)
