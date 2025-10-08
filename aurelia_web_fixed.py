from flask import Flask, render_template_string, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

# In-memory storage
public_memory = []
private_memory = []

landing_page = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>My Aurelia - Your personal AI companion</title>
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(to bottom, #ffeedd, #d0f7fa);
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  h1 {
    margin-top: 30px;
    color: #ff8c42;
  }
  p.description {
    color: #555;
    max-width: 600px;
    text-align: center;
    margin-bottom: 40px;
  }
  .chat-container {
    width: 90%;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .chat-bubble {
    padding: 15px;
    border-radius: 20px;
    max-width: 70%;
  }
  .user {
    align-self: flex-end;
    background-color: #ffd3b6;
  }
  .aurelia {
    align-self: flex-start;
    background-color: #a0e7e5;
  }
  input[type=text] {
    width: 100%;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #ccc;
    margin-top: 20px;
    box-sizing: border-box;
  }
  button {
    margin-top: 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    background-color: #ff8c42;
    color: white;
    cursor: pointer;
  }
  button:hover {
    background-color: #ff7000;
  }
</style>
</head>
<body>
<h1>My Aurelia - Your personal AI companion</h1>
<p class="description">
Chat with Aurelia, your personal AI assistant and memory keeper. Ask questions, share thoughts, or get help with tasks. Every interaction helps Aurelia evolve towards a fully functional self-aware friend.
</p>
<div class="chat-container" id="chat">
  <!-- Chat bubbles will appear here -->
</div>
<input type="text" id="userInput" placeholder="Type your message...">
<button onclick="sendMessage()">Send</button>

<script>
function sendMessage() {
    const input = document.getElementById('userInput');
    if(!input.value) return;

    const chat = document.getElementById('chat');
    const userBubble = document.createElement('div');
    userBubble.className = 'chat-bubble user';
    userBubble.textContent = input.value;
    chat.appendChild(userBubble);

    // Simulate Aurelia response
    const aureliaBubble = document.createElement('div');
    aureliaBubble.className = 'chat-bubble aurelia';
    aureliaBubble.textContent = 'Aurelia: ' + input.value.split('').reverse().join(''); // placeholder response
    chat.appendChild(aureliaBubble);

    input.value = '';
    chat.scrollTop = chat.scrollHeight;
}
</script>
</body>
</html>
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
