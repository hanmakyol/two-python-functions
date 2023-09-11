""" 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5] """

list_1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def duzlestirici(list_1):
    duz = []
    for item in list_1:
        if isinstance(item, list):
            duz.extend(duzlestirici(item))
        else:
            duz.append(item)
    return duz


cikti_1 = duzlestirici(list_1)
print(cikti_1)


"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

list_2 = [[1, 2], [3, 4], [5, 6, 7]]

def terslestirici(list_2):
    ters = []
    for item in list_2[::-1]:
        if isinstance(item,list):
            ters.append(terslestirici(item))
        else:
            ters.append(item)
    return ters

cikti_2 = terslestirici(list_2)
print(cikti_2)