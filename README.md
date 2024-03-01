# MLFlow with GitHub Codespaces

## Requirements
- GitHub account
- Visual Studio Code

## Starter Usage:

As a starter use case, you can use Codespaces as a remote compute environment however the experience will feel as if it were local.

### Commands

In a terminal:
```bash
# Start MLFlow UI/Server with default settings set to local by default
mlflow ui
```

In a second terminal:
```bash
# You will need to specify your MLFlow Tracking Server URI/URL
# Since this is "local" you won't need to setup HTTPS

export MLFLOW_TRACKING_URI="http://127.0.0.1:5000"

# mlflow run <mlflow project path/uri>
# example:
mlflow run https://github.com/mlflow/mlflow-example.git
```

## Open MLFlow Web UI Locally

Your VS Code instance is remotely connected to the GitHub Codespaces instance.  The devcontainer has already been preconfigured to port-forward the Codespaces' "local" port of :5000 to your (actual) local machine (laptop/desktop) to an automatically assigned port (e.g. :63801).  To find this and to manually launch your default browser you can find the "PORTS" tab in VS Code (typically found above the terminal prompt in VS Code - See screenshot below).  Beside the listed PORT Mapping (e.g. 5000) you will also see a small globe icon which will help auto launch your default web browser and load the MLFlow web UI.

![Open Remote MLFlow UI](img/open-ui.png)
