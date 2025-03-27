# Crop-Advisory-System
Smart Crop Advisory System

### **🌱 Overview**

The Smart Crop Advisory System is a web-based platform designed to assist farmers in making data-driven agricultural decisions. It provides recommendations for the best crops based on soil type, water availability, and pH level. The system also suggests suitable fertilizers to maximize crop yield.

### **🚀 Features**

Crop Recommendations: Suggests the most suitable crops based on soil and environmental conditions.

Fertilizer Suggestions: Provides optimal fertilizers for recommended crops.

Multilingual Support: Supports multiple languages including Hindi, Bengali, Telugu, and Marathi.

User-Friendly Interface: Simple and intuitive UI for easy input and result interpretation.

Real-time Data Processing: Sends user inputs to the backend and provides instant recommendations.

### **🛠 Technologies Used**

Frontend: HTML, CSS, JavaScript

Backend: Flask (Python)

Database: CSV dataset containing soil, crop, and fertilizer information

Hosting: 

### **📦 Installation & Usage**

Clone the repository:


  ```sh
git clone https://github.com/Rohan-Dedhia/Crop-Advisory-System

cd smart-crop-advisory
``` 

  
Install dependencies:

```sh
pip install flask pandas
```

Run the backend server:

```sh
python app.py
```

Open index.html in a browser to access the advisory system.

### **📡 API Endpoints**

POST /recommend_crop: Accepts JSON input with soil type, water availability, and pH level, and returns crop and fertilizer recommendations.

### **👥 Contributors**

Rohan Dedhia 

Kunaal Kotak

Arnav Jha

Divyam Agarwal
