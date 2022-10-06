from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector

sampler = EmbeddingComposite(DWaveSampler(
    solver='DW_2000Q_6',
    #token='',
))

h = {}

J = {
    ('Lisa','Timo'): 3,
    ('Lisa','Anna'): 2,
    ('Lisa','Tom'): 6,
    ('Timo','Anna'): 5,
    ('Timo','Tom'): 3,
    ('Anna','Tom'): 5,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
    chain_strength=4,
    annealing_time=100,
)
dwave.inspector.show(response)