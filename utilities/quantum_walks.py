#------------------------------------------------------------------------------
# quantum_walk.py
#
# This module implements a simple quantum walk using a quantum circuit. The walk
# is influenced by a biased rotation, allowing control over the probability of
# movement in either direction. The circuit applies a biased quantum coin flip
# and a controlled NOT operation to simulate the quantum walk process.
#
# Functions included:
# - simple_biased_walk(n, steps, theta): Constructs a quantum circuit implementing a
#  simple quantum walk on an n-position space for a given number of steps and a bias angle.
#
# © Leonardo Lavagna 2025
# @ NESYA https://github.com/NesyaLab
#------------------------------------------------------------------------------

import numpy as np
from qiskit import QuantumCircuit

def simple_biased_walk(n, steps, theta=np.pi/4):
    """
    Implements a quantum walk using a quantum circuit.

    Args:
        n (int): The number of positions available for the walker.
        steps (int): The number of steps the walker takes.
        theta (float): A bias angle for the coined walk.

    Returns:
        QuantumCircuit: The quantum circuit implementing the quantum walk.
    """
    num_qubits = int(np.ceil(np.log2(n)))  
    qc = QuantumCircuit(num_qubits)
    for _ in range(steps):
        # Apply biased rotation (quantum coin flip)
        for qubit in range(num_qubits):
            qc.ry(theta, qubit)
        # Apply a controlled-NOT to shift the walker to the next position
        for qubit in range(num_qubits - 1):
            qc.cx(qubit, qubit + 1)
    qc.measure_all()  
    return qc