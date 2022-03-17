import networkx as nx
import pandas as pd
edges = pd.DataFrame({'source': [0, 1, 2],
               'target': [2, 2, 3],
               'weight':[1,1,1]})
G = nx.from_pandas_edgelist(edges,edge_attr=True,create_using=nx.DiGraph())
G = nx.from_pandas_edgelist(edges, edge_attr=True)
eigen_centrality = nx.eigenvector_centrality_numpy(G)
bet_centrality = nx.betweenness_centrality(G)
degree_centrality = nx.degree_centrality(G)
degree_coefficient = nx.clustering(G)
from pyvis.network import Network
pyvis_G = Network()
pyvis_G.from_nx(G)
pyvis_G.toggle_physics(True)  #html上でレイアウト動かしたくない場合false
pyvis_G.show("mygraph.html")