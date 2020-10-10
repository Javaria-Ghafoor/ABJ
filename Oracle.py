import qiskit as q
from matplotlib import style
import math

# Build an oracle for a balanced function
oracle1_q = q.QuantumRegister(3)
oracle1_circ = q.QuantumCircuit(oracle1_q, name='oracle1')
oracle1_circ.cx(oracle1_q[0], oracle1_q[2])
oracle1_circ.cx(oracle1_q[1], oracle1_q[2])

# Convert to a gate and stick it into an arbitrary place in the bigger circuit
oracle1_inst = oracle1_circ.to_instruction()

# Build an oracle for a constant function
oracle2_q = q.QuantumRegister(3)
oracle2_circ = q.QuantumCircuit(oracle1_q, name='oracle2')
# Convert to a gate and stick it into an arbitrary place in the bigger circuit
oracle2_inst = oracle2_circ.to_instruction()




