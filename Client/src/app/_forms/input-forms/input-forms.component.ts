import { Component, input, OnInit } from '@angular/core';
import {ReactiveFormsModule,ControlValueAccessor, FormControl} from '@angular/forms';

@Component({
  selector: 'app-input-forms',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './input-forms.component.html',
  styleUrl: './input-forms.component.css'
})
export class InputFormsComponent implements ControlValueAccessor  {
  label=input<string>("");
type=input<string>("text");
constructor(){

}
writeValue(obj: any): void {
  throw new Error('Method not implemented.');
}
registerOnChange(fn: any): void {
  throw new Error('Method not implemented.');
}
registerOnTouched(fn: any): void {
  throw new Error('Method not implemented.');
}
setDisabledState?(isDisabled: boolean): void {
  throw new Error('Method not implemented.');
}





}
