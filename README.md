# Project 05 - Cloud Build CI/CD Pipeline

## Overview

This project demonstrates how to automate application deployment using Google Cloud Build and Cloud Run. Instead of manually building and deploying the application after every code change, Cloud Build executes a predefined pipeline that builds a Docker image and deploys it to Cloud Run.

---

## Objectives

- Build a containerized Flask application.
- Automate application deployment using Cloud Build.
- Deploy the application to Cloud Run.
- Understand the principles of Continuous Integration and Continuous Deployment (CI/CD).

---

## Technologies Used

- Google Cloud Platform (GCP)
- Cloud Build
- Cloud Run
- Docker
- Python
- Flask
- YAML

---

## Project Architecture

```
Developer
     │
     ▼
Source Code
     │
     ▼
Cloud Build
     │
     ▼
Docker Image
     │
     ▼
Cloud Run
     │
     ▼
Users
```

---

## Repository Structure

```
05-cloud-build-cicd/
│── app.py
│── Dockerfile
│── requirements.txt
│── cloudbuild.yaml
│── README.md
└── screenshots/
    ├── build-success.png
    ├── cloud-build-history.png
    └── cloud-run-service.png
```

---

## Files

- **app.py** – Flask web application.
- **Dockerfile** – Defines how the application is containerized.
- **requirements.txt** – Python dependencies.
- **cloudbuild.yaml** – Cloud Build pipeline configuration.

---

## Deployment Process

1. Create the Flask application.
2. Create the Dockerfile.
3. Define the Cloud Build pipeline in `cloudbuild.yaml`.
4. Execute the Cloud Build pipeline.
5. Cloud Build builds the Docker image.
6. Cloud Build deploys the image to Cloud Run.
7. Cloud Run creates a new service revision.

---

## Skills Demonstrated

- Cloud Build
- Cloud Run
- CI/CD Pipeline
- Docker Containerization
- Python Flask
- YAML Configuration
- Google Cloud Platform

---

## Key Lessons Learned

- CI/CD automates software deployment.
- Cloud Build executes deployment steps defined in a YAML configuration file.
- Cloud Run enables serverless container deployment.
- Automation reduces manual deployment effort and improves consistency.

---

## Real-World Use Case

Organizations use Cloud Build to automatically build, test, and deploy applications whenever developers push new code to a source code repository. This enables faster and more reliable software delivery while minimizing manual deployment tasks.

---

## Project Notes

The Cloud Build pipeline completed successfully and the application was deployed to Cloud Run.

The Cloud Run service returned **403 Forbidden** because the Google Cloud Skills Boost lab environment restricted the IAM policy required to make the service publicly accessible. Despite this limitation, the deployment pipeline executed successfully and demonstrated the complete CI/CD workflow.

---

## Screenshots

- Build Success
- Cloud Build History
- Cloud Run Service
