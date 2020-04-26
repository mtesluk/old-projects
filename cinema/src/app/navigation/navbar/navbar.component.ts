import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthService } from 'src/app/shared/services/auth/auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  isLogged: Boolean = false;

  constructor(private auth: AuthService, private router: Router) { }

  ngOnInit() {
    this.isLogged = this.auth.shouldBeAuthenticated();
  }

  logOut() {
    this.auth.logout();
    this.isLogged = false;
    this.router.navigate(['']);
  }

  logIn(form: NgForm) {
    this.isLogged = this.auth.login(form.value.username, form.value.password);
  }
}
