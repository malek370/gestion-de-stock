import { HttpErrorResponse, HttpInterceptorFn } from '@angular/common/http';
import { catchError, tap, throwError } from 'rxjs';

export const errorHandlerInterceptor: HttpInterceptorFn = (req, next) => {
  return next(req).pipe(catchError((error: HttpErrorResponse) => {
   //  console.log("err intzer : ");
   //  console.log(error);
    let errorMsg = '';
    if (error.error instanceof ErrorEvent) {
       console.log('This is client side error');
       errorMsg = `Error: ${error.error.message}`;
    } else {
       console.log('This is server side error');
       errorMsg = `Error Code: ${error.status},  Message: ${error.message}`;
    }
    console.log(errorMsg);
    return throwError(()=>new Error(errorMsg));
 }));
};
