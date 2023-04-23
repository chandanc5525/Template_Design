from flask import Flask
from MachineLearning.logger import logging
from MachineLearning.exception import CustomException
import os, sys
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing our custom exception file")
    except Exception as e:
        MachineLearning = CustomException(e, sys)
        logging.info(MachineLearning.error_message)
        logging.info("We are testing logging module")
        return "hello World"
    

if __name__=="__main__":
    app.run(debug=True)