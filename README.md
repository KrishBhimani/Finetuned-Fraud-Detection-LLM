# Finetuned-Fraud-Detection-LLM

A project leveraging Large Language Models (LLMs) for the detection and prevention of fraudulent activities through fine-tuning on specific datasets.

## 🚀 Features

- Utilizes LLMs for intelligent fraud detection
- Fine-tuned on diverse datasets to improve accuracy
- Provides actionable insights and real-time alerts

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

1. Clone the repository and set up your virtual environment by following the instructions above.
2. Install the required dependencies.
3. Run the application.
4. Use the provided API endpoints or interact with the CLI for detecting fraud.

## 🔧 Technologies Used

- Python 3.11
- Jupyter Notebook for experiments and model training
- Machine learning libraries (scikit-learn, TensorFlow, PyTorch)
- API endpoints and CLI interface for user interaction

## 🚀 Challenges & Solutions

- **Challenge 1: Data Imbalance in Training Datasets.**
  - **Solution:** Applied data augmentation techniques and SMOTE to balance the dataset.

- **Challenge 2: Model Complexity and Inference Time.**
  - **Solution:** Optimized the model during training and fine-tuned to ensure faster inference without compromising accuracy.

## 🤝 Contributing

Contributions are welcome! Feel free to submit **issues** or **pull requests** to improve this project.