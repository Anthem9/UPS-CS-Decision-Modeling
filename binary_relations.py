# from numpy import ndarry
from soft import draw_mat
import networkx as nx
# import matplotlib
# matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt


class BinaryRelationsMatrix():

    def __init__(self, matrix):
        self.matrix = matrix
        self.npmatrix = np.matrix(self.matrix)
        self.graph = nx.from_numpy_matrix(self.npmatrix)
        nx.draw(self.graph)
        plt.show()


    def is_reflexive_matrix(self):
        '''
        if for every x ∈ X, x R x;
        :return: True
        '''
        n = len(self.matrix)
        for i in range(n):
            if not self.matrix[i][i]:
                return False
        return True

    def is_irreflexive_matrix(self):
        '''
        if for every x ∈ X, not(x R x)
        :return: True
        '''
        n = len(self.matrix)
        for i in range(n):
            if self.matrix[i][i]:
                return False
        return True

    def is_complete_matrix(self):
        '''
        if for every x, y ∈ X, x R y or y R x (possibly both);
        :return: True
        '''
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if not (self.matrix[i][j] or self.matrix[j][i]):
                    return False
        return True

    # AsymmetricCheck
    def is_asymmetric_matrix(self):
        '''
        if for every x, y ∈ X, [x R y ⇒ not(y R x)];
        :return: True
        '''
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j]:
                    if not (not self.matrix[j][i]):
                        return False
        return True

    # SymmetricCheck

    def is_symmetric_matrix(self):
        '''
        if for every x, y ∈ X, [x R y ⇒ y R x];
        :return: True
        '''
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j]:
                    if not self.matrix[j][i]:
                        return False
        return True

    # AntisymmetricCheck
    def is_antisymmetric_matrix(self):
        """
        if for every x, y ∈ X, [x R y and y R x =⇒ x = y];
        :return: Ture
        """
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] and self.matrix[j][i]:
                    if not i == j:
                        return False
        return True

    # TransitiveCheck
    def is_transitive_matrix(self):
        """
        if for every x, y, z ∈ X, [x R y and y R z =⇒ x R z];
        :return: True
        """
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if self.matrix[i][j] and self.matrix[j][k]:
                        if not self.matrix[i][k]:
                            return False
        return True

    # NegativetransitiveCheck

    def is_negative_transitive_matrix(self):
        """
        if for every x, y, z ∈ X, [not(x R y) and not(y R z) =⇒ not(x R z)];
        :return: True
        """
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (not self.matrix[i][j]) and (not self.matrix[j][k]):
                        if not (not self.matrix[i][k]):
                            return False
        return True

    # CompleteOrderCheck
    def is_complete_order_matrix(self):
        """
        A binary relation R on X is a total order or a linear order if R is complete, antisymmetric and transitive.
        :return:
        """
        return self.is_complete_matrix() and self.is_antisymmetric_matrix() and self.is_transitive_matrix()

    # CompletePreOrderCheck
    def is_complete_preorder_matrix(self):
        """
        A binary relation R on X is a weak order or a complete preorder if R is complete and transitive.
        """
        return self.is_complete_matrix() and self.is_transitive_matrix()

    # Preorder
    def is_preorder_matrix(self):
        """
        A binary relation R on X is a preorder if R is reflexive and transitive.
        :return: True
        """
        return self.is_reflexive_matrix() and self.is_transitive_matrix()

    def is_equivalence_relation_matrix(self):
        """
        A binary relation R on X that is reflexive, symmetric and transitive is called an equivalence relation.
        :return: True
        """
        return self.is_reflexive_matrix() and self.is_symmetric_matrix() and self.is_transitive_matrix()

    # StrictRelation

    def get_strict_relation_part(self):
        """
        For a binary relation R on X, we define a symmetric part I and an asymmetric
        part P as follows: for all x, y ∈ X
        x I y if [x R y and y R x]
        x P y if [x R y and not(y R x)]
        :return: n * n Matrix
        """
        strict_part = []
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if  self.matrix[i][j] and self.matrix[j][i]:
                    strict_part[i][j] = True
                else:
                    strict_part[i][j] = False
        return strict_part

    # IndifferenceRelation
    def get_indifference_relation_part(self):
        """
        For a binary relation R on X, we define a symmetric part I and an asymmetric
        part P as follows: for all x, y ∈ X
        x I y if [x R y and y R x]
        x P y if [x R y and not(y R x)]
        :return: n * n Matrix
        """
        indifference_part = []
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] and not (self.matrix[j][i]):
                    indifference_part[i][j] = True
                else:
                    indifference_part[i][j] = False
        return indifference_part

    # Indegree
    def get_indegree(self, i):
        indegree = 0
        n = len(self.matrix)
        for j in range(n):
            if self.matrix[j][i] == True:
                indegree = indegree + 1
        return indegree

    # Topologicalsorting
    def topological_sort(self):
        """
        Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of
        vertices such that for every directed edge uv, vertex u comes before v in the
        ordering.
        Topological Sorting for a graph is not possible if the graph is not a DAG.
        :return:
        """
        n = len(self.matrix)
        L = []
        S = list(range(n))
        while S:
            for i in S:
                if self.get_indegree(i) == 0:
                    L.append(i)
                    S.remove(i)
                    for j in range(n):
                        self.matrix[i][j] = False
        return L


if __name__ == '__main__':
    # test = BinaryRelationsMatrix([ [False, False],
    #                       [False, False] ])
    test = BinaryRelationsMatrix([ [True, True, True],[True, True, True],[True, True, True] ])
    print(test.is_reflexive_matrix())
    print(test.is_complete_matrix())
    print(test.is_irreflexive_matrix())
    print(test.topological_sort())
