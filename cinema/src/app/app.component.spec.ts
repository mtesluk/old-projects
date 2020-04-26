import { TestBed, async } from '@angular/core/testing';
import { AppComponent } from './app.component';

import { NavbarComponent } from './navigation/navbar/navbar.component';
import { FooterComponent } from './navigation/footer/footer.component';
import { AppRoutingModule } from './app-routing.module';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { ProgrammeComponent } from './components/programme/programme.component';
import { TariffComponent } from './components/tariff/tariff.component';
import { SpecialComponent } from './components/special/special.component';
import { ContactComponent } from './components/contact/contact.component';
import { MyMaterialsModule } from './my-materials.module';
import { FilmsSlideComponent } from './components/dashboard/films-slide/films-slide.component';
import { DateFieldComponent } from './components/programme/date-field/date-field.component';
import { MovieComponent } from './components/programme/movie/movie.component';
import { SlideshowModule } from 'ng-simple-slideshow';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { ReservationComponent } from './components/reservation/reservation.component';
import { WildcardComponent } from './navigation/wildcard/wildcard.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CookieService } from 'ngx-cookie-service';

describe('AppComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        AppComponent, NavbarComponent, FooterComponent, DashboardComponent, ProgrammeComponent,
        TariffComponent, SpecialComponent, ContactComponent, FilmsSlideComponent, DateFieldComponent,
        MovieComponent, ReservationComponent, WildcardComponent, 
      ],
      imports: [
        AppRoutingModule, MyMaterialsModule, SlideshowModule, ReactiveFormsModule, FormsModule,
        HttpClientTestingModule
      ],
      providers: [ CookieService ]
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app).toBeTruthy();
  });
});
