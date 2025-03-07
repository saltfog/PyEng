#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 18:55:39 2025

@author: caseyjenkins
"""

# Compute the equivalent of ±3 standard deviations in the left-skewed distribution
# In a standard normal distribution, ±3 sigma corresponds to ~0.13% (left) and 99.87% (right)
# We find the values in the skew-normal distribution that correspond to these percentiles

# Fix and re-run the corrected code

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import skewnorm

# Define skew parameter
skew_param = -2.5  # Negative value for left skew

# Generate data for the left-skewed normal distribution within the range [7, 10]
x_skewnorm = np.linspace(4, 10, 1000)
y_skewnorm = skewnorm.pdf(x_skewnorm, skew_param, loc=8.5, scale=1)  # Shifted distribution

# Compute the equivalent of ±3 standard deviations in the left-skewed distribution
left_percentile = stats.norm.cdf(-3) * 100  # ~0.13%
right_percentile = stats.norm.cdf(3) * 100  # ~99.87%

# Find the corresponding values in the left-skewed normal distribution (adjusted for location & scale)
left_3sigma_value = skewnorm.ppf(left_percentile / 100, skew_param, loc=8.5, scale=1)
right_3sigma_value = skewnorm.ppf(right_percentile / 100, skew_param, loc=8.5, scale=1)

# Compute the actual percentiles for these values in the skew-normal distribution
left_3sigma_percentile = round(skewnorm.cdf(left_3sigma_value, skew_param, loc=8.5, scale=1) * 100, 3)
right_3sigma_percentile = round(skewnorm.cdf(right_3sigma_value, skew_param, loc=8.5, scale=1) * 100, 3)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x_skewnorm, y_skewnorm, label="Left-Skewed Normal Distribution")

# Highlight the computed 3-sigma equivalent points
for v, p in zip([left_3sigma_value, right_3sigma_value], [left_3sigma_percentile, right_3sigma_percentile]):
    plt.scatter(v, skewnorm.pdf(v, skew_param, loc=8.5, scale=1), color='red', zorder=3)
    plt.axvline(v, color='red', linestyle='dashed', alpha=0.7)
    plt.text(
        v, skewnorm.pdf(v, skew_param, loc=8.5, scale=1) + 0.02, f"{p:.3f}%\n({v:.3f})",
        ha='center', fontsize=10, color='black',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')
    )

# Labels and title
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.title("Left-Skewed Normal Distribution with 3-Sigma Equivalents")
plt.legend(["Skew-Normal Distribution"])
plt.grid()

# Show plot
plt.show()

# Display calculated values
left_3sigma_value, right_3sigma_value
