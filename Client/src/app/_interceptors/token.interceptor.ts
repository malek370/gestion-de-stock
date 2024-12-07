import { HttpInterceptorFn } from '@angular/common/http';

export const tokenInterceptor: HttpInterceptorFn = (req, next) => {
  let user;
  if(localStorage.getItem("user")){
user=JSON.parse(localStorage.getItem("user")!);
console.log(user);
  req = req.clone({
    setHeaders: {
      'x-access-token': user.token,
    },
  });}
  return next(req);
};
