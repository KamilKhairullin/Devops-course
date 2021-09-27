"""This is implementation of web server that shows time in Moscow."""
from datetime import datetime, timedelta, timezone
from collections import deque
from flask import Flask, render_template

app = Flask(__name__)

visitors = deque([])

@app.route("/")
def time():
    """
    Gets current Moscow time and renders html template's
    datetime value

    Returns:
        render_template("index.html", datetime) : newly rendered html
    """
    timezone_offset = 3.0  # Moscow Standard Time (UTC+03:00)
    tzinfo = timezone(timedelta(hours=timezone_offset))
    time = datetime.now(tzinfo).strftime("%H:%M:%S")
    visitors.append(time)
    if len(visitors) > 10:
        visitors.popleft()
    
    return render_template(
        "index.html", datetime=time
    )

@app.route("/visits")
def visits():
    """Returns number of times root path was accessed

    Returns:
        int: number of times was accessed
    """
    ans = ""
    for visitor in visitors:
        ans = ans + str(visitor) + " \n"
    return ans


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
