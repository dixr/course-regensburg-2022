from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
)

h = {}

J = {
    (0,4): -1, (0,5): +1, (0,6): -1, (0,7): +1,
    (1,4): +1, (1,5): -1, (1,7): -1,
    (2,5): +1, (2,6): -1, (2,7): -1,
    (3,4): +1, (3,5): -1, (3,6): -1, (3,7): +1,

    (4,12): +1, (6,14): +1, (7,15): -1,

    (4,12): +1, (6,14): +1, (7,15): -1,
    (8,12): -1, (8,13): +1, (8,14): -1, (8,15): +1,
    (9,12): +1, (9,13): -1, (9,14): +1, (9,15): +1,
    (10,13): -1, (10,14): +1, (10,15): -1,
    (11,12): -1, (11,13): +1, (11,14): -1, (11,15): +1,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=1000,
)
dwave.inspector.show(response)
