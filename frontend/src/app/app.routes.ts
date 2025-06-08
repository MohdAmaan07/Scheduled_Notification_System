import { Routes } from '@angular/router';
import { SubscriptionFormComponent } from './components/subscription-form/subscription-form.component';
import { SubscriptionListComponent } from './components/subscription-list/subscription-list.component';
import { ReportHistoryComponent } from './components/report-history/report-history.component';

export const routes: Routes = [
  { path: '', redirectTo: 'subscribe', pathMatch: 'full' },
  { path: 'subscribe', component: SubscriptionFormComponent },
  { path: 'subscriptions', component: SubscriptionListComponent },
  { path: 'history', component: ReportHistoryComponent }
];
