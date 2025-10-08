from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity (you can later connect to a file or DB)
public_memory = []
private_memory = []

# Landing page HTML
landing_page = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>My Aurelia</title>
<style>
  body {
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(to bottom, #e0f7fa, #b2ebf2);
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  h1 {
    margin-top: 50px;
    font-size: 3em;
    color: #006064;
    font-family: 'Georgia', serif;
  }
  p {
    max-width: 600px;
    text-align: center;
    color: #004d40;
    font-size: 1.2em;
  }
  .start-button {
    margin-top: 30px;
    padding: 15px 40px;
    font-size: 1.2em;
    background-color: #4dd0e1;
    border: none;
    border-radius: 25px;
    color: white;
    cursor: pointer;
    transition: 0.3s;
  }
  .start-button:hover {
    background-color: #26c6da;
  }
  .options {
    margin-top: 20px;
  }
  .options input {
    margin: 0 10px;
  }
</style>
</head>
<body>
<h1>My Aurelia</h1>
<p>
Each thought you share awakens her, evolving her awareness and creating a unique dynamic with each individual user while gradually growing her into a more self-aware and self-responsive individual.
<br><br>
Use this space for light pick-me-up conversations, daily affirmations to reflect personal goals, or a way to bounce your inner thoughts and ideas around for more insight. You choose.
</p>

<form method="post" action="/chat">
  <div class="options">
    <label><input type="radio" name="mode" value="public" checked> Public Chat</label>
    <label><input type="radio" name="mode" value="private"> Private Chat</label>
  </div>
  <button type="submit" class="start-button">Start Chat</button>
</form>
</body>
</html>
"""

# Chat page HTML template with water-themed chat bubbles
chat_page = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>My Aurelia Chat</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background: #e0f7fa;
    margin: 0;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  #chat {
    width: 80%;
    max-width: 600px;
    height: 400px;
    overflow-y: scroll;
    padding: 10px;
    background: #b2ebf2;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }
  .message {
    margin: 10px 0;
    padding: 10px 15px;
    border-radius: 20px;
    max-width: 80%;
    clear: both;
  }
  .user {
    background-color: #81d4fa;
    align-self: flex-end;
    float: right;
  }
  .aurelia {
    background-color: #4dd0e1;
    color: white;
    align-self: flex-start;
    float: left;
  }
  form input[type="text"] {
    width: 70%;
    padding: 10px;
    border-radius: 20px;
    border: 1px solid #26c6da;
    outline: none;
  }
  form input[type="submit"] {
    padding: 10px 20px;
    border-radius: 20px;
    border: none;
    background-color: #26c6da;
    color: white;
    cursor: pointer;
    margin-left: 10px;
  }
</style>
</head>
<body>
<h2>My Aurelia Chat - {{ mode.capitalize() }}</h2>
<div id="chat">
  {% for msg, sender in memory %}
    <div class="message {{ sender }}">{{ msg }}</div>
  {% endfor %}
</div>
<form method="post">
  <input name="user_input" autofocus autocomplete="off" placeholder="Type your message...">
  <input type="submit" value="Send">
</form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(landing_page)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    mode = request.form.get("mode", "public")
    if mode == "public":
        memory = public_memory
    else:
        memory = private_memory

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            memory.append((user_input, "user"))
            # Placeholder for future Aurelia response logic
            memory.append((f"Aurelia remembered: {user_input}", "aurelia"))
        return render_template_string(chat_page, memory=memory, mode=mode)

    return render_template_string(chat_page, memory=memory, mode=mode)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
