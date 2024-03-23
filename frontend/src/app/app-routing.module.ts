import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes } from '@angular/router';
import { SignInComponent } from './cc/sign-in/sign-in.component';
import { SignUpComponent } from './cc/sign-up/sign-up.component';
import { PetComponent } from './cc/pet/pet.component';
import { ResourcesComponent } from './cc/resources/resources.component';
import { CommunityComponent } from './cc/community/community.component';
import { AnalyticsComponent } from './cc/analytics/analytics.component';

export const routes: Routes = [
  AnalyticsComponent.Route,
  CommunityComponent.Route,
  SignInComponent.Route,
  SignUpComponent.Route,
  PetComponent.Route,
  ResourcesComponent.Route,
{
  path: 'analytics',
  title: 'Analytics',
  loadComponent: () =>
    import('./cc/analytics/analytics.component').then(
      (m) => m.AnalyticsComponent
    )
},
{
  path: 'community',
  title: 'Community',
  loadComponent: () =>
    import('./cc/community/community.component').then(
      (m) => m.CommunityComponent
    )
},
{
  path: 'pet',
  title: 'Pet',
  loadComponent: () =>
    import('./cc/pet/pet.component').then(
      (m) => m.PetComponent
    )
},
{
  path: 'resources',
  title: 'Resources',
  loadComponent: () =>
    import('./cc/resources/resources.component').then(
      (m) => m.ResourcesComponent
    )
},
{
  path: 'sign-in',
  title: 'SignIn',
  loadComponent: () =>
    import('./cc/sign-in/sign-in.component').then(
      (m) => m.SignInComponent
    )
},
{
  path: 'sign-up',
  title: 'SignUp',
  loadComponent: () =>
    import('./cc/sign-up/sign-up.component').then(
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
