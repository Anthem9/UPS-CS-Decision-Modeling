import pandas as pd
import numpy as np


def xlsx_to_csv(file_name):
    data_xlsx = pd.read_excel(file_name, index_col=0)
    data_xlsx.to_csv(file_name[:-4]+"csv", encoding="utf-8")


if __name__ == "__main__":
    xlsx_to_csv("DeMTest.xlsx")
    matrix = np.loadtxt("DeMTest.csv", delimiter=",", skiprows=0)
    matrix = np.array(matrix, dtype=bool)
    # draw_mat(matrix)
    print(matrix)


    print(np.array([
        [True, False, False, False],
        [False, False, False, False],
        [False, True, True, False],
        [False, False, False, False],
    ]))

