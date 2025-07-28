from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # frontend from other origin (like file:// or localhost)

@app.route('/merge', methods=['POST'])
def merge_text():
    prompt = request.form.get('prompt')
    uploaded_file = request.files.get('file')

    if not uploaded_file or not uploaded_file.filename.endswith('.txt'):
        return jsonify({"error": "Please upload a .txt file."}), 400

    file_content = uploaded_file.read().decode('utf-8')
    merged = f"{prompt}\n\n{file_content}"

    return jsonify({"merged_text": merged})

if __name__ == '__main__':
    app.run(debug=True)
