import requests
import warnings
import argparse
warnings.filterwarnings("ignore", category=UserWarning)

def send_video_and_get_predictions(video_path, api_url, show_raw=False):
    with open(video_path, 'rb') as f:
        files = {'video': (video_path, f, 'video/mp4')}
        response = requests.post(api_url, files=files)

        if response.status_code == 200:
            data = response.json()
            print(f"Video: {video_path}")
            print("Filtered Predictions (no repeats):", data['predictions'])
            if show_raw:
                print("Raw Predictions (with repeats):", data['raw_predictions'])
            print("-" * 50)
        else:
            print(f"Error for {video_path}:", response.status_code, response.text)
            print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description='Test Sign Language Recognition API')
    parser.add_argument('--api_url', type=str, default="https://sign-api-en2.onrender.com/predict_video_batch",
                        help='API endpoint URL (default: https://sign-api-en2.onrender.com/predict_video_batch)')
    parser.add_argument('--videos', nargs='+', default=['a.mp4', 'b.mp4', 'c.mp4'],
                        help='List of video files to process')
    parser.add_argument('--show_raw', action='store_true',
                        help='Show raw predictions with repeats')
    
    args = parser.parse_args()
    
    print(f"Using API endpoint: {args.api_url}")
    print("Processing videos...")
    print("-" * 50)
    
    for video in args.videos:
        send_video_and_get_predictions(video, args.api_url, args.show_raw)

if __name__ == '__main__':
    main()
