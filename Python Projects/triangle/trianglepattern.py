from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    rows = int(request.args.get("rows", 5))

    pattern = ""
    for i in range(1, rows + 1):
        "" * (rows - i) + "* " * i
        pattern += "" * (rows - i) + "* " * i + "<br>"

    return f"""
        <form action="/" method="get">
            <label for="rows">Number of rows:</label>
            <input type="number" id="rows" name="rows" min="1" value="{rows}">
            <button type="submit">Generate</button>
        </form>
        <div style="fnt-family: monospace;">
            {pattern}
        </div>
    """    