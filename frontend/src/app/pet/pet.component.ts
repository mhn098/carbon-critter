import { Component } from '@angular/core';

@Component({
  selector: 'app-pet',
  standalone: true,
  imports: [],
  templateUrl: './pet.component.html',
  styleUrl: './pet.component.css'
})
export class PetComponent {
  public static Route = {
    path: 'pet',
    title: 'Pet',
    component: PetComponent,
    canActivate: []
  };
constructor(
  public functionService: PetComponent
) {}
}