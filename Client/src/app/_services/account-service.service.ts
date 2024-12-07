import { inject, Injectable, signal } from '@angular/core';
import { User } from '../_models/User';
import { HttpClient } from '@angular/common/http';
import { UserRegister } from '../_models/UserRegister';
import { tap } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AccountServiceService {
  public currentUser = signal<User | null>(null);
  private http = inject(HttpClient);
  private url = "http://127.0.0.1:5000";
  private router=inject(Router);
  register(user: UserRegister) {
    return this.http.post<User>(this.url + "/register", user)
      .subscribe({
        next: res => this.setCurrentUser(res)
      })
  }
  logout() {
    this.setCurrentUser(null);
  }
  login(user:UserRegister){
    return this.http.post<User>(this.url + "/login", user)
      .subscribe({
        next: res => this.setCurrentUser(res)
      })
  }
  private setCurrentUser(u : User|null) {
    if(u){
      this.currentUser.set(u);
          localStorage.setItem("user", JSON.stringify(u));
          this.router.navigateByUrl('');
    }
    else{
      this.currentUser.set(null);
          localStorage.removeItem("user");
          this.router.navigateByUrl('/register');
    }
  }
}
