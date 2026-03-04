# 🚀 Kubernetes Greeting App

A simple **FastAPI** web application containerized with **Docker** and deployed on **Kubernetes**. The app serves an interactive greeting page where users enter their name and receive a personalized welcome message.

---

## 📁 Project Structure

```
K8s-project/
├── app.py              # FastAPI backend application
├── index.html          # Frontend UI (served by FastAPI)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image definition
├── deployment.yaml     # Kubernetes Deployment & Service manifest
└── README.md           # Project documentation
```

---

## 🧰 Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Backend     | FastAPI + Uvicorn |
| Frontend    | HTML / CSS / JS   |
| Container   | Docker            |
| Orchestration | Kubernetes      |

---

## ✨ Features

- **GET /** — Serves the interactive greeting HTML frontend
- **GET /greet/{name}** — Returns a personalized JSON greeting:
  ```json
  { "greeting": "Hello John, welcome to Kubernetes!" }
  ```
- **2 Replicas** for high availability
- **Resource limits & requests** to prevent noisy-neighbor issues
- **Liveness & Readiness probes** for health monitoring
- **NodePort Service** to expose the app externally

---

## 🛠️ Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/) (or any Kubernetes cluster)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MudassarGill/K8s-project.git
cd K8s-project
```

### 2. Build the Docker Image

> ⚠️ If using Minikube, point your Docker CLI to Minikube's Docker daemon first:
> ```bash
> eval $(minikube docker-env)       # Linux/macOS
> minikube docker-env | Invoke-Expression  # Windows PowerShell
> ```

```bash
docker build -t greeting-app:latest .
```

### 3. Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
```

### 4. Verify the Deployment

```bash
# Check pods are running
kubectl get pods

# Check the service
kubectl get services
```

### 5. Access the App

```bash
minikube service greeting-app-service
```

This will open the app in your browser automatically. You can also get the URL with:

```bash
minikube service greeting-app-service --url
```

---

## ⚙️ Kubernetes Configuration Details

### Deployment

| Setting             | Value         |
|---------------------|---------------|
| Replicas            | 2             |
| Container Port      | 8000          |
| Image Pull Policy   | Never (local) |

### Resource Limits

| Resource | Request | Limit  |
|----------|---------|--------|
| CPU      | 100m    | 500m   |
| Memory   | 128Mi   | 256Mi  |

### Health Probes

| Probe     | Path | Port | Initial Delay | Period |
|-----------|------|------|---------------|--------|
| Liveness  | `/`  | 8000 | 5s            | 10s    |
| Readiness | `/`  | 8000 | 3s            | 5s     |

### Service

| Setting     | Value     |
|-------------|-----------|
| Type        | NodePort  |
| Port        | 80        |
| Target Port | 8000      |

---

## 🧹 Clean Up

To delete all created resources from the cluster:

```bash
kubectl delete -f deployment.yaml
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
