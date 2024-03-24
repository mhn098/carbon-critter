import { Injectable } from '@angular/core';
import { Observable, OperatorFunction, ReplaySubject, map } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class Service {
  constructor(protected http: HttpClient) {
  }
  createUser(userData: String): any{
    this.http.post<any>('/api/pet', userData)
  }
  get_answer(question: String): String {
    return this.http.get<String>('/api/pet/{question}')
  }
}