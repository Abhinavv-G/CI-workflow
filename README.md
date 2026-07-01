# Continuous Integration Pipeline with GitHub Actions

Automated Continuous Integration (CI) pipeline that builds, tests, validates, and publishes a Dockerized Flask-based System Diagnostics API to Docker Hub on every push to the `main` branch.

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

- GitHub Actions
- Docker
- Docker Hub
- Python
- Flask
- Pytest

---

## Pipeline Workflow

- Triggers automatically on every push to the `main` branch or via manual workflow dispatch.
- Checks out the latest repository source code.
- Builds a Docker image tagged with the Git commit SHA.
- Executes the Pytest test suite inside the Docker container.
- Starts the container and validates the `/health` endpoint.
- Authenticates securely with Docker Hub using GitHub Secrets.
- Publishes Docker images tagged as both `latest` and the Git commit SHA.

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Returns application status |
| `/health` | Health check endpoint |
| `/system` | Returns operating system and runtime information |
| `/app-info` | Returns application metadata |
| `/environment` | Displays selected environment information |
| `/uptime` | Returns application uptime |

---

## Run Locally

```bash
docker build -t devops-system-api .
docker run -p 5000:5000 devops-system-api
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
