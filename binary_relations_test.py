from binary_relations import *

assert is_reflexive_mat([ [False] ]) == False   # m1
assert is_reflexive_mat([ [True] ]) == True  # m2
assert is_reflexive_mat([ [False, False],
                          [False, False] ]) == False  # m3

assert is_reflexive_mat([ [True, True],
                          [True, True] ]) == True  # m4

assert is_reflexive_mat([ [True, True],
                          [False, True] ]) == True  # m5

assert is_reflexive_mat([ [True, False],
                          [True, True] ]) == True  # m6

assert is_reflexive_mat([ [True, True],
                          [True, False] ]) == False  # m7

assert is_reflexive_mat([ [False, True],
                          [True, True] ]) == False  # m8

assert is_reflexive_mat([ [False, True],
                          [True, False] ]) == False  # m9

assert is_reflexive_mat([ [False, False],
                          [True, False] ]) == False    # m10

assert is_reflexive_mat([ [False, True, True],
                          [True, False, False],
                          [True, True, True] ]) == False    # m11

assert is_reflexive_mat([ [True, True, True],
                          [True, True, True],
                          [True, True, True] ]) == True    # m12