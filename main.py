from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import base64

app = FastAPI()

# Sample data for email and roll number (to keep things simple)
user_info = {
    "email": "john@xyz.com",
    "roll_number": "ABCD123"
}

class DataInput(BaseModel):
    data: List[str]
    file_b64: Optional[str] = None  # File in base64 is optional

def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase = None

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                if not highest_lowercase or item > highest_lowercase:
                    highest_lowercase = item

    return numbers, alphabets, highest_lowercase

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}

@app.post("/bfhl")
async def post_bfhl(data_input: DataInput):
    data = data_input.data
    user_id = "john_doe_17091999"
    numbers, alphabets, highest_lowercase = process_data(data)
    
    # File validation logic
    file_valid = False
    file_mime_type = None
    file_size_kb = None
    
    if data_input.file_b64:
        try:
            file_bytes = base64.b64decode(data_input.file_b64)
            file_valid = True
            file_size_kb = len(file_bytes) / 1024  # Convert size to KB
            file_mime_type = "image/png"  # You can set up a function to validate MIME type if needed
        except Exception as e:
            file_valid = False

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": user_info["email"],
        "roll_number": user_info["roll_number"],
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": f"{file_size_kb:.2f}" if file_size_kb else None
    }

    return response
