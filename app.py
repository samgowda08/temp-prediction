from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load the weather dataset
weather_df = pd.read_csv('weather.csv')

# Create a LinearRegression model and fit it to the data
model = LinearRegression()
X = weather_df[['humidity', 'wind_speed']]
y = weather_df['temperature']
model.fit(X, y)

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    humidity = float(request.form['humidity'])
    wind_speed = float(request.form['wind_speed'])

    # Use the model to make a prediction
    input_data = pd.DataFrame({'humidity': [humidity], 'wind_speed': [wind_speed]})
    prediction = model.predict(input_data)[0]

    # Render the result template with the prediction
    return render_template('result.html', prediction=prediction)
@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded CSV file
    csv_file = request.files['csv-file']

    # Load the CSV file into a Pandas DataFrame
    new_data = pd.read_csv(csv_file)

    # Merge the new data with the training dataset
    df = pd.concat([df, new_data], ignore_index=True)

    # Re-train the model with the merged dataset
    X = df[['humidity', 'wind_speed']]
    y = df['temperature']
    model.fit(X, y)

    # Redirect to the home page
    return redirect(url_for('index'))

@app.route('/uploadpage')
def uploadpage():
    return render_template('upload.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

if __name__ == '__main__':
    app.run(debug=True)
#add statistics of the model in another page(live statistics)
#refine upload page
#add input validation for csv upload