# Student Exam Performance Prediction

A Flask application that predicts a student’s math score based on demographic and exam preparation data using a trained CatBoost model and preprocessing pipeline.

## Project Structure

```
artifacts/                # Stored model and preprocessing artifacts
  ├── model.pkl           # Trained CatBoost model
  └── preprocessor.pkl    # Preprocessing pipeline

data/                     # Raw and processed data files
  ├── train.csv
  └── test.csv

notebook/                 # Jupyter notebooks
  ├── 1. EDA STUDENT PERFORMANCE.ipynb
  └── 2. MODEL TRAINING.ipynb

src/                      # Application source code
  ├── components/         # Data validation and input schemas
  ├── pipeline/           # Inference pipeline assembly
  ├── exception.py        # Custom exception classes
  ├── logger.py           # Logging setup
  └── utils.py            # Utility functions

templates/                # HTML templates for Flask
  ├── home.html
  └── index.html

Dockerfile                # Docker build instructions
Dockerrun.aws.json        # AWS Elastic Beanstalk configuration
buildspec.yml             # AWS CodeBuild spec
application.py            # Flask application entry point
requirements.txt          # Python dependencies
.gitignore                # Files to ignore in Git
.dockerignore             # Files to ignore in Docker context
README.md                 # Project documentation (this file)
```

## Prerequisites

- Docker installed locally
- (Optional) Python 3.8+ and pip if running without Docker

## Quick Start with Docker

1. **Build the image** (run from project root):

   ```bash
   docker build -t ml-app .
   ```

2. **Run the container**:

   ```bash
   docker run -d \
     -p 5000:5000 \
     --name ml-app \
     ml-app
   ```

3. **Access the app** in your browser:

   ```
   http://localhost:5000/
   ```

## Running Locally without Docker

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   export FLASK_APP=application.py
   export FLASK_ENV=production
   flask run --host=0.0.0.0 --port=5000
   ```

4. Navigate to `http://localhost:5000/`

## Model Training

See `notebook/2. MODEL TRAINING.ipynb` for details on data preprocessing and training the CatBoost model. The trained model and preprocessor are saved in `artifacts/model.pkl` and `artifacts/preprocessor.pkl`.

## License

This project is licensed under the MIT License. Feel free to use and modify.

