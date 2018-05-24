import numpy as np
import pandas as pd
from functools import reduce

class DIC:
    """
    Delineamento Inteiramente casualizado
    """

    def __init__(self, file_csv_path: str):
        self._file_csv_path = file_csv_path
        self._result = None
    
    result = property(lambda self: self._result)

    def calculate(self):
        res = {'CAUSA DA VARIAÇÃO': ['Tratamentos', 'Resíduo', 'Total']}

        table = pd.read_csv(self._file_csv_path, sep=',')
        data = np.array(table, np.float64)

        del table

        I = len(data[0])
        J = len(data)

        res['G.L.'] = self._calculate_GL(data, I, J)
        res['S.Q.'] = self._calculate_SQ(data, I, J)
        res['Q.M.'] = self._calculate_QM(res['S.Q.'], I, J)

        self._result = pd.DataFrame(data=res)
    
    def _calculate_GL(self, data, I, J):
        GL_trat = I - 1
        GL_residuo = I * (J - 1)
        GL_total = (I * J) - 1

        return [GL_trat, GL_residuo, GL_total]

    def _calculate_SQ(self, data, I, J):
        C = np.sum([np.sum([x for x in y]) for y in data]) ** 2
        C = C / (I * J)

        SQ_trat = (1 / J) * sum([sum([data[j][i] for j in range(J)]) ** 2 for i in range(I)]) - C
        SQ_total = sum([sum([data[j][i] ** 2 for j in range(J)]) for i in range(I)]) - C
        SQ_residuo = SQ_total - SQ_trat

        return [SQ_trat, SQ_residuo, SQ_total]
    
    def _calculate_QM(self, SQ, I, J):
        QM_trat = SQ[0] / (I - 1)
        QM_residuo = SQ[1] / (I * (J - 1))

        return [QM_trat, QM_residuo, ""]