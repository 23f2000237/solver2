from flask import Flask, request, jsonify
from Flask import Response
from flask_cors import CORS
import os
import socket
import asyncio
from response import get_response
socket.setdefaulttimeout(300)
app = Flask(__name__)
CORS(app)  # Enable CORS globally
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300
UPLOAD_FOLDER = '/tmp'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/', methods=['POST'])
def handle_request():
    """POST endpoint to accept query and optional file."""
    file_path = None
    query = request.form.get('question')  # Using "question" to match your request
    file = request.files.get('file')
    if not query:
        return jsonify({"error": "Query is required."}), 400
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
    val = asyncio.run(get_response(query, file_path))
    return jsonify({"answer": Response(val, mimetype="text/plain")}),200
    # Save the file if uploaded

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
