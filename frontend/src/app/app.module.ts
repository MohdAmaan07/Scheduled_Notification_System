import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';

import { AppComponent } from './app.component';
import { routes } from './app.routes';

import { SubscriptionFormComponent } from './components/subscription-form/subscription-form.component';
import { SubscriptionListComponent } from './components/subscription-list/subscription-list.component';
import { ReportHistoryComponent } from './components/report-history/report-history.component';

@NgModule({
  imports: [
    BrowserModule,
    AppComponent,
    SubscriptionFormComponent,
    SubscriptionListComponent,
    ReportHistoryComponent
  ],
  providers: [
    provideRouter(routes)
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
