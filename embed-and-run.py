#!/usr/bin/env python3

from __future__ import print_function  # allow it to run on python2 and python3

import numpy as np
from dwave.system.samplers import DWaveSampler
from dwave.system import EmbeddingComposite, LazyFixedEmbeddingComposite

# load matrix
qubomatrix = np.loadtxt('qubomatrix.txt')
print('Loaded matrix:\n', qubomatrix, '\n')

# convert into QUBO
qubo = {(i,i):0.0 for i in range(len(qubomatrix))}  # necessary to keep the order of the sample columns consistent
for index,value in np.ndenumerate(qubomatrix):
    if value != 0:
        qubo[index] = value
print('Converted matrix into QUBO for D-Wave:\n', qubo, '\n')

# embed and run on the D-Wave with 1000 reads
sampler = LazyFixedEmbeddingComposite(DWaveSampler())

response = sampler.sample_qubo(qubo, num_reads=1000, chain_strength=2.0, annealing_time=1)  # NOTE: setting chain_strength and annealing_time explicitly
print('Response from the D-Wave:\n', response, '\n')
print('Embedding\n', sampler.embedding, '\n')
print('Nodelist\n', sampler.nodelist, '\n')
print('Edgelist\n', sampler.edgelist, '\n')
print('Adjacency\n', sampler.adjacency, '\n')

# save results in results.txt
with open('results.txt','w') as file:
    file.write('energy\tnum_occurrences\tsample\n')
    for sample, energy, num_occurrences, cbf in response.data():
        newsample = np.array([value for key,value in sorted(sample.items())])  # rearrange the samples so that the computed energy matches
        file.write('%f\t%d\t%s\n' % (energy, num_occurrences, np.array2string(newsample).replace('\n','')))
    print('Saved results in results.txt')

with open('embedding.txt','w') as file:
    file.write('logicalqubit\tphysicalqubits\n')
    for logicalqubit, physicalqubits in sampler.embedding.items():
        file.write('%d\t%s\n' % (logicalqubit, physicalqubits))
    print('Saved embedding in embedding.txt')
