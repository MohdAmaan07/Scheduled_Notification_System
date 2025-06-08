import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { SubscriptionService } from '../../services/subscription.service';
import { Subscription } from '../../models/subscription';

@Component({
  selector: 'app-subscription-form',
  standalone: true,
  imports: [
    CommonModule,         
    ReactiveFormsModule   
  ],
  templateUrl: './subscription-form.component.html',
  styleUrls: ['./subscription-form.component.scss']
})
export class SubscriptionFormComponent implements OnInit {
  form!: FormGroup;
  submitting = false;

  constructor(private fb: FormBuilder, private svc: SubscriptionService) {}

  ngOnInit() {
    this.form = this.fb.group({
      start_date: ['', Validators.required],
      end_date: ['', Validators.required],
      report_format: ['PDF', Validators.required],
    });
  }

  onSubmit() {
    if (this.form.invalid) return;
    this.submitting = true;
    const payload: Subscription = this.form.value;
    console.log('Payload being submitted:', this.form.value);

    this.svc.create(payload).subscribe({
      next: () => {
        alert('Subscribed successfully!');
        this.form.reset({ format: 'PDF', active: true });
      },
      error: () => alert('Error subscribing.'),
      complete: () => this.submitting = false
    });
  }
}
