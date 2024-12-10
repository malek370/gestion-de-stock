import { Routes } from '@angular/router';
import { RegisterFormComponent } from './register-form/register-form.component';
import { LoginFormComponent } from './login-form/login-form.component';
import { HomeComponent } from './home/home.component';
import { ProduitComponent } from './produit/produit.component';
import { CommandesComponent } from './commandes/commandes.component';

export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'register', component: RegisterFormComponent},
    {path: 'login', component: LoginFormComponent},
    {path: 'produit', component: ProduitComponent},
    {path: 'commandes', component: CommandesComponent},
];
