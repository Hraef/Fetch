# Fetch Health Checker

## Overview

The Fetch Health Checker is a Python application that continuously monitors the health of specified endpoints defined in a YAML configuration file. It checks the availability and response times of the endpoints at regular intervals, logging the results to the console.

## Features

- Load endpoint configurations from a YAML file.
- Perform health checks at 15 second intervals.
- Log the availability percentage of each endpoint.
- Print status and latency for each endpoint.
- Logs overall result for each endpoint

## Requirements

- Python 3.9 or higher
- `requests` library
- `PyYAML` library

## Demo YAML Configuration

For a demonstration of the YAML file structure, please view the `demo.yaml` file in this repository. This file currently contains placeholders that you can replace with your own values or upload your own YAML file.

Ensure that your custom YAML file follows the same structure as the provided `demo.yaml`.

## Installation

1. **Clone the repository:**

  ```bash
  git clone <repository-url>
  cd <repository-directory>
  ```
2. **Setup virtual environment (Optional but recommended):**
  ```bash
  python -m venv venv
  ```
3. **Activate virtual environment**
- For Bash:
  ```bash
  source venv/scripts/activate
  ```
- For Windows (command prompt):
  ```cmd
  venv\Scripts\activate
  ```
- For Windows (powershell):
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
4. **Install requirements:**
  ```python
  pip install -r requirements.txt
  ```
5. **Run program**:
  ```python
  python fetch.py /path/to/your/yaml_file.yaml
  ```

## Note:

If your YAML file is in the same directory, you can run:
   
  ```python
    python fetch.py ./demo.yaml
  ```

To end the program press:
    
  Ctrl+C