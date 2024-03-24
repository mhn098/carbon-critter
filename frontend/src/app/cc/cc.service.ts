import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CCService{

constructor(
  protected http: HttpClient,
  private router: Router) {}

  pet: Pet = Pet.Temp;
  pet_sound: string = '';
  pet_name: string = '';

  createUser(userData: String) {
    this.http.post<any>('/api/pet', userData)
  }
  get_answer(question: String): Observable<String> {
    return this.http.get<String>(`/api/pet/${question}`)
  }

  public bunny1() {
    this.pet = Pet.Bunny;
    this.pet_sound = 'Squeak!'
    console.log('bunny1!')
  }

  public cat2() {
    this.pet = Pet.Cat;
    this.pet_sound = 'Meow!'
  }

  public dog3() {
    this.pet = Pet.Dog
    this.pet_sound = 'Woof!'
  }

  public hamster4() {
    this.pet = Pet.Hamster
    this.pet_sound = 'Squeak!'
  }

  public chicken5() {
    this.pet = Pet.Chicken
    this.pet_sound = 'Cluck!'
  }

  public fox6() {
    this.pet = Pet.Fox
    this.pet_sound = 'Squeak!'
  }

  public lion7() {
    this.pet = Pet.Lion
    this.pet_sound = 'Roar!'
  }

  public monkey8() {
    this.pet = Pet.Monkey
    this.pet_sound = 'OOO!'
  }

  public elephant9() {
    this.pet = Pet.Elephant
    this.pet_sound = 'Toot!'
  }

  public turtle10() {
    this.pet = Pet.Turtle
    this.pet_sound = 'Hi!'
  }

  public seal11() {
    this.pet = Pet.Seal
    this.pet_sound = 'ARF!'
  }

  public mouse12() {
    this.pet = Pet.Mouse
    this.pet_sound = 'Squeak!'
  }

  public koala13() {
    this.pet = Pet.Koala
    this.pet_sound = 'Hi!'
  }

  public snail14() {
    this.pet = Pet.Snail
    this.pet_sound = 'Hi!'
  }

  public hippo15() {
    this.pet = Pet.Koala
    this.pet_sound = 'Hi!'
  }

  public frog16() {
    this.pet = Pet.Frog
    this.pet_sound = 'Ribbit!'
  }

  public onSubmit(name: string) {
    this.pet_name = name;
    this.router.navigate(['pet']);
  }

  
}

enum Pet {
  Temp,
  Bunny,
  Cat,
  Dog,
  Hamster,
  Chicken,
  Fox,
  Lion,
  Monkey,
  Elephant,
  Turtle,
  Seal,
  Mouse,
  Koala,
  Snail,
  Hippo,
  Frog
}
