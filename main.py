from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy movie prediction function
def predict_movie_success(features):
    # For demonstration, a simple rule-based prediction
    # For example, if budget > 50 million and genre is 'Action', predict success
    budget = float(features.get('budget', 0))
    genre = features.get('genre', '').lower()
    if budget > 50 and genre == 'action':
        return "High Success Probability"
    else:
        return "Low Success Probability"

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = {
        'budget': request.form.get('budget'),
        'genre': request.form.get('genre')
    }
    prediction = predict_movie_success(features)
    return render_template('index.html', prediction=prediction, features=features)

if __name__ == '__main__':
    app.run(debug=True)
