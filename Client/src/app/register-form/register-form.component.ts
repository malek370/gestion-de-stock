import { Component, inject, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, ReactiveFormsModule, ValidationErrors, ValidatorFn, Validators } from '@angular/forms';

@Component({
  selector: 'app-register-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './register-form.component.html',
  styleUrl: './register-form.component.css'
})
export class RegisterFormComponent implements OnInit {
  fn = inject(FormBuilder);
  registerForm: FormGroup = new FormGroup({});
  ngOnInit(): void {
    this.initializeForm();
  }

  initializeForm() {
    this.registerForm = this.fn.group({
      username: ["", Validators.required],
      password: ["", [Validators.required, Validators.minLength(8)]],
      confirmPassword: ["", [Validators.required, Validators.minLength(8),this.matchPassword]]
    });
    this.registerForm.get("password")?.valueChanges.subscribe({
      next:_=>this.registerForm.get("password")?.updateValueAndValidity
    })
  }
  matchPassword(): ValidatorFn {
    return (control: AbstractControl): ValidationErrors | null => {
      console.log("parent:"+control.parent?.get("password")?.value);
      console.log("controle:"+control.value);
      console.log("test:"+control.value===control.parent?.get("password")?.value);
      return control.value===control.parent?.get("password")?.value?null:{NoMatch:true};
    }
  }
  register(){
    console.log(this.registerForm.value);
    console.log(this.registerForm.status);
  }
}
