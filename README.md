# Emotion Detector

This is my final project for the Python AI application course. It uses the Watson NLP emotion service to analyse a sentence and return scores for anger, disgust, fear, joy and sadness.

The result also shows the dominant emotion.

## Running the project

Install the requirements:

```bash
python3 -m pip install -r requirements.txt
```

Run the unit tests:

```bash
python3 test_emotion_detection.py
```

Start the Flask app:

```bash
python3 server.py
```

The app runs on port `5000`. The Watson service is available from the Skills Network lab environment.

To check the code quality, run:

```bash
pylint server.py
```
