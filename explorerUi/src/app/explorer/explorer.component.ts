import { Component, OnInit } from '@angular/core';
import { ExplorerService } from './explorer.service';

@Component({
  selector: 'app-explorer',
  templateUrl: './explorer.component.html',
  styleUrls: ['./explorer.component.css']
})
export class ExplorerComponent implements OnInit {

  blockList: any = [];
  detailedTransaction: any = {};
  detailedBlock: any = {};
  searchText: any;

  constructor(
    private explorerService: ExplorerService
  ) {
    console.log('Im into Explorer');
  }

  ngOnInit() {
    this.getLatestBlock();
  }

  blockMoreDetails(block: any) {
    console.log(block);
    this.detailedBlock = block;
  }

  onNext(blockNo: any) {
    console.log(blockNo);
    const startBlock = blockNo - 5;
    const endBlock = blockNo - 1;
    this.blockList = [];
    this.explorerService.getBlockStartEnd(startBlock, endBlock).subscribe( response => {
      console.log(response);
      this.blockList = response;
    }, error => {
        console.log('Error Occured');
    });
  }

  onBack(blockNo: any) {
    console.log(blockNo);
    const startBlock = blockNo + 1;
    const endBlock = blockNo + 5;
    this.blockList = [];
    this.explorerService.getBlockStartEnd(startBlock, endBlock).subscribe( response => {
      console.log(response);
      this.blockList = response;
    }, error => {
      console.log('Error Occured');
    });
  }

  getLatestBlock() {
    this.blockList = [];
    this.searchText = '';
    this.explorerService.getLatestBlock().subscribe( response => {
      console.log(response);
      this.blockList = response;
    });
  }

  getTransactionById(transactionId: any) {
    console.log(transactionId);
    this.explorerService.getTransaction(transactionId).subscribe( response => {
      console.log(response);
      this.detailedTransaction = response;
    });
  }

  getBlockById(blockNo: any) {
    console.log(blockNo);
    this.blockList = [];
    this.explorerService.getBlockById(blockNo).subscribe(response => {
      this.searchText = '';
      console.log(response);
      this.blockList.push(response);
    });
  }

}
