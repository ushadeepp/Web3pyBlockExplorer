from Helper.helper import *
from Service.BlockService import *
import logging

def getTransaction(w3,txHash):
    return w3.eth.getTransaction(txHash)

def recentTransactionList(app,w3,maxblock,offset,listlen):
    resultList=[]
    app.logger.info('Inside Service transaction list')
    currentBlock=getBlock(w3,maxblock)
    app.logger.info('transactions')
    app.logger.info(currentBlock['transactions'])
    if len(currentBlock['transactions']) > offset:
        j=1
        if len(currentBlock['transactions'])>0:
            while ((len(resultList) < listlen) and (len(currentBlock['transactions'])>=(j+offset))):
                result=toDict(getTransaction(w3,currentBlock['transactions'][-(j+offset)]))
                app.logger.info('result')
                app.logger.info(result)
                resultList.append(result)                
                app.logger.info(resultList)
                j+=1
        
    while ((len(resultList)<listlen) and (maxblock>0)):
        maxblock-=1
        offset=0
        j=1
        currentBlock=getBlock(w3,maxblock)
        app.logger.info('transactions')
        app.logger.info(currentBlock['transactions'])
        app.logger.info(len(resultList))
        if len(currentBlock['transactions'])>0:
            while ((len(resultList)<listlen) and len(currentBlock['transactions'])>=(j+offset)):
                result=toDict(getTransaction(w3,currentBlock['transactions'][-(j+offset)]))
                app.logger.info('result')
                app.logger.info(result)
                resultList.append(result)                
                app.logger.info(resultList)
                j+=1
    return resultList




