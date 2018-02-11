"""
Main App file
"""
import csv
import io
import json
import os
from markupsafe import Markup

from settings import FILES

from flask import Flask, render_template  # , request

# static files should really be handled by a web server...
app = Flask(__name__)  # , static_url_path='/assets')

@app.route("/")
def home():
    return render_template(
        "index.html",
        filenames=Markup(json.dumps(FILES.keys())),
    )


def read_csv(filename):
    path = os.path.join(os.getcwd(), "data", filename)
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

    filename = FILES.get(file_constant)

    if filename is None:
        return app.response_class(
            response="Invalid file: {}".format(file_constant),
            status=404,
            mimetype="application/json",
        )

    data = read_csv(filename)
    return json.dumps(data)
