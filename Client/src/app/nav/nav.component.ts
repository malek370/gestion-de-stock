import { Component, inject } from '@angular/core';
import { AccountServiceService } from '../_services/account-service.service';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-nav',
  standalone: true,
  imports: [RouterLinkActive,RouterLink],
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent {
   account=inject(AccountServiceService);
  logout(){
    this.account.logout();
  }
}
