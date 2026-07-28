# Emotion Detector

This is my final project for the Python AI application course. The app takes a short piece of text and uses the Watson NLP emotion service to check the emotion behind it.

It returns scores for anger, disgust, fear, joy and sadness, then shows which one is the dominant emotion.

## Project files

- `EmotionDetection/emotion_detection.py` contains the emotion detection function
- `EmotionDetection/test_emotion_detection.py` contains the unit tests
- `server.py` runs the Flask web application
- `templates/index.html` contains the page layout
- `static/mywebscript.js` sends the text to the Flask route

## Running the application

Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the tests:

```bash
python3 -m unittest EmotionDetection/test_emotion_detection.py -v
```

Start the Flask application:

```bash
python3 server.py
```

The application runs on port `5000`.
