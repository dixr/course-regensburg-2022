from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
    #token='',
)

h = {}

# Ergänzen Sie hier die Werte der 
# anderen Koppler in der Form
# (qubit1, qubit2): Kopplerwert,
J = {
    (0,4): +1,  # Beispiel
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
)

dwave.inspector.show(response)
