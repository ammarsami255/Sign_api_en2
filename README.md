# Sign Language Recognition API

This API uses computer vision and machine learning to recognize sign language gestures from video input. It processes videos frame by frame, detects hand landmarks using MediaPipe, and predicts the corresponding sign language character.

## Features

- Video-based sign language recognition
- Supports American Sign Language (ASL) alphabet and numbers 0-9
- RESTful API for easy integration

## API Endpoints

- `GET /`: API status and available endpoints
- `POST /predict_video_batch`: Upload a video file for sign language recognition
  - Returns filtered predictions with consecutive duplicates removed
  - Also provides raw predictions with all detected signs
- `GET /health`: Health check endpoint to verify the API is running properly
  - Returns a JSON response with status "healthy" and HTTP 200 OK
  - Useful for monitoring services and deployment health checks

For detailed API documentation, see [API_DOCUMENTATION.md](API_DOCUMENTATION.md).

## Deployment on Render

Follow these steps to deploy this API on Render:

1. Create a new account on [Render](https://render.com/) if you don't have one
2. Click on "New" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service with the following settings:
   - **Name**: Choose a name for your service
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn api:app`
5. Click "Create Web Service"

Render will automatically deploy your application and provide you with a URL to access it.

**Important Note**: Make sure the Start Command is exactly `gunicorn api:app` (not `app:app`). The error "No module named 'app'" indicates that Render might be trying to use `app:app` instead of the correct module name.

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python api.py`
4. The API will be available at `http://localhost:5000`

## Testing the API

You can use the included `request.py` script to test the API locally:

```bash
# Basic usage with default videos
python request.py

# Test with specific videos
python request.py --videos video1.mp4 video2.mp4

# Show raw predictions (with repeats)
python request.py --show_raw

# Test against deployed API
python request.py --api_url https://your-render-url.onrender.com/predict_video_batch
```

The script provides the following command-line options:
- `--api_url`: Specify the API endpoint URL
- `--videos`: List of video files to process
- `--show_raw`: Show raw predictions with repeats