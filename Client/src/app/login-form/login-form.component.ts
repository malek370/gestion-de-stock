import { Component, inject, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AccountServiceService } from '../_services/account-service.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { UserRegister } from '../_models/UserRegister';

@Component({
  selector: 'app-login-form',
  standalone: true,
  imports: [RouterLink,ReactiveFormsModule],
  templateUrl: './login-form.component.html',
  styleUrl: './login-form.component.css'
})
export class LoginFormComponent implements OnInit {

accountService=inject(AccountServiceService);
fb=inject(FormBuilder);
loginForm : FormGroup =new FormGroup({});
ngOnInit(): void {
  this.loginForm=this.fb.group({
    username : ["",[Validators.required]],
    password : ["",[Validators.required]]
  })
}
login(){
  const user :UserRegister={
    username:this.loginForm.value.username,
    password:this.loginForm.value.password
  }
  this.accountService.login(user);
}
}
