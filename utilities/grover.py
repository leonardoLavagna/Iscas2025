#------------------------------------------------------------------------------
# grover.py
#
# This module provides utility functions for implementing the approximate Grover 
# search algorithm using Qiskit. It includes functions for constructing an 
# approximate Grover circuit, creating oracles for marked states, and applying 
# Grover search to solve permutation-based problems.
#
# Functions included:
# - approximate_grover(n_qubits, oracle, iterations, theta): Implements an 
#   approximate Grover search algorithm.
# - create_oracle(s): Creates a Grover's oracle for a specific bitstring.
# - permutation_grover(t, permutation_function): Finds the original bitstring 
#   given a permuted bitstring and a permutation function.
#
# These utilities are designed for quantum computing applications, particularly 
# in quantum search algorithms.
#
# © Leonardo Lavagna 2025
# @ NESYA https://github.com/NesyaLab
#------------------------------------------------------------------------------


import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from config import backend


def simulate(circ,backend):
    """
    Simulate a quantum circuit on a given backend.

    Args:
        circ: qiskit QuantumCircuit to be executed.
        backend: qiskit Aer backend to run the circuit on

    Returns:
        counts of the measurement results
    """
    qc = transpile(circ, backend)
    job = backend.run(qc, shots=1024)
    return job.result().get_counts(circ)

    
def approximate_grover(n_qubits, oracle, iterations=1, theta=np.pi/2):
    """
    Implements an approximate Grover search algorithm with a parameterized circuit.
    
    Args:
        n_qubits: The number of qubits in the circuit.
        oracle: The oracle function that marks the solution state.
        iterations: The number of iterations of the Grover operator.
        theta: The angle parameter for the Grover operator.
    
    Returns:
        A QuantumCircuit implementing the approximate Grover search.
    """
    qr = QuantumRegister(n_qubits)
    cr = ClassicalRegister(n_qubits)
    qc = QuantumCircuit(qr, cr)
    # Initialization
    for i in range(n_qubits):
        qc.h(qr[i])
    # Grover operator
    for _ in range(iterations):
        qc.append(oracle, qr)
        # Diffusion operator
        for i in range(n_qubits):
            qc.h(qr[i])
        for i in range(n_qubits):
            qc.x(qr[i])
        qc.h(qr[n_qubits - 1])
        qc.mcx(list(range(n_qubits - 1)), qr[n_qubits - 1])
        qc.h(qr[n_qubits - 1])
        for i in range(n_qubits):
            qc.x(qr[i])
        for i in range(n_qubits):
            qc.h(qr[i])
    qc.measure(qr, cr)
    return qc


def create_oracle(s):
    """
    Creates a Grover's oracle for a specific bitstring.
    
    Args:
        s: The bitstring to be marked by the oracle.
    
    Returns:
        A QuantumCircuit representing the oracle.
    """
    n_qubits = len(s)
    qr = QuantumRegister(n_qubits)
    qc = QuantumCircuit(qr)
    # Apply X gates to flip qubits corresponding to '0' in the target bitstring
    for i in range(n_qubits):
        if s[i] == '0':
            qc.x(qr[i])
    # Apply multi-controlled-Z gate to flip the phase of the target state
    qc.h(qr[n_qubits - 1])
    qc.mcx(list(range(n_qubits - 1)), qr[n_qubits - 1])
    qc.h(qr[n_qubits - 1])
    # Apply X gates again to revert the initial flips
    for i in range(n_qubits):
        if s[i] == '0':
            qc.x(qr[i])
    return qc


def permutation_grover(t, permutation_function):
    """
    Finds the original bitstring 's' given a permuted bitstring 't' and the permutation function.
    
    Args:
        t: The permuted bitstring.
        permutation_function: A function that applies the permutation to a bitstring.
    
    Returns:
        The original bitstring 's'.
    """
    n_qubits = len(t)
    # Define the oracle that checks if a given candidate bitstring 's' produces 't' when permuted.
    def oracle_function(candidate_s):
        permuted_candidate = permutation_function(candidate_s)
        return permuted_candidate == t
    # Iterate through all possible bitstrings and check if they produce 't' when permuted.
    def create_oracle_from_function(oracle_function):
        for i in range(2**n_qubits):
            candidate_s = bin(i)[2:].zfill(n_qubits)
            if oracle_function(candidate_s):
                oracle_circ = create_oracle(candidate_s)
                return oracle_circ
        return None
    oracle_circ = create_oracle_from_function(oracle_function)
    if oracle_circ is not None:
        grover_circuit = approximate_grover(n_qubits, oracle_circ, iterations=1)
        counts = simulate(grover_circuit, backend)
        most_frequent_outcome = max(counts, key=counts.get)
        best_iterations = 0
        best_probability = 0
        for iterations in range(1, int(np.sqrt(2**len(t)))):
            grover_circuit = approximate_grover(n_qubits, oracle_circ, iterations=iterations)
            counts = simulate(grover_circuit, backend)
            if counts:
                most_frequent_outcome = max(counts, key=counts.get)
                probability = counts[most_frequent_outcome] / 1024
                if probability > best_probability:
                    best_probability = probability
                    best_iterations = iterations
        return most_frequent_outcome, best_iterations