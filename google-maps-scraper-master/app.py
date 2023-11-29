from flask import Flask, request, jsonify
from src.gmaps import Gmaps  # Assuming your Gmaps class is in src/gmaps.py

app = Flask(__name__)

@app.route('/get_places', methods=['POST'])
def get_places():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Check if the 'query' key is present in the JSON data
        if 'query' not in data:
            return jsonify({"error": "Query parameter is required"}), 400

        # Extract the query from the JSON data
        query = data['query']

        # Call the Gmaps.places method to get places
        places_result = Gmaps.places([query], max=5)

        # You can do something with the places_result here if needed

        return jsonify({"success": "Query processed successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
