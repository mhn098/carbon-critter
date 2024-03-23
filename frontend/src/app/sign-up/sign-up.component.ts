import { Component } from '@angular/core';

@Component({
  selector: 'app-sign-up',
  standalone: true,
  imports: [],
  templateUrl: './sign-up.component.html',
  styleUrl: './sign-up.component.css'
})
export class SignUpComponent {
  public static Route = {
    path: 'sign-up',
    title: 'SignUp',
    component: SignUpComponent,
    canActivate: []
  };
constructor(
  public functionService: SignUpComponent
) {}
}
