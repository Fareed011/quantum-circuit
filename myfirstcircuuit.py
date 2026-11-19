import pennylane as qml

# 1. Create a simulator with one qubit
#dev = qml.device("default.qubit", wires=1)
#new dev makes it have 1k times more shots to get a better estimate of the probabilities
dev = qml.device("default.qubit", wires=1, shots=1000)

# 2. Define the quantum circuit
@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    #return qml.probs(wires=0)
    return qml.counts(wires=0)          

# 3. Execute the circuit
probabilities = circuit()

print("Measurement probabilities:", probabilities)
