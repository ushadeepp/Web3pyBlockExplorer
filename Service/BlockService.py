from Helper.helper import *


def getBlock(w3,blockNumber):
    return w3.eth.getBlock(blockNumber)


# To get the transactions in blocks range
def getTransactionHashList(w3,startBlock,EndBlock):
    transactionsHashList=[]
    for i in range(startBlock,EndBlock):
        currentBlock = w3.eth.getBlock(i)
        transactionsHashList.extend(currentBlock['transactions'])
    return transactionsHashList


def getBlockList(w3,startBlock,endBlock):
    resultList=[]
    if startBlock<0:
        startBlock=0
    for i in range(endBlock,startBlock-1,-1):
        resultList.append(toDict(getBlock(w3,i)))
    return resultList



def getLatestBlockList(w3,listSize):
    resultList=[]
    resultList.append(toDict(w3.eth.getBlock('latest')))
    endBlock=resultList[0]['number']-1
    if endBlock-listSize+2>=0:
        startBlock=endBlock-listSize+2
    else:
        startBlock=0
    for i in range(endBlock,startBlock-1,-1):
        resultList.append(toDict(getBlock(w3,i)))
    return resultList
