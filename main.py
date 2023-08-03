from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

def download_video(link):
    try:
        youtube_object = YouTube(link)
        video_stream = youtube_object.streams.get_highest_resolution()
        
        video_stream.download()
        
        return True, youtube_object.title
    except Exception as e:
        return False, str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_link = request.form['video_link']
        success, message = download_video(video_link)
        if success:
            return render_template('index.html', message=f"Downloaded: {message}")
        else:
            return render_template('index.html', message=f"Error: {message}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
