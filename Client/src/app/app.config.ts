import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { errorHandlerInterceptor } from './_interceptors/error-handler.interceptor';
import { tokenInterceptor } from './_interceptors/token.interceptor';
import { provideAnimations } from '@angular/platform-browser/animations';

import { provideToastr } from 'ngx-toastr';
export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideHttpClient(withInterceptors([errorHandlerInterceptor,tokenInterceptor])),
    provideAnimations(), // required animations providers
    provideToastr({
      timeOut: 2000,
      positionClass: 'toast-bottom-right',
    }),
  ]
  
};
