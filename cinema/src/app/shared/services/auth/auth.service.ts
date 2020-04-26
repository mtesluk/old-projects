import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

import { CookieService } from 'ngx-cookie-service';
import { Config } from 'src/app/config';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  user: string;
  token: string;
  conf = Config;

  constructor(private http: HttpClient, private cookie: CookieService) { }

  fetchToken(username: string, password: string) {
    this.user = username;
    // should be this.http.post with sending username and password, but there is no backend
    return this.http.get(this.conf.urls.get_token).pipe(
      map((response: {token: string}) => {
        this.token = response.token;
        this.cookie.delete('token');
        this.cookie.set('token', response.token);
        return response;
      }
      )
    );
  }

  logout() {
    this.token = null;
    this.user = null;
    this.cookie.delete('token');
    // notifier logout
  }

  login(username: string, password: string) {
    this.fetchToken(username, password).subscribe();
    return this.token ? true : false;
    // notifier login
  }

  isAuthenticated() {
    return !!this.user && !!this.token;
  }

  shouldBeAuthenticated() {
    this.token = this.cookie.get('token');
    return this.token ? true : false;
  }
}
