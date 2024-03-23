import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { AppModule } from '../../app.module';
import { CCService } from '../cc.service';

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
  public ccService: CCService
) {}
}
