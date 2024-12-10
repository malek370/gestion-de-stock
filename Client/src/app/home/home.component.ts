import { Component, inject, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AccountServiceService } from '../_services/account-service.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  router=inject(Router);
  account = inject(AccountServiceService);
  ngOnInit(): void {
    if(!this.account.currentUser())
    this.router.navigateByUrl('/register');
  }

}
