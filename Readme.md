# Movieshop FastAPI Application (Without DB) Documentation

## Overview

This project is a FastAPI application named **MovieshopFastAPIwithoutDB**. It runs inside a Docker container, allowing you to quickly set up and run the application in any environment that supports Docker.

### Features:
- **FastAPI** framework for building APIs.
- Runs in a **Docker container** for ease of deployment.
- The application exposes **port 8000** for external access.

## Prerequisites

Ensure the following are installed on your system before proceeding:

- [Docker](https://www.docker.com/get-started)
- [Python 3.12.7](https://www.python.org/downloads/release/python-3127/)

## Project Structure

The project directory should have the following files and structure:

```
MovieshopFastAPIwithoutDB/
├── Dockerfile
├── main.py
├── requirements.txt
├── other_project_files
```

- **main.py**: The FastAPI application entry point.
- **requirements.txt**: Contains the necessary Python packages.
- **Dockerfile**: The file that defines the Docker image setup.

## Dockerfile

Below is the content of the `Dockerfile`:

```Dockerfile
FROM python:3.12.7
LABEL author="Manoj" application="MovieshopFastAPIwithoutDB"
COPY . /MovieshopFastAPIwithoutDB
WORKDIR /MovieshopFastAPIwithoutDB
EXPOSE 8000
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### Dockerfile Breakdown:
- **FROM**: Uses the official Python 3.12.7 image as the base image.
- **LABEL**: Adds metadata to the image (author name and application name).
- **COPY**: Copies the project files into the container.
- **WORKDIR**: Sets the working directory inside the container.
- **EXPOSE**: Opens port 8000 to allow external access.
- **RUN**: Installs the required dependencies from `requirements.txt`.
- **CMD**: Starts the FastAPI application using `uvicorn`.

## How to Build and Run the Docker Image

### Step 1: Clone the Repository
Clone the project repository to your local machine:

```bash
git clone <repository-url>
cd MovieshopFastAPIwithoutDB
```

### Step 2: Build the Docker Image
Run the following command to build the Docker image:

```bash
docker build -t movieshop-fastapi-app .
```

### Step 3: Run the Docker Container
Once the image is built, you can start the container using:

```bash
docker run -d -p 8000:8000 movieshop-fastapi-app
```

### Step 4: Access the Application
You can now access the FastAPI application in your browser or via curl:

```bash
http://localhost:8000
```

## Stopping the Container

To stop the running container, use the following command:

```bash
docker stop <container-id>
```

You can find the container ID using:

```bash
docker ps
```

## Troubleshooting

- **Dependency Issues**: Ensure all required packages are listed in `requirements.txt`.
- **Port Conflicts**: Ensure port 8000 is not being used by another application.
- **Docker Not Installed**: Ensure Docker is installed and running on your system.

## Author

This project was developed by **Manoj**.