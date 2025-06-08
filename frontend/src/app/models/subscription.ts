export interface Subscription {
  id?: number;
  start_date: string;   // YYYY-MM-DD
  end_date: string;     // YYYY-MM-DD
  format: 'PDF' | 'HTML' | 'BOTH';
  active: boolean;
}
