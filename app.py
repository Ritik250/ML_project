
import traceback
from flask import Flask, request, render_template
from markupsafe import escape
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('home.html')

    try:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get(
                'parental_level_of_education'
            ),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get(
                'test_preparation_course'
            ),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        pred_df = data.get_data_as_data_frame()
        app.logger.info("Input data received successfully.")

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        app.logger.info("Prediction completed successfully.")

        return render_template('home.html', results=results[0])

    except Exception:
        error_details = traceback.format_exc()
        app.logger.error("PREDICTION FAILED:\n%s", error_details)

        return (
            "<h2>Prediction failed</h2>"
            "<p>Please share this error with the developer:</p>"
            f"<pre>{escape(error_details)}</pre>",
            500
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
