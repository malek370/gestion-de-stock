import { Component, inject, OnInit, signal } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialog, MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';
import { CommandesService } from '../_services/commandes.service';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-produit-commande',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, ReactiveFormsModule, FontAwesomeModule,NgFor],
  templateUrl: './produit-commande.component.html',
  styleUrl: './produit-commande.component.css'
})
export class ProduitCommandeComponent implements OnInit {

  faPlus = faPlus;
  faMinus = faMinus;
  commandeService=inject(CommandesService);
  maxQtt =signal<number>( inject(MAT_DIALOG_DATA));
  produitCommandeForm: FormGroup = new FormGroup({});
  fb=inject(FormBuilder);
  ngOnInit(): void {
      this.produitCommandeForm=this.fb.group({
        nb_prod:["1",[Validators.min(1),Validators.max(this.maxQtt())]],
        code_cmd:[,[Validators.required]]
      })
      this.commandeService.getAll();
  }
  plusOne() {
    if(!(this.produitCommandeForm.value.nb_prod>=this.maxQtt()))
      this.produitCommandeForm.get("nb_prod")?.setValue(Number(this.produitCommandeForm.value.nb_prod)+1); 
    }
    minusOne() {
      if(this.produitCommandeForm.value.nb_prod>1)
        this.produitCommandeForm.get("nb_prod")?.setValue(Number(this.produitCommandeForm.value.nb_prod)-1);
    }
}
