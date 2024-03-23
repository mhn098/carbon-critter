import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { AppModule } from '../../app.module';
import { CCService } from '../cc.service';

@Component({
  selector: 'app-analytics',
  standalone: true,
  imports: [],
  templateUrl: './analytics.component.html',
  styleUrl: './analytics.component.css'
})
export class AnalyticsComponent {
  public static Route = {
    path: 'cc/analytics',
    title: 'Analytics',
    component: AnalyticsComponent,
    canActivate: []
  };
constructor(
  public ccService: CCService
) {}
}