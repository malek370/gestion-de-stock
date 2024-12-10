import { Component, inject } from '@angular/core';
import { CommandeDetailComponent } from '../commande-detail/commande-detail.component';
import { NgFor } from '@angular/common';
import { CommandesService } from '../_services/commandes.service';
import { Command } from '../_models/Commandes';

@Component({
  selector: 'app-commandes',
  standalone: true,
  imports: [CommandeDetailComponent,NgFor],
  templateUrl: './commandes.component.html',
  styleUrl: './commandes.component.css'
})
export class CommandesComponent {
  commandeService=inject(CommandesService);
  commandeACreer:Command={
    code_cmd: "",
    titre: "",
    description: "",
    items: []
    }
  ngOnInit(): void {
    this.commandeService.getAll();
    
  }
  supprimer(event:string){
    if(event.length>0)
    this.commandeService.supprimer(event);
    //this.ngOnInit()
  }
  trackById(index: number, commande: Command): string {
    return commande.code_cmd;
  }
}
