# run.py

# Starts the application up.

from app import app

import sys

if __name__ == "__main__":
    print("Access the GUI via http://127.0.0.1:5000/ in your prefered browser.")
    app.run(debug=True)