import { TestBed, getTestBed } from '@angular/core/testing';

import { AuthService } from './auth.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CookieService } from 'ngx-cookie-service';
import { HttpClient } from '@angular/common/http';

describe('AuthService', () => {
  let injector: TestBed;
  let service: AuthService;
  let cookie: CookieService;
  let http: HttpClient;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ AuthService, CookieService ]
    });
    injector = getTestBed();
    service = injector.get(AuthService);
    cookie = injector.get(CookieService);
    http = injector.get(HttpClient);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should logout', () => {
    service.token = 'tkn';
    service.user = 'usr';
    cookie.set('token', 'tkn');

    service.logout();

    expect(service.token).toBeNull();
    expect(service.user).toBeNull();
    expect(cookie.get('token')).toEqual('');
  });

  it('should check if token is saved in cookies', () => {
    spyOn(cookie, 'get').and.returnValue('tkn');
    expect(service.shouldBeAuthenticated()).toEqual(true);
  });

  it('should check if token is not saved in cookies', () => {
    spyOn(cookie, 'get').and.returnValue('');
    expect(service.shouldBeAuthenticated()).toEqual(false);
  });

  it('should return true if user and token is given', () => {
    service.user = 'user';
    service.token = 'token';
    expect(service.isAuthenticated()).toBeTruthy();
  });

  it('should return false if user or token is not given', () => {
    service.user = 'user';
    service.token = '';
    expect(service.isAuthenticated()).toBeFalsy();
  });
});
