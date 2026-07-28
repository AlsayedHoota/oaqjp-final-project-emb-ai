function RunSentimentAnalysis() {
    const text = document.getElementById("textToAnalyze").value;
    fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(text))
        .then(response => response.text())
        .then(data => {
            document.getElementById("system_response").innerHTML = data;
        });
}
