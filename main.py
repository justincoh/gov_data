"""
Main App file
"""
import csv
import io
import json
import settings

from flask import Flask, render_template
app = Flask(__name__)

def read_csv(filename):

    with io.open(filename, "r", encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
        data = [row for row in reader]
        return data

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/outlays")
def outlays():
    data = read_csv(settings.FILE_OUTLAY_BY_AGENCY)
    return json.dumps(data)

@app.route("/testfile")
def testfile():
    data = read_csv(settings.FILE_TEST)
    return json.dumps(data)