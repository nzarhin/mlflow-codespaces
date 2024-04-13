# Use an official Python runtime as a parent image
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

RUN apt update
RUN apt install python3-pip -y
# Install PyTorch and MLflow
RUN pip install --no-cache mlflow==2.10.2

# Install ODBC Drivers for SQL on Debian 11
# https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=debian18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline
RUN curl https://packages.microsoft.com/config/debian/11/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools18
RUN apt-get install -y unixodbc-dev libgssapi-krb5-2

USER vscode

RUN mkdir -p ~/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-py311_24.1.2-0-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
    rm -rf ~/miniconda3/miniconda.sh && \
    ~/miniconda3/bin/conda init bash

# Fix issue #1 for non-login shells
RUN    echo 'export PATH="/usr/local/python/current/bin:/usr/local/py-utils/bin:/usr/local/share/nvm/current/bin:/usr/local/bin:$PATH"' >> ~/.bashrc
