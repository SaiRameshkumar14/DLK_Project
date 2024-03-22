from flask import Flask, render_template, jsonify, request
from transformers import VitsModel, AutoTokenizer


app = Flask(__name__)

model = VitsModel.from_pretrained("facebook/mms-tts-tam")
feature_extractor = AutoTokenizer.from_pretrained("facebook/mms-tts-tam")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    audio_data = request.files['audio'].read()
    input_features = feature_extractor(audio_data, return_tensors="pt")
    output = model(**input_features).logits
    text_output = feature_extractor.decode(output)[0]

    return jsonify({'text': text_output}), 200

if __name__ == '__main__':
    app.run(debug=True)


