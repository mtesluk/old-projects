import { Component, OnInit, Input } from '@angular/core';
import { Observable } from 'rxjs';

import { ApiHandlerService } from 'src/app/shared/services/api-handler/api-handler.service';
import { Config } from 'src/app/config';
import { ImgMovie } from 'src/app/shared/interface/movie.interface';

@Component({
  selector: 'app-films-slide',
  templateUrl: './films-slide.component.html',
  styleUrls: ['./films-slide.component.scss']
})
export class FilmsSlideComponent implements OnInit {
  @Input() category: string;
  conf = Config;
  current_movies: Observable<ImgMovie[]>;
  imageSource: ImgMovie[];

  constructor(private api_handler: ApiHandlerService) { }

  ngOnInit() {
    switch (this.category) {
      case 'soon': {
        this.current_movies = this.api_handler.fetchList(this.conf.urls.get_soon_movies);
      }break;
      case 'recommended': {
        this.current_movies = this.api_handler.fetchList(this.conf.urls.get_recommended_movies);
      }break;
      case 'kids': {
        this.current_movies = this.api_handler.fetchList(this.conf.urls.get_kids_movies);
      }break;
    }

    if (this.current_movies) {
      this.current_movies.subscribe(movies => this.imageSource = movies);
    }
  }

}
