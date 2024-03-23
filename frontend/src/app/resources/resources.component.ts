import { Component } from '@angular/core';

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
  public functionService: ResourcesComponent
) {}
}
