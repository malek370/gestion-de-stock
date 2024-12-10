import { Component, inject, OnInit, signal } from '@angular/core';
import { ProduitDetailComponent } from "../produit-detail/produit-detail.component";
import { Produit } from '../_models/Produit';
import { ProduitService } from '../_services/produit.service';
import { NgFor } from '@angular/common';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-produit',
  standalone: true,
  imports: [ProduitDetailComponent,NgFor],
  templateUrl: './produit.component.html',
  styleUrl: './produit.component.css'
})
export class ProduitComponent implements OnInit {
  produitService=inject(ProduitService);
  fb = inject(FormBuilder);
  creerProduitForm :FormGroup=new FormGroup({});
  produitACreer:Produit={
    code_prod: "",
    nom_prod: "",
    description: "",
    quantite: 0,
    prix_unit: 0
  }
  ngOnInit(): void {
    this.produitService.getAll();
  }
  supprimer(event:string){
    if(event.length>0)
    this.produitService.supprimer(event);
    //this.ngOnInit()
  }
  trackById(index: number, produit: Produit): string {
    return produit.code_prod;
  }

}
