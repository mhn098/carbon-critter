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
  private router: Router,
  public ccService: CCService
) {}

public goAnalytics() {
  this.router.navigate(['analytics']);
}

public goCommunity() {
  this.router.navigate(['community']);
}

public goPet() {
  this.router.navigate(['pet']);
}

public goResources() {
  this.router.navigate(['resources']);
}

public goSignOut() {
  this.router.navigate(['sign-out']);
}

}