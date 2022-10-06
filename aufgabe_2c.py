from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector

sampler = EmbeddingComposite(DWaveSampler(
    solver='DW_2000Q_6',
    #token='',
))

h = {}

J = {
    ('Lisa','Timo'): 3,
    # Ergänzen Sie hier die Werte 
    # der anderen Koppler
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
    chain_strength=1,  # hiermit müssen Sie
                       # rumspielen um
                       # gute Lösungen zu
                       # bekommen
    annealing_time=20,  # diesen Wert
                        # können Sie zstl.
                        # ändern um bessere
                        # Lösungen zu 
                        # bekommen 
)
dwave.inspector.show(response)