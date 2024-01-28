document.getElementById('sendButton').addEventListener('click', function() {
    var userInput = document.getElementById('userInput').value;
    var messages = document.getElementById('messages');

    // Append user's message to the chat
    messages.innerHTML += '<p>You: ' + userInput + '</p>';

    // Send POST request
    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({input: userInput}),
    })
    .then(response => response.json())
    .then(data => {
        // Append server's response to the chat
        messages.innerHTML += '<p>Server: ' + data.response + '</p>';
    });

    // Clear the input field
    document.getElementById('userInput').value = '';
});