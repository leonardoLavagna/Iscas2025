from qiskit_aer import Aer, AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeVigoV2


shots = 1024
tvd = 0.40234375
noisy = False
if noisy:
    backend = FakeVigoV2()
else: 
    backend = AerSimulator()
