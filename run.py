from flask import Flask
from flask_cors import CORS
from app.routes import application



# -----------------------------------------------
# Run server
# -----------------------------------------------
if __name__ == '__main__':
    application.run(debug=True)
