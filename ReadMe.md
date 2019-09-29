# Ethereum Block Explorer with web3py
This is an easily configurable & quickly runnable Block Explorer for Ethereum network (preferred private Ethereum networks) developed using web3py & Angular.<br/>Backend is designed with Api's which can be consumed by existing systems.

### Steps to Run:
Backend Flask Server:
1) Make sure Python is installed with Version above 3.0.0
2) Install Packages using pip install -r requirements.txt
3) Configure your Ethereum node RPC end point in Configure.py inside Configure Package
4) Run Application : python Web3PyFlask.py


Front end:
<br>
Note: Prerequsites: NodeJs & Angular

1) Ensure NodeJs is installed in your machine.
To check if node is installed run: node -v in command line. If it returns the version, then node is installed. If not, visit NodeJs official website for installation instructions.
2) After installing NodeJs, install Angular. 
  run : npm install @angular/cli
3) After installing the requirements, go into the explorerUi folder
  run: cd explorerUi
4) run: npm install - to install the dependencies.
5) run: ng serve - to host explorer in your local system.
6) Open any web browser and visit "http://localhost:4200/explorer"

### List of Api's:
/getBlockList/\<startBlockNumber\>/\<endBlockNumber\> : to get the Block details of the given range.

/getBlock/\<blockNumber\> : get Block details of given blockumber

/getTransaction/\<txhash\> : get transaaction details of given transaction hash

/getTransactionList/\<startBlock\>/\<offSet\> : get recent transactions staring from given block and offset is no of recent transactions you want to skip in the starting block.

/getBlockListLatest  : get recent 5 blocks (5 is the default window size given for front end, can change that from Configure.py if required).

### Application:
![Alt text](./UiImages/1.png?raw=true "BlockExporer")
Block explorer home screen.

![Alt text](./UiImages/2.png?raw=true "Transactions")
Fetching individual transaction details by clicking on transaction hash.


![Alt text](./UiImages/3.png?raw=true "Blockdetails")
Block search based on Block number.

![Alt text](./UiImages/4.png?raw=true "Full Block details")
Full Block details display.


There you go! Happy Exploring..!!.
