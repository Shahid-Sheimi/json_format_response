import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Dummy data for entities and their details
entities = ["Entity1", "Entity2", "Entity3","Entity4", "Entity5", "Entity6"]
entity_details = ["Entity_Detailsd1", "Entity_Detailsd2", "Entity_Detailsd3","Entity_Detailsd4", "Entity_Detailsd5", "Entity_Detailsd6"]

@app.route('/')
def home_page():
    return jsonify({"message": "Welcome to the Plant Disease Diagnosis API"})

@app.route('/index')
def ai_engine_page():
    return jsonify({"message": "AI Engine page"})

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        file_extension = filename.rsplit('.', 1)[-1].lower()
        if file_extension not in ['png', 'jpg', 'jpeg', 'webp', 'jfif']:
            return jsonify({"error": "Unsupported file format. Please upload a PNG, JPG, JPEG, webp, or jfif file."}), 400

        # Save the file if needed
        file_path = os.path.join('static/uploads', filename)
        image.save(file_path)

        # Use dummy index for this example
        pred = 0  # You can change this index or implement logic if needed

        # Create response based on dummy data
        response = {
            "Entity": entities,
            "Entity_Details": entity_details
        }

        return jsonify(response)

@app.route('/detail', methods=['GET'])
def detail():
    return jsonify({
        "Entity": entities
    })

if __name__ == '__main__':
    app.run(debug=True)
