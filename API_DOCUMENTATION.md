# Sign Language API Documentation

## Base URL

All API endpoints are relative to the base URL of your deployment:

```
https://your-api-url.onrender.com
```

For local development:

```
http://localhost:5000
```

## Endpoints

### Endpoint: /
Method: GET
Description: Returns API status and available endpoints

Response:
```json
{
  "status": "Sign Language API is running",
  "endpoints": ["/predict_video_batch", "/health"]
}
```

### Endpoint: /health
Method: GET
Description: Health check endpoint to verify the API is running properly

Response:
```json
{
  "status": "healthy"
}
```

### Endpoint: /predict_video_batch
Method: POST
Description: Uploads a video file and returns predictions of sign language characters

Headers:
- Content-Type: multipart/form-data

Request Body:
- video: File (Required) - The video file containing sign language gestures

Response:
```json
{
  "predictions": ["A", "B", "C"],
  "raw_predictions": ["A", "A", "A", "B", "B", "C", "C", "C"]
}
```

Response Fields:
- predictions: array of strings
  - Filtered sign language characters with consecutive duplicates removed
  - Each character represents a detected sign (A-Z, 0-9)

- raw_predictions: array of strings
  - All raw predictions from each frame where a hand was detected
  - Includes consecutive duplicates

Error Responses:

1. No video file provided:
```json
{
  "error": "No video file provided"
}
```
Status Code: 400

2. Empty video filename:
```json
{
  "error": "No selected video"
}
```
Status Code: 400

## Example Usage

### Using cURL

```bash
curl -X POST -F "video=@path/to/your/video.mp4" https://your-api-url.onrender.com/predict_video_batch
```

### Using Python Requests

```python
import requests

url = "https://your-api-url.onrender.com/predict_video_batch"
files = {"video": open("path/to/your/video.mp4", "rb")}

response = requests.post(url, files=files)
data = response.json()

print("Filtered predictions:", data["predictions"])
print("Raw predictions:", data["raw_predictions"])
```

## Notes

- The API supports videos containing American Sign Language (ASL) alphabet signs (A-Z) and numbers (0-9)
- For optimal recognition, ensure good lighting and a clear view of hand gestures
- The API processes videos frame by frame and may take longer for larger video files
- Consecutive duplicate predictions are automatically filtered out in the "predictions" field
- Raw predictions with duplicates are available in the "raw_predictions" field