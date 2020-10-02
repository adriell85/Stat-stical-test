""" Em estatística, o teste Kolmogorov–Smirnov (também conhecido como teste KS ou teste K–S) é um teste não paramétrico de bondade do ajuste sobre a 
igualdade de distribuições de probabilidade contínuas e unidimensionais que pode ser usado para comparar uma amostra com uma distribuição de 
probabilidade de referência (teste K–S uniamostral) ou duas amostras uma com a outra (teste K–S biamostral). 
Recebe este nome em homenagem aos matemáticos russos Andrei Kolmogorov e Nikolai Smirnov. """

import statistical_tests as st
import file_operations as fo
import numpy as np
import cv2

# Import paths
data1 = '/home/adriell/Documentos/SegmentationMetrics-master/o_ 8_em_csv/KNN.csv'
data2 = '/home/adriell/Documentos/SegmentationMetrics-master/o_ 8_em_csv/RandomForest.csv'



# ---------------------------------------------------------------
# data1=np. asarray([1,90642,2,10288,1,52229,2,61826,1,42738,2,22488,1,69742,3,15435,1,98492,1,99568],np.uint8)
# data2=np. asarray([1,90642,2,10288,1,52229,2,61826,1,42738,2,22488,1,69742,3,15435,1,98492,1,99568],np.uint8)

# st.transf2gaussian()


# Kolmogorov-Smirnov test
print('resultados comogorov')
st.kolmogorov(data1, data2, 3, False)

# print('\n\nresultados students')
# # # Student's t-test
# st.studentst(data1, data2, 1, False)


# print('\n\nresultados friedman')
# # # Friedman test
# st.friedman(data1, data2, 3, False)

# #
# print('\n\nresultados bartlett')
# # # bartelett test
# st.bartlett_test(data1, data2, 3, False)

#
# print('\n\nresultados levene')
# # # levene test
# st.levene_test(data1, data2, 3, False)
#
#
# print('\n\nresultados normal')
# # # normal test
# st.normal_test(data1, 3, False)
# #
# #
# print('\n\nresultados mann_whitney ')
# # # mann_whitney test
# st.Mann_Whitney_test(data1, data2, 3, False)

#
# print('\n\nresultados ranksums ')
# # # ranksums test
# st.ranksums_test(data1, data2, 3, False)


