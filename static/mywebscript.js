const RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const responseElement = document.getElementById("system_response");
    const request = new XMLHttpRequest();

    request.onreadystatechange = () => {
        if (request.readyState === XMLHttpRequest.DONE) {
            responseElement.textContent = request.status === 200
                ? request.responseText
                : "The analysis service is temporarily unavailable. Please try again.";
        }
    };
    request.open(
        "GET",
        `emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`,
        true
    );
    request.send();
};
