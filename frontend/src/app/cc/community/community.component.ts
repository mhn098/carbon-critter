import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { AppModule } from '../../app.module';
import { CCService } from '../cc.service';

@Component({
  selector: 'app-community',
  standalone: true,
  imports: [],
  templateUrl: './community.component.html',
  styleUrl: './community.component.css'
})
export class CommunityComponent {
  public static Route = {
    path: 'community',
    title: 'Community',
    component: CommunityComponent,
    canActivate: []
  };
constructor(
  public ccService: CCService
) {}
}
