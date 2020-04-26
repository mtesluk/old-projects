import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { MovieComponent } from './movie.component';
import { Router } from '@angular/router';
import { AppRoutingModule } from 'src/app/app-routing.module';
import { DashboardComponent } from '../../dashboard/dashboard.component';
import { ProgrammeComponent } from '../programme.component';
import { ReservationComponent } from '../../reservation/reservation.component';

describe('MovieComponent', () => {
  let component: MovieComponent;
  let fixture: ComponentFixture<MovieComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MovieComponent ],
      imports: [ RouterTestingModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MovieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
