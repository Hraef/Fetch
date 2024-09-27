# Fetch Health Checker

## Overview

The Fetch Health Checker is a Python application that continuously monitors the health of specified endpoints defined in a YAML configuration file. It checks the availability and response times of the endpoints at regular intervals, logging the results to the console.

## Features

- Load endpoint configurations from a YAML file.
- Perform health checks at configurable intervals.
- Log the availability percentage of each endpoint.
- Print status and latency for each endpoint.
- Logs overall result for each endpoint

## Requirements

- Python 3.9 or higher
- `requests` library
- `PyYAML` library

## Installation

1. **Clone the repository:**

  ```bash
  git clone <repository-url>
  cd <repository-directory>
  ```
2. **Install requirements:**
  ```python
  pip install -r requirements.txt
  ```
3. **Run program**:
  ```python
  python fetch.py /path/to/your/yaml_file.yaml
  ```

## Note:

If your yaml file is in the same directory then you can declare like this:
   
    ```python
      python fetch.py ./demo.yaml
    ```

To end the program press:
    
    **Ctrl+C**