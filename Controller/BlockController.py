from flask import Flask
from flask_cors import CORS, cross_origin
import json
from Config.Config import *
from Service.BlockService import *
from Service.TransactionService import *
from Helper.helper import *

import web3
from web3 import Web3
from web3.contract import ConciseContract
from web3.middleware import geth_poa_middleware

app = Flask(__name__)
CORS(app, support_credentials=True)
w3 = Web3(Web3.HTTPProvider(Config.RpcConnection))
# w3.middleware_stack.inject(geth_poa_middleware, layer=0)   


@app.route('/getBlock/<blockNumber>')
@cross_origin(supports_credentials=True)
def getBlockController(blockNumber):
    result=getBlock(w3,int(blockNumber))
    return toDict(result)

@app.route('/getBlockList/<startBlockNumber>/<endBlockNumber>')
@cross_origin(supports_credentials=True)
def getBlockListController(startBlockNumber,endBlockNumber):
    return json.dumps(getBlockList(w3,int(startBlockNumber),int(endBlockNumber)))

@app.route('/getBlockListLatest')
@cross_origin(supports_credentials=True)
def getBlockListLatestController():
    return json.dumps(getLatestBlockList(w3,Config.FrontEndWindowSize))

@app.route('/getTransaction/<txhash>')
@cross_origin(supports_credentials=True)
def getTransactionController(txhash):
    # 0x2e01ef55de66c8d99c61b56e70da12dc442c23f83e8a6a9ed021b215e2467209
    result=getTransaction(w3,txhash)
    return toDict(result)

@app.route('/getTransactionList/<startBlock>/<offSet>')
@cross_origin(supports_credentials=True)
def getTransactionListController(startBlock,offSet):
    app.logger.info('Controller hit') 
    # recentTransactionList(app,w3,2199491,0,5)  
    return json.dumps(recentTransactionList(app,w3,int(startBlock),int(offSet),Config.FrontEndWindowSize))
