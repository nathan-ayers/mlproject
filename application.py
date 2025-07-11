from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # 1) gather & wrap form inputs
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=int(request.form.get('reading_score', 0)),
            writing_score=int(request.form.get('writing_score', 0))
        )
        # 2) turn it into a DataFrame
        pred_df = data.get_data_as_data_frame()
        # 3) predict
        pipeline = PredictPipeline()
        result = pipeline.predict(pred_df)[0]

    # on GET, result is None → just show empty form; on POST, show form + result
    return render_template('index.html', result=result)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)
