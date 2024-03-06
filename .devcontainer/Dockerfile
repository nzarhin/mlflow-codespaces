# Use an official Python runtime as a parent image
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Install PyTorch and MLflow
RUN pip install --no-cache mlflow==2.10.2

USER vscode

RUN mkdir -p ~/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-py311_24.1.2-0-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
    rm -rf ~/miniconda3/miniconda.sh && \
    ~/miniconda3/bin/conda init bash
