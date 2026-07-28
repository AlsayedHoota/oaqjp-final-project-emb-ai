# Emotion Detector

This is my final project for the Python AI application course. The app takes a short piece of text and uses the Watson NLP emotion service to check the emotion behind it.

It returns scores for anger, disgust, fear, joy and sadness, then shows which one is the dominant emotion.

## Project files

- `EmotionDetection/emotion_detection.py` contains the emotion detection function
- `EmotionDetection/__init__.py` exposes the function so the folder works as a package
- `test_emotion_detection.py` contains the unit tests
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
python3 test_emotion_detection.py
```

Start the Flask application:

```bash
python3 server.py
```

The application runs on port `5000`.

Run the static code analysis:

```bash
pylint server.py
```

## Note on the Watson NLP service

The emotion service at `sn-watson-emotion.labs.skills.network` is an embedded
Watson NLP instance that is only reachable from inside the Skills Network Cloud
IDE. Running the tests or the web application from another network will fail to
connect to it.
