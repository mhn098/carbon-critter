import { Component } from '@angular/core';
import { Sign } from 'crypto';

@Component({
  selector: 'app-sign-in',
  standalone: true,
  imports: [],
  templateUrl: './sign-in.component.html',
  styleUrl: './sign-in.component.css'
})
export class SignInComponent {
  public static Route = {
    path: 'sign-in',
    title: 'SignIn',
    component: SignInComponent,
    canActivate: []
  };
constructor(
  public functionService: SignInComponent
) {}
}