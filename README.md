# Iscas2025

Implementations for the project "Trade-offs in Cryptosystems by Boolean and Quantum Circuits" presented at the conference [Iscas 2025](https://2025.ieee-iscas.org/).

## What's in here?
Here you can find the code we used in the project.
* `utilities` contains functions to carry out random walks, Grover searches and frequency attacks on the Caesar's cipher.
* `notebooks` contains the script we used to get the main results in the project, as well as to get the parameter `tvd` in the configuration file (i.e. the total variation distance metric).
* `config.py` is a configuration file used to specify some settings (e.g. the noise model).
* `requirements.txt` contains the requirements (install the file before using the code in this repository).
* `LICENSE.txt`: MIT License.

## Use this repository
If you want to use the code in this repository in your projects, please cite explicitely our work, and
* Clone the repository with `git clone https://github.com/leonardoLavagna/Iscas2025`
* Install the requirements with `pip install -r requirements.txt`

## Contributing
We welcome contributions to enhance the functionality and performance of the models. Please submit pull requests or open issues for any improvements or bug fixes.

## License
This project is licensed under the MIT License.

## Citation
Cite this repository or one of the associated papers 
```
@INPROCEEDINGS{Lav25,
  author={Lavagna, Leonardo and De Falco, Francesca and Ceschini, Andrea and Rosato, Antonello and Panella, Massimo},
  booktitle={2025 IEEE International Symposium on Circuits and Systems (ISCAS)}, 
  title={Trade-offs in Cryptosystems by Boolean and Quantum Circuits}, 
  year={2025},
  volume={},
  number={},
  pages={1-5},
  keywords={Fault tolerance;Circuits and systems;Fault tolerant systems;Quantum mechanics;Focusing;Encryption;Noise measurement;Quantum circuit;Integrated circuit modeling;Circuit theory},
  doi={10.1109/ISCAS56072.2025.11043205}}
``` 

