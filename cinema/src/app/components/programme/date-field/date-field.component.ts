import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-date-field',
  templateUrl: './date-field.component.html',
  styleUrls: ['./date-field.component.css']
})
export class DateFieldComponent implements OnInit {
  @Input() date: Date;

  str_date: string;
  week_day: string;

  constructor() { }

  ngOnInit() {
    if (this.date) {
      const tmp = this.date.toDateString().split(' ');
      this.week_day = tmp[0];
      this.str_date = tmp[2] + ' ' + tmp[1];
    }
  }
}
