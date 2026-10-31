from pathlib import Path

import numpy as np
import pandas as pd


# Set a fixed random seed for reproducible results
rng = np.random.default_rng(seed=42)

# Number of virtual beam configurations
n_samples = 1000

# Generate random beam geometry
length = rng.uniform(0.5, 2.0, n_samples)          # m
width = rng.uniform(0.02, 0.10, n_samples)         # m
thickness = rng.uniform(0.005, 0.02, n_samples)    # m

# Generate random material properties
youngs_modulus = rng.uniform(70e9, 210e9, n_samples)  # Pa
density = rng.uniform(2700, 7850, n_samples)           # kg/m^3

# Rectangular cross-section properties
cross_section_area = width * thickness
second_moment_area = width * thickness**3 / 12

# First eigenvalue for a cantilever beam
beta_1 = 1.875104

# First natural frequency using Euler-Bernoulli beam theory
natural_frequency = (
    beta_1**2
    / (2 * np.pi * length**2)
    * np.sqrt(
        youngs_modulus * second_moment_area
        / (density * cross_section_area)
    )
)

# Create the structural-dynamics dataset
df = pd.DataFrame(
    {
        "Length_m": length,
        "Width_m": width,
        "Thickness_m": thickness,
        "Youngs_Modulus_Pa": youngs_modulus,
        "Density_kg_m3": density,
        "Natural_Frequency_Hz": natural_frequency,
    }
)

# Determine project directory independent of the current terminal location
project_root = Path(__file__).resolve().parent.parent
output_file = project_root / "data" / "beam_dataset.csv"

# Save dataset
df.to_csv(output_file, index=False)

print("Dataset generated successfully!")
print(f"Number of samples: {len(df)}")
print(f"Dataset saved to: {output_file}")
print()
print(df.head())
print()
print("Natural frequency statistics:")
print(df["Natural_Frequency_Hz"].describe())