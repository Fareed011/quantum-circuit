import pennylane as qml
def circuit(params):
    qml.RX(params[0], wires = 0)
    qml.RY(params[1], wires = 0)
    #qml.RZ(params[2], wires = 0)
    return qml.expval(qml.PauliZ(0)) 

