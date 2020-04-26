import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

import { Config } from 'src/app/config';
import { ApiHandlerService } from 'src/app/shared/services/api-handler/api-handler.service';
import { environment } from 'src/environments/environment';
import { City } from 'src/app/shared/interface/city.interface';
import { Movie } from 'src/app/shared/interface/movie.interface';

@Component({
  selector: 'app-programme',
  templateUrl: './programme.component.html',
  styleUrls: ['./programme.component.css']
})
export class ProgrammeComponent implements OnInit {
  cities: Observable<City[]>;
  current_movies: Observable<Movie[]>;
  current_city: string;
  current_day: string;
  days: Date[];
  city_chosen: Boolean = false;
  date_chosen: Boolean = false;
  conf = Config;

  constructor(private api_handler: ApiHandlerService) { }

  ngOnInit() {
    this.days = [];
    const day = new Date();

    for (let i = 0; i < environment.available_reservation_days; i++) {
      this.days.push(new Date(day));
      day.setDate(day.getDate() + 1);
    }

    this.cities = this.api_handler.fetchList(this.conf.urls.get_all_sites);

    if (localStorage['current_city']) {
      this.current_city = localStorage['current_city'];
      this.city_chosen = true;
    }
  }

  setCurrentCity(event) {
    this.current_city = event.value;
    localStorage['current_city'] = this.current_city;
    this.city_chosen = true;
    this.current_movies = this.ready_to_show() ? this.getMovies() : null;
    }

  getMovies() {
    const url = this.conf.urls.get_movies_for_city;
    const endpoint = url.first_part + this.current_city.toLowerCase() + url.second_part;
    return this.api_handler.fetchList(endpoint);
  }

  choose_date(day: string) {
    this.current_day = day;
    this.date_chosen = true;
    this.current_movies = this.ready_to_show() ? this.getMovies() : null;
  }

  ready_to_show() {
    return this.date_chosen && this.city_chosen ? true : false;
  }
}
