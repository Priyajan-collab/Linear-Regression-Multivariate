
# Linear Regression Model Implementation

This project implements a Linear Regression model using Python from scratch, including feature scaling, gradient descent, and visualization of the cost function's convergence.

## Objective
To understand and implement the basic principles of linear regression without relying on external libraries for the modeling process.

## Features
- Data preprocessing: Handles missing data and performs feature scaling (mean normalization and standardization).
- Custom Linear Regression class: Implements prediction, cost computation, and weight updates.
- Visualization: Plots the convergence of the cost function over iterations using Matplotlib.

## Project Structure
- **`train.csv`**: Dataset file containing features and the target variable (`price`).
- **`linear_regression.py`**: Python script for the Linear Regression implementation.
- **`README.md`**: Documentation file for the project.

## Getting Started

### Prerequisites
- Python 3.x
- Libraries: `numpy`, `pandas`, `matplotlib`

Install required libraries using pip:
```bash
pip install numpy pandas matplotlib
```

### Running the Code
1. Clone this repository and navigate to the project directory.
2. Place the `train.csv` file in the same directory as the Python script.
3. Run the script using:
   ```bash
   python linear_regression.py
   ```
4. The script will output the cost at each iteration and display a graph showing the convergence of the cost function.

### Dataset
The dataset should include the following columns:
- **Features**: `area`, `bedrooms`, `bathrooms`, `stories`, `parking`
- **Target**: `price`

## How It Works
1. **Data Preprocessing**: 
   - Convert all feature columns to numeric and handle missing values by replacing them with zeros.
   - Normalize the features and target variable.

2. **Linear Regression Model**:
   - Predictions are made using the formula: `y = Xw + b`
   - The cost function is computed as the mean squared error.
   - Weights and biases are updated using gradient descent.

3. **Visualization**:
   - A graph is plotted to visualize the cost function's reduction over iterations.

## Results
The implementation shows the reduction in cost (error) as the model learns. The cost function is expected to converge, indicating the effectiveness of the gradient descent optimization.

## License
This project is licensed under the MIT License.

---

Happy Coding!
