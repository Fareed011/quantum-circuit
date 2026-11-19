
import pennylane as qml

dev = qml.device("braket.local.qubit", wires=2)


qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])

print(circuit())