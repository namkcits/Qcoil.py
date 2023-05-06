import numpy as np
from qiskit.quantum_info import Statevector

# Create an unnormalized statevector
psi = np.array([1, 2+3j, 4j, 5])

# Normalize the statevector
psi_norm = psi / np.linalg.norm(psi)

# Create a Statevector object
sv = Statevector(psi_norm)

# Print the statevector
print(sv)
