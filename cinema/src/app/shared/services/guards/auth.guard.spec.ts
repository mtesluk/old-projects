import { TestBed, async, inject } from '@angular/core/testing';

import { AuthGuard } from './auth.guard';
import { RouterTestingModule } from '@angular/router/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CookieService } from 'ngx-cookie-service';
import { AuthService } from '../auth/auth.service';

describe('AuthGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ AuthGuard, CookieService ],
      imports: [ RouterTestingModule, HttpClientTestingModule ]
    });
  });

  it('should init', inject([AuthGuard], (guard: AuthGuard) => {
    expect(guard).toBeTruthy();
  }));

  it('should activate page when login', inject([AuthGuard, AuthService], (guard: AuthGuard, auth: AuthService) => {
    spyOn(auth, 'isAuthenticated').and.returnValue(true);
    let activated_route_snapshot;
    let router_state_snapshot;

    expect(guard.canActivate(activated_route_snapshot, router_state_snapshot)).toEqual(true);
  }));

  it('should activate page when token took from cookie', inject([AuthGuard, AuthService], (guard: AuthGuard, auth: AuthService) => {
    spyOn(auth, 'isAuthenticated').and.returnValue(false);
    spyOn(auth, 'shouldBeAuthenticated').and.returnValue(true);

    let activated_route_snapshot;
    let router_state_snapshot;

    expect(guard.canActivate(activated_route_snapshot, router_state_snapshot)).toEqual(true);
  }));

  it('should not activate page', inject([AuthGuard, AuthService], (guard: AuthGuard, auth: AuthService) => {
    spyOn(auth, 'isAuthenticated').and.returnValue(false);
    spyOn(auth, 'shouldBeAuthenticated').and.returnValue(false);

    let activated_route_snapshot;
    let router_state_snapshot;

    expect(guard.canActivate(activated_route_snapshot, router_state_snapshot)).toEqual(false);
  }));
});
