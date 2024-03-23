import { Component } from '@angular/core';

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
  public functionService: CommunityComponent
) {}
}
