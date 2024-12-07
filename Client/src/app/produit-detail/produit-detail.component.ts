import { Component, inject, input, OnInit, output } from '@angular/core';
import { Produit } from '../_models/Produit';
import { ProduitService } from '../_services/produit.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-produit-detail',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './produit-detail.component.html',
  styleUrl: './produit-detail.component.css'
})
export class ProduitDetailComponent implements OnInit {

produit=input.required<Produit>();
produitService=inject(ProduitService);
toDelete=output<string>();
fb=inject(FormBuilder);
produitForm : FormGroup=new FormGroup({});
ngOnInit(): void {
  this.produitForm=this.fb.group({
    nom_prod:[this.produit().nom_prod],
    prix_unit:[this.produit().prix_unit],
    quantite : [this.produit().quantite],
    description : [this.produit().description]
  });
  if(this.produit().code_prod.length>0)
  this.produitForm.disable();
}


switchModif(){
  this.produitForm.enable();
}
enregistrer(){
  
  const p :Produit ={...this.produitForm.value,code_prod:this.produit().code_prod};
  console.log(p);
  this.produitService.update(p)
  this.produitForm.disable();
}
ajouterProduit(){
  const p :Produit ={...this.produitForm.value,code_prod:this.produit().code_prod};
  this.produitService.ajouterProduit(p);
  this.produitForm.reset();
}
}
