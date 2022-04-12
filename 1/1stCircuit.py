from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

"""
qc_output = QuantumCircuit(8) #circuit w/ 8 qubits
qc_output.measure_all() #output extraction

qc_output.draw(initial_state=True, output='mpl') #draw plot
plt.show() #present circuit
print(qc_output) #present circuit in terminal

sim = Aer.get_backend('aer_simulator') #quantum simulation in classical pc
result = sim.run(qc_output).result()
counts = result.get_counts()
plot_histogram(counts)
plt.show()


qc_encode = QuantumCircuit(8)
qc_encode.x(7) # x == NOT gate, 7th qubit just flipped
qc_encode.measure_all()
qc_encode.draw(output='mpl')
plt.show()

sim = Aer.get_backend('aer_simulator')
result = sim.run(qc_encode).result()
counts = result.get_counts()
plot_histogram(counts)
plt.show() #plot shows 100% prob for 10000000 because the 7th bit was flipped

"""



qu_adder_circuit = QuantumCircuit(4, 2) #init circuit with 4 inputs and 2 outputs

qu_adder_circuit.x(0) #flip bit 0
qu_adder_circuit.x(1) #flit bit 1

qu_adder_circuit.barrier() #barrier between inputs and operations

qu_adder_circuit.cx(0, 2) #store XOR gate result in 3rd bit
qu_adder_circuit.cx(1, 2) #store XOR gate result in 3rd bit

qu_adder_circuit.ccx(0, 1, 3) #AND gate to determine the carry between the 2 bits

qu_adder_circuit.barrier() #barrier between operations and outputs

qu_adder_circuit.measure(2, 0) #measure XOR value and place it in the 1st position
qu_adder_circuit.measure(3, 1) #measure AND value (carry bit) and place it in the 2nd position

qu_adder_circuit.draw(output = 'mpl')
plt.show()


sim = Aer.get_backend('aer_simulator')
qobj = assemble(qu_adder_circuit)
counts = sim.run(qobj).result().get_counts()
plot_histogram(counts) #plot for the probabilites of inputs 1 and 1 (always 10, because reasons)
plt.show()