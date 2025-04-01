from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/recommend_crop": {"origins": "*"}})  # Adjust origins as needed

# Load dataset
try:
    crop_data = pd.read_csv('crop.csv')
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")
    crop_data = pd.DataFrame()  # Fallback empty DataFrame

@app.route('/recommend_crop', methods=['POST', 'OPTIONS'])
def recommend_crop():
    if request.method == 'OPTIONS':
        return '', 200

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data received"}), 400

        soil_type = data.get('soil_type')
        water_available = data.get('water_available')
        soil_ph = data.get('soil_ph')

        if any(x is None for x in [soil_type, water_available, soil_ph]):
            return jsonify({"error": "Missing input fields: soil_type, water_available, soil_ph required"}), 400

        # Convert inputs to appropriate types
        soil_type = int(soil_type)
        water_available = float(water_available)
        soil_ph = float(soil_ph)

        # Filter crops based on conditions
        filtered_crops = crop_data[
            ((crop_data['Soil_Type'] == soil_type) | (soil_type == 0)) &  # Soil type match or general soil
            (crop_data['Water_Requirement_mm'] <= water_available) &      # Water availability
            (abs(crop_data['pH_Avg'] - soil_ph) <= 0.5)                  # pH within ±0.5
        ]

        if filtered_crops.empty:
            return jsonify({"message": "No suitable crops found for the given conditions"}), 200

        # Prepare recommendations
        recommendations = filtered_crops[[
            'Crop', 'Recommended_Fertilizer', 'Water_Requirement_mm', 
            'Yield_per_Acre_Qtl', 'Best_Harvest_Time'
        ]].to_dict(orient='records')

        return jsonify({"recommended_crops": recommendations}), 200

    except ValueError as ve:
        return jsonify({"error": f"Invalid input format: {str(ve)}"}), 400
    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
