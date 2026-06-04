CI/CD Pipeline with GitHub Actions & Docker

This repository demonstrates a basic CI/CD pipeline using GitHub Actions to automate testing, building, and deploying a Dockerized Python application.

Overview

The pipeline performs the following steps:

Trigger on push to main branch or manual dispatch
Checkout repository code
Build a Docker image
Run tests inside the container using pytest
Authenticate with Docker Hub
Push the Docker image to Docker Hub

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/3ac9a1dd-2dfb-4f63-a906-559170904a49" />

## Run Locally

docker build -t myapp .

docker run myapp


#Workflow Trigger

The GitHub Actions workflow executes automatically when code is pushed to the 'main' branch.
