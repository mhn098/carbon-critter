import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes } from '@angular/router';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { PetComponent } from './pet/pet.component';
import { ResourcesComponent } from './resources/resources.component';
import { CommunityComponent } from './community/community.component';
import { AnalyticsComponent } from './analytics/analytics.component';

export const routes: Routes = [
  AnalyticsComponent.Route,
  CommunityComponent.Route,
  SignInComponent.Route,
  SignUpComponent.Route,
  PetComponent.Route,
  ResourcesComponent.Route,
{
  path: 'community',
  title: 'Community',
  loadComponent: () =>
    import('./community/community.component').then(
      (m) => m.CommunityComponent
    )
},
{
  path: 'pet',
  title: 'Pet',
  loadComponent: () =>
    import('./pet/pet.component').then(
      (m) => m.PetComponent
    )
},
{
  path: 'resources',
  title: 'Resources',
  loadComponent: () =>
    import('./resources/resources.component').then(
      (m) => m.ResourcesComponent
    )
},
{
  path: 'sign-in',
  title: 'SignIn',
  loadComponent: () =>
    import('./sign-in/sign-in.component').then(
      (m) => m.SignInComponent
    )
},
{
  path: 'sign-up',
  title: 'SignUp',
  loadComponent: () =>
    import('./sign-up/sign-up.component').then(
      (m) => m.SignUpComponent
    )
}
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule
  ]
})
export class AppRoutingModule { }
