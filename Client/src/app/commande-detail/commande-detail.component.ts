import { Component, inject, input, output } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommandesService } from '../_services/commandes.service';
import { Command } from '../_models/Commandes';
import { MatDialog } from '@angular/material/dialog';
import { CommandeItemsComponent } from '../commande-items/commande-items.component';

@Component({
  selector: 'app-commande-detail',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './commande-detail.component.html',
  styleUrl: './commande-detail.component.css'
})
export class CommandeDetailComponent {

  commande = input.required<Command>();
  commandeService = inject(CommandesService);
  toDelete = output<string>();
  fb = inject(FormBuilder);
  commandeForm: FormGroup = new FormGroup({});
  readonly dialog = inject(MatDialog);
  ngOnInit(): void {
    this.commandeForm = this.fb.group({
      titre: [this.commande().titre, [Validators.required]],
      description: [this.commande().description, [Validators.required]]
    });
    if (this.commande().code_cmd.length > 0)
      this.commandeForm.disable();
  }

  details() {
    const buttonElement = document.activeElement as HTMLElement; // Get the currently focused element
    buttonElement.blur(); // Remove focus from the button
    const dialogRef = this.dialog.open(CommandeItemsComponent,{width: '40%',
      data:this.commande()
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
    });
  }



  ajoutercommande() {
    const p: Command = { ...this.commandeForm.value, code_prod: this.commande().code_cmd };
    this.commandeService.ajouterCommande(p);
    this.commandeForm.reset();
  }
}
