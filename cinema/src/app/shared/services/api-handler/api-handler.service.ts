import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiHandlerService {

  constructor(private http: HttpClient) { }

  fetchData(endpoint: string, data = {}): Observable<any> {
    return this.http.get<any>(endpoint, data = data);
  }

  fetchList(endpoint: string, data = {}): Observable<any[]> {
    return this.http.get<any[]>(endpoint, data = data);
  }

  postData(endpoint, data) {
    return this.http.post(endpoint, {
      data: data
    });
  }
}
