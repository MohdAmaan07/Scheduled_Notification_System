import { Component, OnInit, OnDestroy, ChangeDetectorRef } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Router, NavigationEnd } from '@angular/router';
import { Subscription } from 'rxjs';
import { environment } from '../../../environments/environment';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-report-history',
  standalone: true,
  imports: [
    CommonModule,      
  ],
  templateUrl: './report-history.component.html',
  styleUrls: ['./report-history.component.scss']
})
export class ReportHistoryComponent implements OnInit, OnDestroy {
  history: any[] = [];
  routerSubscription?: Subscription;

  constructor(
    private http: HttpClient, 
    private router: Router,
    private cd: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.fetchReports();

    this.routerSubscription = this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.fetchReports();
      }
    });
  }

  fetchReports() {
    const params = new HttpParams()
      .set('start_date', '2025-06-01')
      .set('end_date', '2025-06-08');

    this.http.get<{ reports: any[] }>(`${environment.apiUrl}/reports/history/`, { params }).subscribe({
      next: data => {
        this.history = data.reports;
        this.cd.detectChanges(); // Force UI update
      },
      error: err => console.error('Error fetching report history:', err)
    });
  }

  ngOnDestroy() {
    this.routerSubscription?.unsubscribe();
  }
}
