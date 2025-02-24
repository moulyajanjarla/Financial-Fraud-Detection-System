💰 Financial Fraud Detection System


A Financial Fraud Detection System built with Python 3.11, Flask, and Scikit-learn. The system detects fraudulent transactions using a machine learning model trained on the Kaggle Credit Card Fraud Detection Dataset. The API is containerized using Docker for easy deployment.

🚀 Features


🔍 Detect fraudulent transactions based on input features
📊 Machine learning model trained using RandomForestClassifier
🌐 REST API using Flask
🐳 Dockerized for seamless deployment
⚡ Fast, efficient, and scalable
🏗️ Project Structure


financial-fraud-detection/
│
├── app.py                      # Flask API for fraud prediction
├── fraud_detection_model.pkl    # Trained machine learning model
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
├── train_model.ipynb            # Jupyter Notebook for training the model
└── README.md      

# Project documentation


📥 Installation

✅ 1. Clone the Repository
bash
Copy
Edit
git clone <your-github-repo-url>
cd financial-fraud-detection



✅ 2. Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate



✅ 3. Install Dependencies

pip install -r requirements.txt
✅ 4. Train the Model
Run the Jupyter Notebook to train the model:


jupyter notebook train_model.ipynb
This will generate the fraud_detection_model.pkl file.

🐳 Docker Setup
✅ 1. Build the Docker Image

docker build -t fraud-detection-flask .

✅ 2. Run the Docker Container

docker run -d -p 5000:5000 fraud-detection-flask

✅ 3. Verify Running Containers

docker ps


🔌 API Endpoints


📍 POST /predict
Request:
Sends transaction details as features for fraud prediction.


{
  "features": [0.1, -1.2, 0.5, 0.3, 1.5, -0.9, 0.7, -0.6, 0.4, 0.3, 0.1, -1.1, 1.2, 0.0, -0.4, 0.2, 1.3, 0.1, -0.5, 0.4, 0.2, 0.1, -1.0, 1.4, -0.3, 0.1, 0.5, -0.2, 0.3]
}
Response:


{
  "fraud_prediction": 0
}
0 → Not Fraudulent
1 → Fraudulent
🛑 Stopping the Docker Container
List running containers:


docker ps
Stop the container:


docker stop <container_id>

🛠️ Technologies Used



Python 3.11
Flask - For building RESTful APIs
Scikit-learn - Machine Learning
Docker - Containerization
Jupyter Notebook - Model training


🧑‍💻 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

📜 License
This project is licensed under the MIT License.

🔗 Acknowledgments
Kaggle Credit Card Fraud Detection Dataset
