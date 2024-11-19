
# Assignment 3

## Overview
This project demonstrates the use of **Docker Compose** to deploy a scalable application consisting of multiple web services and a load balancer. The setup uses the following components:
- **Web Services**: Two identical services running a Python-based application, each configured to handle incoming requests.
- **Load Balancer**: An Nginx load balancer to distribute traffic between the web services.
- **Configuration Management**: A shared configuration file is mounted into each service.

## Requirements
- Docker
- Docker Compose

## Project Structure
```
project/
│
├── Dockerfile1          # Dockerfile for web services
├── Dockerfile2          # Dockerfile for the load balancer 
├── docker-compose.yml   # Docker Compose configuration file
├── web-service/         # Web service directory
│   ├── app.py           # Python application
│   └── config.txt       # Shared configuration file
├── nginx.conf           # Configuration file for Nginx load balancer

```

## Getting Started
1. Clone the repository.
2. Navigate to the project directory:
   ```bash
   cd advance-containers
   ```

3. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

## Usage
- Access the load balancer at:
  ```
  http://localhost:80
  ```
- Access individual web services (for testing) at:
  ```
  http://localhost:5001
  http://localhost:5002
  ```

## Scaling
Scale the number of replicas for the web service using the following command:
```bash
docker-compose up --scale web_service=3
```

## Stopping the Services
To stop and remove the containers, networks, and volumes created by Docker Compose:
```bash
docker-compose down
```
