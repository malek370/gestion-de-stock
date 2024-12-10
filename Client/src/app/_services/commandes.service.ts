import { HttpClient } from '@angular/common/http';
import { inject, Injectable, signal } from '@angular/core';
import { Command } from '../_models/Commandes';

@Injectable({
  providedIn: 'root'
})
export class CommandesService {

  http=inject(HttpClient);
  commandes=signal<Command[]>([]);
url="http://127.0.0.1:5000"+"/commande";
  getAll(){
    this.http.get<Command[]>(this.url).subscribe({
      next:res=>this.commandes.set(res)
    })
  }

  supprimer(code:string){
    this.http.delete(this.url+"/"+code).subscribe({
      next : _=>{
        this.commandes.update(ps=>{
          ps=ps.filter(p=>p.code_cmd!==code);
          return ps
          
        })
      }
    })
  }
  ajouterCommande(commande:Command){
    this.http.post<any>(this.url,commande)
      .subscribe({
        next:res=>{
          commande.code_cmd=res.message;
          this.commandes.update(ps=>{
            let res=[...ps];
            res.push(commande);
            return res;
          })
        }
      })
  }
  ajouterProduitCommande(code_cmd:string,nb_produit:number,code_prod:string){
    this.http.put(this.url+"/"+code_cmd,{code_prod:code_prod,nb_produit:nb_produit})
      .subscribe({
        next: res=>{
          console.log(res);
        }
      })
  }
}
