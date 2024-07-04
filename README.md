# Project Name

## Description
Brief description of what the project does.

## Table of Contents
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Building Docker Images](#building-docker-images)
- [Puing Docker Images](#puing-docker-images)
- [Kubernetes Setup](#kubernetes-setup)
- [Deploying the Application](#deploying-the-application)
- [Setting Up Secrets](#setting-up-secrets)
- [Usage](#usage)
- [License](#license)

## Project Structure
projectname/
├── backend/
│ ├── app.py # Main application file for backend
│ ├── requirements.txt # List of dependencies for backend
│ ├── Dockerfile # Dockerfile for backend
│ ├── backend-service.yaml # Kubernetes service configuration for backend
│ └── deployment.yaml # Kubernetes deployment configuration for backend
├── frontend/
│ ├── templates/
│ │ └── index.html # Main HTML template
│ ├── Dockerfile # Dockerfile for frontend
│ ├── deployment.yaml # Kubernetes deployment configuration for frontend
│ └── frontend-service.yaml # Kubernetes service configuration for frontend
├── README.md # Project README file
└── LICENSE # Project license file



## Prerequisites
- Git
- Docker
- Kubernetes
- Google Cloud SDK

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd projectname
Building Docker Images

# Backend:

cd backend
Build the Docker image:

docker build -t backend:latest .

# Frontend:

cd frontend
Build the Docker image:docker build -t frontend:latest .

# Puing Docker Images and Tag the Docker images:

docker tag frontend:latest gcr.io/mounika8036-426015/frontend:latest
docker tag backend:latest gcr.io/mounika8036-426015/backend:latest

# Pu the Docker images to your repository:

docker pu gcr.io/mounika8036-426015/frontend:latest
docker pu gcr.io/mounika8036-426015/backend:latest

#Kubernetes Setup
#Create the Kubernetes cluster:
gcloud container clusters create mycluster --zone us-central1 --cluster-version 1.28.9-gke.1000000 --machine-type e2-micro --num-nodes 1 --disk-type=pd-standard

# Resize the Kubernetes cluster:
gcloud container clusters resize mycluster --node-pool default-pool --num-nodes=3 --zone us-central1-a

# Get cluster credentials:
gcloud container clusters get-credentials mycluster --region us-central1-a

# Namespaces
Create namespaces for frontend and backend:
kubectl create namespace frontend
kubectl create namespace backend

#Setting Up Secrets
Create secrets for the backend:
kubectl create secret generic db-credentials --from-literal=DB_NAME=myappdb --from-literal=DB_USER=myuser --from-literal=DB_PASSWORD=admin123 --from-literal=DB_HOST=34.23.231.65 --namespace=backend

#Create Docker registry secret for the frontend:
kubectl create secret docker-registry regcred --docker-server=gcr.io --docker-username=_json_key --docker-password="$(cat mounika8036-426015-b4fef215183c.json)" --docker-email=deva.jal369@gmail.com --namespace=frontend

#Deploying the Application
 Backend
 Apply the backend Kubernetes configurations:
 cd backend
 kubectl apply -f backend-service.yaml
 kubectl apply -f deployment.yaml

 Frontend
 Apply the frontend Kubernetes configurations:
 cd frontend
 kubectl apply -f deployment.yaml
 kubectl apply -f frontend-service.yaml

#Usage
Check the services:
kubectl get services -n backend
kubectl get services -n frontend
Access the frontend application through the service URL.
Enter data in the HTML frontend page.
The data will be stored in the PostgreSQL database accessed by the backend.