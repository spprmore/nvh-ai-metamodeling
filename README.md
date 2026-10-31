AI-Based NVH Metamodeling
This project demonstrates the use of machine learning as a surrogate model (metamodel) for predicting structural dynamic characteristics.

The objective is to explore how data-driven surrogate models can reduce computational effort by providing fast predictions of structural responses. In this proof-of-concept, a dataset of virtual beam configurations is generated using an analytical structural-dynamics model, and a machine learning model is trained to estimate the first natural frequency from geometric and material parameters.

Motivation
Modern CAE workflows often require large numbers of simulations for parameter studies, design exploration, and optimization. These simulations can become computationally expensive when many design combinations need to be evaluated.

This project investigates how machine learning can be used to create surrogate models that approximate physics-based calculations and predict structural dynamic behavior more efficiently, supporting future NVH and engineering analysis applications.

The current implementation uses an analytical beam model as the data source. The same workflow could later be extended to FEM-generated or experimental data.

Key Topics
Structural Dynamics
NVH (Noise, Vibration, Harshness)
Machine Learning
Surrogate Modeling
CAE Data Analytics
Python
Physics-Based Data Generation
Project Objectives
Generate a structural-dynamics dataset
Calculate the first natural frequency using an analytical beam model
Train a machine learning surrogate model
Predict natural frequencies from geometric and material parameters
Compare analytical and machine-learning responses
Evaluate surrogate-model prediction performance
Analyze the influence of individual input parameters
Demonstrate AI-driven metamodeling for future CAE applications
Methodology
The project follows the workflow:

Generate random beam geometry and material parameters.
Calculate the first natural frequency using Euler-Bernoulli beam theory.
Store the generated results as a structural-dynamics dataset.
Split the dataset into training and testing subsets.
Train a Random Forest regression model.
Predict natural frequencies for unseen test configurations.
Evaluate model performance using R² and RMSE.
Compare actual and predicted natural frequencies.
Analyze feature importance and compare the learned relationships with the underlying physics.
Input Parameters
The following parameters are varied:

Beam length
Beam width
Beam thickness
Young's modulus
Material density
The prediction target is:

First natural frequency (Hz)
A total of 1,000 virtual beam configurations are generated.

Physics Model
The first bending natural frequency of a uniform cantilever beam is calculated using the Euler-Bernoulli beam formulation:

f₁ = (β₁² / 2πL²) × √(EI / ρA)

where:

β₁ ≈ 1.875 for the first cantilever bending mode
L = beam length
E = Young's modulus
I = second moment of area
ρ = material density
A = cross-sectional area
For a rectangular cross-section:

A = b × h

I = b × h³ / 12

where:

b = beam width
h = beam thickness
For this idealized formulation:

I / A = h² / 12

Therefore, the beam width cancels from the analytical natural-frequency relationship. This becomes useful later when comparing the physics with the feature importance learned by the machine-learning model.

Dataset
The generated dataset contains 1,000 samples.

Example variables:

Length_m
Width_m
Thickness_m
Youngs_Modulus_Pa
Density_kg_m3
Natural_Frequency_Hz
Natural frequency statistics from the generated dataset:

Samples:   1000
Minimum:   0.81 Hz
Mean:     10.71 Hz
Median:    6.52 Hz
Maximum:  83.40 Hz
The dataset is stored in:

data/beam_dataset.csv
Machine Learning Model
A Random Forest Regressor is used as the surrogate model.

The dataset is divided into:

80% training data: 800 samples
20% testing data: 200 samples
A fixed random state is used to make the experiment reproducible.

The model receives the following inputs:

Length
Width
Thickness
Young's Modulus
Density
and predicts:

First Natural Frequency
The Random Forest contains 100 decision trees and learns the nonlinear relationship between the beam parameters and the corresponding natural frequency directly from the generated dataset.

Results
The trained Random Forest surrogate model achieved:

R² Score: 0.9743
RMSE: 1.6060 Hz
The R² score indicates strong agreement between the surrogate-model predictions and the analytical test data.

The RMSE represents the prediction error in the same unit as the target quantity, Hz.

Actual vs Predicted Natural Frequency
The following figure compares the analytical natural frequencies with the predictions produced by the Random Forest surrogate model.

Actual vs Predicted Natural Frequency

Each point represents one unseen test configuration.

The red dashed line represents ideal predictions where:

Predicted Frequency = Actual Frequency
Most predictions are located close to the ideal prediction line, demonstrating strong overall agreement between the analytical model and the machine-learning surrogate model.

Larger deviations are visible for some high-frequency configurations, providing an opportunity for further model and dataset improvement.

Feature Importance
The Random Forest model also provides information about the relative importance of each input parameter.

Feature Importance

The analysis shows that:

Beam length has the strongest influence.
Beam thickness is the second most influential parameter.
Density and Young's modulus have smaller influences.
Beam width has almost no influence.
This result is consistent with the underlying analytical relationship:

f₁ ∝ (h / L²) × √(E / ρ)

The very low importance of beam width deal Euler-Bernoulli natural-frequency formulation for the rectangular cross-section used in this project.

This provides a useful consistency check between the relationships learned by the machine-learning model and the underlying structural physics.

Project Structure
nvh-ai-metamodeling/
│
├── data/
│   └── beam_dataset.csv
│
├── docs/
│
├── figures/
│   ├── actual_vs_predicted.png
│   └── feature_importance.png
│
├── results/
│   └── random_forest_model.pkl
│
├── src/
│   ├── generate_data.py
│   └── train_model.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
Tools and Technologies
Python
NumPy
Pandas
Scikit-Learn
Matplotlib
Seaborn
Joblib
Git / GitHub
How to Run
1. Install the required Python packages
python -m pip install -r requirements.txt
2. Generate the structural-dynamics dataset
python src/generate_data.py
This generates:

data/beam_dataset.csv
3. Train and evaluate the surrogate model
python src/train_model.py
This:

Trains the Random Forest model
Evaluates the model on unseen test data
Calculates R² and RMSE
Generates the evaluation plots
Saves the trained surrogate model
The trained model is stored in:

results/random_forest_model.pkl
The evaluation figures are stored in:

figures/
Assumptions and Limitations
This project is a proof-of-concept and uses synthetic data generated from an analytical structural-dynamics model.

The primary assumptions are:

Uniform cantilever beam
Rectangular cross-section
Linear elastic material behavior
Small deformation
Euler-Bernoulli beam theory
First bending mode only
No damping
No FEM-generated training data
No experimental training data
Therefore, the current surrogate model should not be interpreted as a replacement for industrial NVH or CAE simulations.

The purpose of the project is to demonstrate the complete workflow from physics-based data generation to machine-learning surrogate modeling, validation, and engineering interpretation.

Future Work
Potential extensions include:

Generate training data using FEM simulations
Include additional structural parameters
Consider different boundary conditions
Predict multiple natural frequencies and mode shapes
Compare Random Forest with other surrogate-modeling approaches
Perform hyperparameter optimization
Introduce noise and uncertainty into the dataset
Perform design optimization using the trained surrogate model
Extend the workflow toward automotive NVH applications

Status
✅ Version 1 Complete

Current implementation includes:

Physics-based dataset generation
1,000 parametric beam configurations
Random Forest surrogate modeling
Train/test validation
R² and RMSE evaluation
Actual vs predicted visualization
Feature-importance analysis
Physics-to-ML consistency analysis

License
This project is licensed under the MIT License.