from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn

memory_file = "aurelia_memory.txt"

def load_memory():
    try:
        with open(memory_file, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_memory(memories):
    with open(memory_file, "w") as f:
        f.write("\n".join(memories))

memories = load_memory()

app = FastAPI()

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Aurelia</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; }}
        .chat-box {{ border: 1px solid #ccc; padding: 20px; max-width: 600px; margin: auto; background: #fff; }}
        .memory {{ background: #eee; padding: 5px; margin: 5px 0; border-radius: 4px; }}
        input[type=text] {{ width: 80%; padding: 10px; margin-right: 10px; }}
        button {{ padding: 10px; }}
    </style>
</head>
<body>
    <div class="chat-box">
        <h2>Hello, Faith. Aurelia is ready.</h2>
        <form action="/chat" method="post">
            <input name="user_input" type="text" autofocus required>
            <button type="submit">Send</button>
        </form>
        <div>
            {memories_html}
        </div>
    </div>
</body>
</html>
"""

def render_memories():
    return "".join([f'<div class="memory">{m}</div>' for m in memories])

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE.format(memories_html=render_memories())

@app.post("/chat", response_class=HTMLResponse)
def chat(user_input: str = Form(...)):
    memories.append(user_input)
    save_memory(memories)
    return HTML_PAGE.format(memories_html=render_memories())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

