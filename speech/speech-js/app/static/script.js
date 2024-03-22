document.addEventListener("DOMContentLoaded", function() {
    const startBtn = document.getElementById("startBtn");
    const resultDiv = document.getElementById("result");

    // Function to handle speech recognition
    function startRecognition() {
        const recognition = new webkitSpeechRecognition(); // Create speech recognition object

        // Configure recognition settings
        recognition.lang = 'ta-IN'; // Set language to Tamil
        recognition.continuous = false; // Recognize speech continuously
        recognition.interimResults = false; // Do not return interim results

        // Start recognition when button is clicked
        recognition.start();

        // Event listener for when speech recognition is complete
        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript; // Get the recognized speech
            resultDiv.innerHTML = "<p>Recognized Speech:</p><p>" + transcript + "</p>"; // Display the recognized speech
        };

        // Event listener for error handling
        recognition.onerror = function(event) {
            resultDiv.innerHTML = "<p>Error occurred: " + event.error + "</p>"; // Display error message
        };
    }

    // Event listener for button click to start speech recognition
    startBtn.addEventListener("click", function() {
        startRecognition();
    });
});
