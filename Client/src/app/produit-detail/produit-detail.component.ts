import { Component, inject, input, OnInit, output } from '@angular/core';
import { Produit } from '../_models/Produit';
import { ProduitService } from '../_services/produit.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { ProduitCommandeComponent } from '../produit-commande/produit-commande.component';
import { CommandesService } from '../_services/commandes.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-produit-detail',
  standalone: true,
  imports: [ReactiveFormsModule, MatButtonModule, MatDialogModule],
  templateUrl: './produit-detail.component.html',
  styleUrl: './produit-detail.component.css'
})
export class ProduitDetailComponent implements OnInit {


  produit = input.required<Produit>();
  produitService = inject(ProduitService);
  commandeService=inject(CommandesService);
  router=inject(Router);
  toDelete = output<string>();
  fb = inject(FormBuilder);
  produitForm: FormGroup = new FormGroup({});
  readonly dialog = inject(MatDialog);
  ngOnInit(): void {
    this.produitForm = this.fb.group({
      nom_prod: [this.produit().nom_prod,[Validators.required,Validators.minLength(1)]],
      prix_unit: [this.produit().prix_unit,[Validators.required,Validators.min(50)]],
      quantite: [this.produit().quantite,[Validators.required,Validators.min(1)]],
      description: [this.produit().description,[Validators.required,Validators.minLength(1)]]
    });
    if (this.produit().code_prod.length > 0)
      this.produitForm.disable();
  }
  openDialog() {
    const buttonElement = document.activeElement as HTMLElement; // Get the currently focused element
    buttonElement.blur(); // Remove focus from the button
    const dialogRef = this.dialog.open(ProduitCommandeComponent,{
      data:this.produit().quantite
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
      if(result){
        this.commandeService.ajouterProduitCommande(result.code_cmd,result.nb_prod,this.produit().code_prod);
        this.produitService.produits.update(prods => {
          const newProds = prods.map(p => {
            if (p.code_prod === this.produit().code_prod) {
              return { ...p, quantite: p.quantite - result.nb_prod }; // Create a new object
            }
            return p; // Return the original object if not modified
          });
          return newProds; // Return a new array
        });
        this.produit().quantite=this.produit().quantite-result.nb_prod;
        this.ngOnInit();
      }
    });
  }


  switchModif() {
    this.produitForm.enable();
  }
  enregistrer() {

    const p: Produit = { ...this.produitForm.value, code_prod: this.produit().code_prod };
    console.log(p);
    this.produitService.update(p)
    this.produitForm.disable();
  }
  ajouterProduit() {
    const p: Produit = { ...this.produitForm.value, code_prod: this.produit().code_prod };
    this.produitService.ajouterProduit(p);
    this.produitForm.reset();
  }
  
}
