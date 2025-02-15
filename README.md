# MarkItDown API

A FastAPI-based API service that converts documents to Markdown format using the [MarkItDown](https://pypi.org/project/markitdown/#description) package.

## Prerequisites

- Python 3.13 or higher
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) package manager

## Installation

Create a virtual environment and install dependencies:

```bash
uv venv
source .venv/bin/activate  # On macOS/Linux
uv sync
```

## Running the Server

Start the development server:
```bash
uv run -- fastapi dev main.py
```

The server will be available at `http://localhost:8000`

## API Usage

### Upload and Convert File
- **Endpoint**: `POST /convert`
- **Method**: POST
- **Content-Type**: `multipart/form-data`
- **Request Body**: File upload with field name `file`

You can test the API using the web interface at `http://localhost:8000` or using curl:

```bash
curl -X POST -F "file=@your_file.docx" http://localhost:8000/convert
```
