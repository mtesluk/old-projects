import { Component, OnInit, Input } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { Movie } from 'src/app/shared/interface/movie.interface';

@Component({
  selector: 'app-movie',
  templateUrl: './movie.component.html',
  styleUrls: ['./movie.component.scss']
})
export class MovieComponent implements OnInit {
  @Input() movie: Movie;
  @Input() date: string;

  constructor(private router: Router, private route: ActivatedRoute) { }

  ngOnInit() {
    // if (this.movie) {

    // }
  }

  navigate_to_detail(time: string) {
    const prepared_movie_caption = this.movie.en_movie_name.replace(/\s/g, '_').toLowerCase();
    console.log(prepared_movie_caption);
    console.log(time);
    console.log(this.date);
    this.router.navigate(['programme', prepared_movie_caption]);
  }

}
