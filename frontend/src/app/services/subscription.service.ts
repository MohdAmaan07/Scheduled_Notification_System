import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Subscription } from '../models/subscription';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class SubscriptionService {
  private base = `${environment.apiUrl}/subscriptions`;

  constructor(private http: HttpClient) {}

  list(): Observable<Subscription[]> {
    return this.http.get<Subscription[]>(`${this.base}/`);
  }

  create(sub: Subscription): Observable<Subscription> {
    return this.http.post<Subscription>(`${this.base}/`, sub);
  }

  update(id: number, sub: Partial<Subscription>): Observable<Subscription> {
    return this.http.patch<Subscription>(`${this.base}/${id}/`, sub);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.base}/${id}/`);
  }
}
