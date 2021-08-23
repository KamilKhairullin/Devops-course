"""This is implementation of web server that shows time in Moscow."""
from datetime import datetime, timedelta, timezone

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
    return render_template(
        "index.html", datetime=datetime.now(tzinfo).strftime("%H:%M:%S")
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
