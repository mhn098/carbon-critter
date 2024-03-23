import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { AppModule } from '../../app.module';
import { CCService } from '../cc.service';

@Component({
  selector: 'app-resources',
  standalone: true,
  imports: [],
  templateUrl: './resources.component.html',
  styleUrl: './resources.component.css'
})
export class ResourcesComponent {
  public static Route = {
    path: 'resources',
    title: 'Resources',
    component: ResourcesComponent,
    canActivate: []
  };
constructor(
  public ccService: CCService
) {}
}
