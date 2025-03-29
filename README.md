# **Finetuned-Fraud-Detection-LLM**

This repository aims to develop a fine-tuned language model for identifying fraudulent transactions in financial datasets.

## 🚀 Features

- Fraud detection model fine-tuned on financial transaction data.
- Deep learning model using transformer architecture for high accuracy.
- Comprehensive documentation and dataset preprocessing scripts.

## 🕠️ Installation

### 1 Clone the Repository

```sh
git clone https://github.com/KrishBhimani/Finetuned-Fraud-Detection-LLM.git
```

### 2 Create a Virtual Environment

#### For Windows:
```sh
conda create -p venv python==3.11 -y
conda activate venv/
```

#### For macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3 Install Dependencies

```sh
pip install -r requirements.txt
```

### 4 Run the Application

```sh
python app.py
```

## 📌 Usage

1. Clone the repository and run the pipeline using the command `python run_pipeline.py`.
2. Import and use the fintuned fraud detection model in your application for real-time transaction evaluation.

## 🔧 Technologies Used

- Python
- PyTorch
- Scikit-learn
- Jupyter Notebook
- Pandas
- TensorFlow

## 🚀 Challenges & Solutions

- **Challenge:** Limited labeled data for model training.
  - **Solution:** Used semi-supervised learning techniques to leverage unlabelled data.
- **Challenge:** Extracting relevant features from raw transaction data.
  - **Solution:** Developed custom feature extraction scripts to preprocess data.

## 🤝 Contributing

Contributions are welcome! Feel free to submit **issues** or **pull requests** to improve this project.

---

For more details, refer to the `README` in the root directory of the repository or the API documentation.