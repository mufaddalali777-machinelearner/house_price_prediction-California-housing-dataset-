# California Housing Price Prediction  
## Linear Regression from Scratch (NumPy)

---

## Project Overview
This project implements **Linear Regression from scratch** (without using scikit-learn’s regression models) to predict **median house values** using the **California Housing dataset**.

The main objective of this project is to build a strong understanding of the **mathematics and optimization behind linear regression**, including feature scaling, cost functions, and gradient descent.

---

## Objectives
- Implement Linear Regression **without using ML libraries**
- Understand and apply **gradient descent**
- Perform **feature scaling** for faster convergence
- Analyze cost reduction during training

---

## Dataset
- **Source:** `sklearn.datasets.fetch_california_housing`
- **Total samples:** 20,640
- **Features:** 8 numerical features  
  (e.g., median income, house age, average rooms, etc.)
- **Target variable:** `MedHouseVal` (Median house value)

---

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

> No scikit-learn regression models were used  
> Model implemented fully from scratch

---

## Methodology

### 1) Data Preparation
- Loaded dataset using `fetch_california_housing`
- Separated features (`X`) and target (`y`)
- Applied **feature scaling (standardization)**

### 2) Model Implementation
- Defined Mean Squared Error (MSE) cost function
- Implemented:
  - Forward computation
  - Gradient calculation
  - Gradient Descent optimization
- Tuned learning rate (`α`) and number of iterations

### 3) Training
- Initialized weights and bias to zero
- Iteratively updated parameters using gradient descent
- Tracked cost function values to monitor convergence

---

## Results & Observations
- Cost function decreased steadily, confirming correct implementation
- Feature scaling significantly improved convergence speed
- Model learned meaningful weights for housing features

---

## Key Learnings
- Linear regression is fundamentally an optimization problem
- Feature scaling is crucial for gradient descent performance
- Implementing models from scratch builds strong ML fundamentals
- Understanding the math helps in debugging and model intuition

---


---

## Future Improvements
- Add train-test split and evaluation metrics (RMSE, R²)
- Compare performance with scikit-learn implementation
- Extend to polynomial regression
- Implement regularization (Ridge / Lasso)

---

## Author
**Mufaddal Tambawala**  
Aspiring Machine Learning Engineer  

