import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
  })
};

@Injectable({
  providedIn: 'root'
})
export class ExplorerService {

  url = 'http://192.168.1.5:5000/';

  constructor(
    private http: HttpClient
  ) { }

  getLatestBlock() {
    return this.http.get(this.url + 'getBlockListLatest', httpOptions).pipe(
      catchError(this.handleError)
    );
  }

  getTransaction(data: any) {
    return this.http.get(this.url + 'getTransaction/' + data, httpOptions).pipe(
      catchError(this.handleError)
    );
  }

  getBlockById(data: any) {
    return this.http.get(this.url + 'getBlock/' + data, httpOptions).pipe(
      catchError(this.handleError)
    );
  }

  getBlockStartEnd(start: any, end: any) {
    return this.http.get(this.url + 'getBlockList/' + start + '/' + end, httpOptions).pipe(
      catchError(this.handleError)
    );
  }

  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error.message);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    // return an observable with a user-facing error message
    return throwError(
      'Something bad happened; please try again later.');
  };

}
