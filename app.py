import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

## route for a home page

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    
    else:
        data=C