import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Observable } from 'rxjs';

import { Config } from 'src/app/config';
import { ApiHandlerService } from 'src/app/shared/services/api-handler/api-handler.service';
import { City } from 'src/app/shared/interface/city.interface';
import { Contact } from 'src/app/shared/interface/contact.interface';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent implements OnInit {
  cities: Observable<City[]>;
  contact: Observable<Contact>;
  contactForm: FormGroup;
  current_city: string;
  conf = Config;

  constructor(private api_handler: ApiHandlerService,
              private _fb: FormBuilder) { }

  ngOnInit() {
    this.cities = this.api_handler.fetchList(this.conf.urls.get_all_sites);
    this.contactForm = this._fb.group({
      email: '',
      topic: '',
      text: ''
    });

    if (localStorage['current_city']) {
      this.current_city = localStorage['current_city'];
      const url = this.conf.urls.get_contact;
      const endpoint = url.first_part + this.current_city.toLowerCase() + url.second_part;
      this.contact = this.api_handler.fetchData(endpoint);
    }
  }

  setCurrentCity(event) {
    this.current_city = event.value;
    localStorage['current_city'] = this.current_city;
    const url = this.conf.urls.get_contact;
    const endpoint = url.first_part + this.current_city.toLowerCase() + url.second_part;
    this.contact = this.api_handler.fetchData(endpoint);
  }

  sendClientRequest() {
    this.api_handler.postData(this.conf.urls.post_client_request, this.contactForm.value).subscribe();
    this.contactForm.reset();
  }

}
