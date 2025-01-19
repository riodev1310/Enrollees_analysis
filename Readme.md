# Deep Learning Model for Employment Prediction

This project uses a **deep learning model** built with **PyTorch** to predict employment status (`employed` vs. `not employed`) based on demographic, educational, and professional data. The dataset is preprocessed and fed into a fully connected neural network to make predictions.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Dataset Description](#dataset-description)
3. [Model Description](#model-description)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Testing](#testing)
7. [Results](#results)
8. [Future Enhancements](#future-enhancements)

---

## Project Overview

The goal of this project is to predict whether an individual is employed (`employed = 1`) or not (`employed = 0`) using a deep learning model. The project includes:
- Preprocessing of categorical and numerical data.
- Implementation of a PyTorch-based deep learning model.
- Training and evaluation of the model.

---

## Dataset Description

The dataset contains the following columns:

| Column Name            | Description                                        |
|------------------------|----------------------------------------------------|
| `enrollee_id`          | Unique identifier for each enrollee               |
| `city`                 | Location of the individual                        |
| `gender`               | Gender of the enrollee                            |
| `enrolled_university`  | Enrollment status in higher education             |
| `education_level`      | Highest level of education attained               |
| `major_discipline`     | Field of study                                    |
| `relevent_experience`  | Whether the individual has relevant experience    |
| `experience`           | Total years of experience                         |
| `company_size`         | Size of the last company                          |
| `company_type`         | Type of company                                   |
| `last_new_job`         | Gap between last job and current                  |
| `training_hours`       | Number of training hours undertaken               |
| `employed`             | Target variable (1: Employed, 0: Not employed)    |

---

## Model Description

The model is a fully connected neural network implemented in PyTorch. Key details:

1. **Architecture**:
   - Input layer: Matches the number of features.
   - Hidden layers: Two hidden layers with ReLU activation.
   - Output layer: Single neuron with sigmoid activation for binary classification.

2. **Loss Function**:
   - Binary Cross-Entropy Loss (BCELoss).

3. **Optimizer**:
   - Adam optimizer with a learning rate of 0.001.

4. **Training**:
   - Mini-batch gradient descent with a batch size of 32.
   - 20 epochs.

---

## Installation

### Prerequisites

- Python 3.8+
- PyTorch
- scikit-learn
- pandas
- numpy
- matplotlib (for visualization)

### Install Dependencies

```bash
pip install torch torchvision scikit-learn pandas numpy matplotlib
```

---

## Usage

### 1. Data Preprocessing

The dataset is preprocessed by:
- Imputing missing values for numerical and categorical features.
- Scaling numerical data using `StandardScaler`.
- Encoding categorical features using `OneHotEncoder`.

### 2. Training the Model

The model is trained using the `train_loader` and validated on the `test_loader`.

### 3. Evaluation

Evaluate the model using metrics such as accuracy and a classification report.

Run the following script:

```bash
python train_model.py
```

---

## Testing

To test the model on the test dataset:

```bash
python test_model.py
```

The script outputs metrics such as accuracy, precision, recall, and F1-score.

### Example Output

```plaintext
Accuracy: 0.87

Classification Report:
              precision    recall  f1-score   support

         0.0       0.85      0.90      0.87       100
         1.0       0.89      0.84      0.86       100

    accuracy                           0.87       200
   macro avg       0.87      0.87      0.87       200
weighted avg       0.87      0.87      0.87       200
```

---

## Results

- **Accuracy**: ~87%
- The model effectively differentiates between employed and unemployed individuals based on the features provided.

---

## Future Enhancements

1. **Hyperparameter Tuning**:
   - Optimize learning rate, batch size, and number of layers.

2. **Feature Engineering**:
   - Add interaction terms or derived features.

3. **Deep Learning Improvements**:
   - Experiment with advanced architectures such as LSTM or Transformers for sequential features.

4. **Deployment**:
   - Create an API for real-time predictions using Flask or FastAPI.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.