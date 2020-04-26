import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

import { Config } from 'src/app/config';
import { Discount } from 'src/app/shared/interface/discount.interface';
import { ApiHandlerService } from 'src/app/shared/services/api-handler/api-handler.service';

@Component({
  selector: 'app-special',
  templateUrl: './special.component.html',
  styleUrls: ['./special.component.css']
})
export class SpecialComponent implements OnInit {
  discounts: Observable<Discount[]>;
  conf = Config;

  constructor(private api_handler: ApiHandlerService) { }

  ngOnInit() {
    this.discounts = this.api_handler.fetchData(this.conf.urls.get_discounts);
  }
}
