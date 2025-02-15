import os
from fastapi import FastAPI, HTTPException, UploadFile
from markitdown import MarkItDown
from fastapi.responses import HTMLResponse
from tempfile import TemporaryDirectory

app = FastAPI()

# Create MarkItDown instance
converter = MarkItDown()

@app.get("/")
async def main():
    content = """
        <body>
        <form action="/convert" enctype="multipart/form-data" method="post">
        <input name="file" type="file" multiple>
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)


@app.post("/convert")
async def convert_to_markdown(file: UploadFile):
    with TemporaryDirectory() as temp_dir:
        try:
            # Create temp file path
            temp_file_path = os.path.join(temp_dir, file.filename)

            # Save uploaded file
            with open(temp_file_path, "wb") as f:
                contents = await file.read()
                f.write(contents)

            # Convert using file path
            markdown_content = converter.convert(temp_file_path)

            # Use FileResponse with background task to cleanup after response is sent
            return markdown_content.text_content
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
