import { Component, inject, OnInit } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';
import { RegisterFormComponent } from './register-form/register-form.component';
import { AccountServiceService } from './_services/account-service.service';
import { NavComponent } from './nav/nav.component';
import { LoginFormComponent } from "./login-form/login-form.component";
import { User } from './_models/User';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NavComponent, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {

  account = inject(AccountServiceService);
  title = 'Client';
  ngOnInit(): void {
    let current_user = localStorage.getItem("user");
    if (current_user) {
      let currentUser: User
      currentUser = {
        username: JSON.parse(current_user).username,
        token: JSON.parse(current_user).token,
      };
      this.account.currentUser.set(currentUser);
    }
  }
}
