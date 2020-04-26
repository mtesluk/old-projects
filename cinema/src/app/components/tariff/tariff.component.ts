import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

import { Config } from 'src/app/config';
import { ApiHandlerService } from 'src/app/shared/services/api-handler/api-handler.service';
import { MoviePrice } from 'src/app/shared/interface/price.interface';
import { SnackPrice } from 'src/app/shared/interface/price.interface';
import { KitPrice } from 'src/app/shared/interface/price.interface';

@Component({
  selector: 'app-tariff',
  templateUrl: './tariff.component.html',
  styleUrls: ['./tariff.component.css']
})
export class TariffComponent implements OnInit {
  movie_prices: Observable<MoviePrice>;
  snack_prices: Observable<SnackPrice>;
  kit_prices: Observable<KitPrice>;
  conf = Config;

  constructor(private api_handler: ApiHandlerService) { }

  ngOnInit() {
    this.movie_prices = this.api_handler.fetchData(this.conf.urls.get_movie_price);
    this.snack_prices = this.api_handler.fetchData(this.conf.urls.get_snacks_price);
    this.kit_prices = this.api_handler.fetchData(this.conf.urls.get_kit_price);
  }
}
