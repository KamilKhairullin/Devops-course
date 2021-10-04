"""This is implementation of web server that shows time in Moscow."""
from datetime import datetime, timedelta, timezone
from collections import deque
from flask import Flask, render_template

app = Flask(__name__)

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
    cur_time = datetime.now(tzinfo).strftime("%H:%M:%S")

    visits = []
    with open("visits.txt", "r", encoding="utf-8") as file:
            visits = file.readlines()
    visits = visits[:100]
    visits.insert(0, str(cur_time)+' ')
    with open("visits.txt", "w", encoding="utf-8") as file:
        file.writelines(visits)
      
    return render_template(
        "index.html", datetime=cur_time
    )

@app.route("/visits")
def visits():
    """Returns number of times root path was accessed

    Returns:
        int: number of times was accessed
    """
    visits = []
    with open("visits.txt", "r", encoding="utf-8") as file:
        visits = file.readlines()

    return str(visits)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
