from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
    #token='',
)

h = {0: +1}

# Hier wählen wir:
# 0 = Lauch
# 4 = Sellerie
# 7 = Erbsen
# 3 = Mais
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