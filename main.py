"""
Main App file
"""
import csv
import io
import json
import os
import settings

from flask import Flask, render_template  # , request

# static files should really be handled by a web server...
app = Flask(__name__)  # , static_url_path='/assets')

@app.route("/")
def home():
    return render_template("index.html", test="variable")


def read_csv(filename):
    path = os.path.join(os.getcwd(), filename)
    with io.open(path, "r", encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
        data = [row for row in reader]
        return data


@app.route("/data/<file_constant>")
def get_data(file_constant):
    """
    Ajax entry endpoint for csv data
    TODO gate this?
    """
    try:
        filename = getattr(settings, file_constant)

    except AttributeError:
        return app.response_class(
            response="Invalid file name",
            status=404,
            mimetype="application/json",
        )

    data = read_csv(filename)
    return json.dumps(data)
