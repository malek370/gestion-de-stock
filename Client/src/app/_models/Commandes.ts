export interface Command {
    code_cmd: string;
    titre: string;
    description: string;
    items: any[];
    prixCommande?:number;
    nombreItems?:number;
}