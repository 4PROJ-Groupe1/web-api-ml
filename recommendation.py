import numpy as np
import pandas as pd
from apyori import apriori
import pickle


def generateRules():
    df = pd.read_csv("Classeur1.csv", header=None)

    ordersWithNan = df.values.tolist()

    orders = []
    for i in range (0,len(ordersWithNan)):
        tempList = []
        for j in range (0,31):
            if(str(ordersWithNan[i][j]) != 'nan'):
                tempList.append(ordersWithNan[i][j])
        if(len(tempList) > 0):
            orders.append(tempList)

    return updateRules(orders)





def updateRules(orders):
    rules = apriori(orders,min_support=0.006, min_confidence=0.25,min_length=2)

    listRules = list(rules)

    dumpRules(listRules)

    return listRules



def dumpRules(listRules):
    dictionnary = {"rules": []}
    for i in range (0,len(listRules)):
        if len(listRules[i][2][0].items_base) > 0:
            lhs = list(listRules[i][2][0].items_base)[0]
            rhs = list(listRules[i][2][0].items_add)[0]
            confidence = listRules[i][2][0][3]
            dictionnary['rules'].append({'lhs': lhs, 'rhs': rhs, 'confidence': confidence})
    with open('rules.txt', 'wb') as dumpFile:
       pickle.dump(dictionnary, dumpFile)



def loadRules():
    try:
        with open('rules.txt', 'rb') as dumpFile:
            dictionnary = pickle.load(dumpFile)
            return dictionnary['rules']
    except:
        return generateRules()

def recommend(article):
    listrules = loadRules()
    recommendationList = []
    for i in range (0,len(listrules)):
        if article == listrules[i]['lhs']:
            recommendationList.append(i)

    bestConfidence = 0
    articleToRecommend = 0
    tempItem = 0

    for j in range (0,len(recommendationList)):
        tempItem = recommendationList[j]
        if listrules[tempItem]['confidence'] > bestConfidence:
            bestConfidence = listrules[tempItem]['confidence']
            articleToRecommend = tempItem
    return listrules[articleToRecommend]['rhs']




#print(recommend('chicken'))
