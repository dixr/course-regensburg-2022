from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
    #token='',
)

# 0 = Lauch
# 4 = Sellerie
# 7 = Erbsen
# 3 = Mais

# ISING:
# E = s0 - s0 s4 + s0 s7 + s3 s4 - s3 s7
# QUBO: (si = 2*xi - 1)
# E = 2 x0 - 4 x0 x4 + 4 x0 x7 + 4 x3 x4 - 4 x3 x7 + 1

Q = {
    (0,0): +2,
    (0,4): -4,
    (0,7): +4,
    (3,4): +4,
    (3,7): -4,
}
response = sampler.sample_qubo(
    Q, 
    num_reads=100,
)
print(response)
dwave.inspector.show(response)