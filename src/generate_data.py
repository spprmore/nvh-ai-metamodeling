# AI-Based NVH Metamodeling
# Dataset generation script

import numpy as np
import pandas as pd

# Number of samples
n_samples = 1000

# Random beam parameters
length = np.random.uniform(0.5, 2.0, n_samples)      # m
width = np.random.uniform(0.02, 0.10, n_samples)     # m
thickness = np.random.uniform(0.005, 0.02, n_samples) # m
youngs_modulus = np.random.uniform(70e9, 210e9, n_samples) # Pa
density = np.random.uniform(2700, 7850, n_samples)   # kg/m³

# Simplified natural frequency model
frequency = (
    (thickness / length**2)
    * np.sqrt(youngs_modulus / density)
    * 100
)

# Create dataframe
df = pd.DataFrame({
    "Length_m": length,
    "Width_m": width,
    "Thickness_m": thickness,
    "Youngs_Modulus_Pa": youngs_modulus,
    "Density_kg_m3": density,
    "Natural_Frequency_Hz": frequency
})

# Save dataset
df.to_csv("data/beam_dataset.csv", index=False)

print("Dataset generated successfully!")
print(df.head())

