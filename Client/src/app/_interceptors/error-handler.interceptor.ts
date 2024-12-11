import { HttpErrorResponse, HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { Toast, ToastrService } from 'ngx-toastr';
import { catchError, tap, throwError } from 'rxjs';
export const errorHandlerInterceptor: HttpInterceptorFn = (req, next) => {
   let toast=inject(ToastrService);
  return next(req).pipe(catchError((error: HttpErrorResponse) => {
   console.log(error);
    let errorMsg = '';
    if (error.error instanceof ErrorEvent) {
       console.log('This is client side error');
       errorMsg = `Error: ${error.error.message}`;
    } else {
      if(error.error.message)toast.error(String(error.status),error.error.message);
      else toast.error("erreur!! verifier la console.");
    }
    console.log(errorMsg);
    return throwError(()=>new Error(errorMsg));
 }));
};
