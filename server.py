from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
@app.route('/emotionDetector', methods=['GET','POST'])
def detect_emotion():
    if request.method == 'POST':
        # Extract JSON data from POST request
        data = request.json
        statement = data.get("statement")
    elif request.method == 'GET':
        # Extract query parameter from GET request
        statement = request.args.get('textToAnalyze')

    response=emotion_detector(statement)

    # If dominant_emotion is None, return error message
    if response.get('dominant_emotion') is None:
        response_message="Invalid text! Please try again."
        return jsonify({"response": response_message})

    # Create a human-readable message
    response_message = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

    return jsonify({"response": response_message})


if __name__ == '__main__':
     app.run()
     