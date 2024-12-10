import { HttpClient } from '@angular/common/http';
import { inject, Injectable, signal } from '@angular/core';
import { Produit } from '../_models/Produit';
import { tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProduitService {
  http=inject(HttpClient);
  produits=signal<Produit[]>([]);
  url="http://127.0.0.1:5000"+"/produit";
  
  getAll(){
    console.log('get all produit');
    this.http.get<Produit[]>(this.url).subscribe({
      next:res=>this.produits.set(res)
    });
    console.log("got all produits x");
    console.log(this.produits());
  }
  getOne(code:string){
    return this.http.get<Produit>(this.url+"/"+code);
  }
  update(produit:Produit){
    this.http.put(this.url+"/"+produit.code_prod,produit).subscribe({
      next:_=>{
        this.produits.update(ps=>{
          ps.map(p=>{
            if(p.code_prod===produit.code_prod)p=produit;
            
          });
          return ps
        })
      }
    })
  }
  supprimer(code:string){
    this.http.delete(this.url+"/"+code).subscribe({
      next : _=>{
        this.produits.update(ps=>{
          ps=ps.filter(p=>p.code_prod!==code);
          return ps
          
        })
      }
    })
  }
  ajouterProduit(produit:Produit){
    this.http.post<any>(this.url,produit)
      .subscribe({
        next:res=>{
          produit.code_prod=res.message;
          this.produits.update(ps=>{
            let res=[...ps];
            res.push(produit);
            return res;
          })
        }
      })
  }
}
