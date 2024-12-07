import { Component, inject, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, ReactiveFormsModule, ValidationErrors, ValidatorFn, Validators } from '@angular/forms';
import { User } from '../_models/User';
import { UserRegister } from '../_models/UserRegister';
import { AccountServiceService } from '../_services/account-service.service';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-register-form',
  standalone: true,
  imports: [ReactiveFormsModule,RouterLink],
  templateUrl: './register-form.component.html',
  styleUrl: './register-form.component.css'
})
export class RegisterFormComponent implements OnInit {
  fb = inject(FormBuilder);
  accountService=inject(AccountServiceService);
  registerForm: FormGroup = new FormGroup({});
  ngOnInit(): void {
    this.initializeForm();
  }

  initializeForm() {
    this.registerForm = this.fb.group({
      username: ['', Validators.required],
      password: ['12345678', [Validators.required, Validators.minLength(8)]],
      confirmPassword: ['12345678', Validators.required],
    }, { validators: this.passwordsMatchValidator });
  }
  passwordsMatchValidator: Validators = (group: FormGroup): ValidationErrors | null => {
    const password = group.get('password')?.value;
    const confirmPassword = group.get('confirmPassword')?.value;

    return password === confirmPassword ? null : { passwordsMismatch: true };
  };
  register(){
    console.log(this.registerForm.value);
    const user :UserRegister={
      username:this.registerForm.value.username,
      password:this.registerForm.value.password
    }
    console.log(this.registerForm.status);
    this.accountService.register(user);
  }
}
