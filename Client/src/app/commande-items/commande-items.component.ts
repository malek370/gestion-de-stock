import { Component, inject, Inject, input, OnInit, signal } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MAT_DIALOG_DATA, MatDialogModule } from '@angular/material/dialog';
import { Command } from '../_models/Commandes';
import { NgFor } from '@angular/common';
import { ProduitService } from '../_services/produit.service';

@Component({
  selector: 'app-commande-items',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule,NgFor],
  templateUrl: './commande-items.component.html',
  styleUrl: './commande-items.component.css'
})
export class CommandeItemsComponent implements OnInit{
  commande =signal<Command>( inject(MAT_DIALOG_DATA));
  proditService=inject(ProduitService);
  data=[];
  
  ngOnInit(): void {
    console.log(this.commande());
    this.commande.update(cmd=>{
      cmd.prixCommande=0;
      cmd.nombreItems=0;
      cmd.items.map(el=>{
        this.proditService.getOne(el.code_prod).subscribe({
          next:resp=>{
            el.prixTot=el.nb_produit*resp.prix_unit;
            cmd.prixCommande=cmd.prixCommande+el.prixTot;
            cmd.nombreItems=cmd.nombreItems+el.nb_produit;
          }
        });
      });
      return cmd;
    })
    console.log(this.commande());
  }
  
}
