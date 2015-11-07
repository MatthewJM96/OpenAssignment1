# views.py

# Handles the various views of the flask application.

from flask import render_template, flash, redirect, url_for, request
from app import app
from app import utils

import numpy as np

import os

@app.route("/", methods=["GET"])
def entry():
  # entry
  # Handles the entry point route to the application.
  # Author: Matthew Marshall
  # Date Created: 06/11/2015
  
  # Check data file directory contents, fail if empty.
  if not os.listdir("data"):
    return render_template("error.html?error=1",
                            title="Error - No Data Files.")
  
  # Form template for inserting located data files.
  form = { "data": { "label": "Data File:", "isSelect": 1, "name": "file", "selections": [] } }
  
  # Iterate data files and add to form template.
  for file in os.listdir("data"):
    if file.endswith(".csv"):
      form["data"]["selections"].append({ "name": os.path.splitext(file)[0], "value": file })
  
  # Create view with form of data files.
  return render_template("index.html",
                          title="Graphing Utility",
                          form=form)

@app.route("/graphing", methods=["POST"])
def graphing():
  # graphing
  # Handles the graphing route of the application.
  # Author: Matthew Marshall
  # Date Created: 06/11/2015
  
  # Read chosen data file and if reading fails, render error.
  fileData = utils.readFile("data/" + request.form["file"])
  if (fileData == 0):
    return render_template("error.html?error=2",
                            title="Error - File Not Read.")
  
  # Transpose file data and construct a form for rendering.
  fileDataTransposed = np.transpose(fileData)
  form = { "data":   { "names":        { "label": "Name",       "data":  fileDataTransposed[0] },
                       "type":         { "label": "Type",       "data":  fileDataTransposed[1] },
                       "population":   { "label": "Population", "data":  fileDataTransposed[2] },
                       "latitude":     { "label": "Latitude",   "data":  fileDataTransposed[3] },
                       "longitude":    { "label": "Longitude",  "data":  fileDataTransposed[4] } },
           "params": { "data":         { "name":  "data",       "value": request.form["file"], "isHidden": 1 },
                       "type":         { "name":  "type",       "value": "pop_geo_bar",        "isHidden": 1 }, } }
  
  #os.system("python app/test.py " + request.form["file"])
  
  # Create view with form of file data.
  return render_template("graphing.html",
                          title="Graphing Utility",
                          form=form)

@app.route("/graphing/plot", methods=["GET"])
def plot():
  # plot
  # Handles the plotting of a graph.
  # Author: Matthew Marshall
  # Date Created: 06/11/2015
  
  if str(request.args.get("type")) == "pop_geo_bar":
    os.system("python app/plotPopGeo.py " + request.args.get("data"))
    
  return render_template("complete.html",
                          title="Graphing Utility",)