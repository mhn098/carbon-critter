import { Component } from '@angular/core';

@Component({
  selector: 'app-analytics',
  standalone: true,
  imports: [],
  templateUrl: './analytics.component.html',
  styleUrl: './analytics.component.css'
})
export class AnalyticsComponent {
  public static Route = {
    path: 'analytics',
    title: 'Analytics',
    component: AnalyticsComponent,
    canActivate: []
  };
constructor(
  public functionService: AnalyticsComponent
) {}
}