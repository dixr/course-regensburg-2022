from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
    #token='',
)

h = {}

J = {
    # Ersetzen Sie hier "0" durch die korrekten Werte der Koppler
    (0,4): 0, (0,5): 0, (0,6): 0, (0,7): 0,
    (1,4): 0, (1,5): 0, (1,7): 0,
    (2,5): 0, (2,6): 0, (2,7): 0,
    (3,4): 0, (3,5): 0, (3,6): 0, (3,7): 0,

    (8,12): 0, (8,13): 0, (8,14): 0, (8,15): 0,
    (9,12): 0, (9,13): 0, (9,14): 0, (9,15): 0,
    (10,13): 0, (10,14): 0, (10,15): 0,
    (11,12): 0, (11,13): 0, (11,14): 0, (11,15): 0,

    (4,12): 0, (6,14): 0, (7,15): 0,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=1000,
)
dwave.inspector.show(response)
