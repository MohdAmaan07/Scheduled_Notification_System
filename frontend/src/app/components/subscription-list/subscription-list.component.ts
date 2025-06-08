import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { SubscriptionService } from '../../services/subscription.service';
import { Subscription } from '../../models/subscription';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-subscription-list',
  standalone: true,
  imports: [
    CommonModule  
  ],
  templateUrl: './subscription-list.component.html',
  styleUrls: ['./subscription-list.component.scss']
})
export class SubscriptionListComponent implements OnInit {
  subscriptions: Subscription[] = [];

  constructor(private svc: SubscriptionService, private cd: ChangeDetectorRef) {}

  ngOnInit() {
    this.load();
  }

  load() {
    this.svc.list().subscribe(data => {
      this.subscriptions = data;
      this.cd.detectChanges(); // force UI update immediately after data change
    });
  }

  unsubscribe(id: number) {
    this.svc.delete(id).subscribe(() => this.load());
  }

  toggleActive(sub: Subscription) {
    this.svc.update(sub.id!, { active: !sub.active }).subscribe(() => this.load());
  }
}
