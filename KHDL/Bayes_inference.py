import numpy as np

# Define the prior probabilities
prior = np.ones(6) / 6

# Simulate the dice rolls
dice_rolls = np.random.randint(1, 7, size=3)

# Update the prior probabilities based on the observed data
for roll in dice_rolls:
    likelihood = np.array([roll == i for i in range(1, 7)])
    posterior = prior * likelihood
    prior = posterior / np.sum(posterior)

# Predict the most likely outcome
predicted_result = np.argmax(prior) + 1

print(f"The predicted result of the 3 random dice rolls is: {predicted_result}")
