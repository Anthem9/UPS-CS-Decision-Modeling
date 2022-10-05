# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import networkx as nx
import matplotlib.pyplot as plt
# plt.use('TkAgg')

nx.draw(nx.DiGraph([[True,False],[False,True]]) )
# nx.draw([[1,0],[0,1]])
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
