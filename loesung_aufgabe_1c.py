from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
)

h = {}

# Hier wählen wir:
# Qubit 0 = Lauch
# Qubit 4 = Sellerie
# Qubit 7 = Erbsen
# Qubit 3 = Mais
J = {
    (0,4): -1,
    (0,7): +1,
    (3,4): +1,
    (3,7): -1,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
)

dwave.inspector.show(response)
