import requests
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def send_video_and_get_predictions(video_path):
    url = 'http://127.0.0.1:5000/predict_video_batch'
    with open(video_path, 'rb') as f:
        files = {'video': (video_path, f, 'video/mp4')}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            print("Predictions:", response.json()['predictions'])
        else:
            print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    send_video_and_get_predictions('a.mp4')
    send_video_and_get_predictions('b.mp4')
    send_video_and_get_predictions('c.mp4')
