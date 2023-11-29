from flask import Flask, request, jsonify

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

        # Here, you can call your Gmaps.places method or perform any other desired action with the query

        return jsonify({"success": "Query processed successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
