import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { MyMaterialsModule } from './my-materials.module';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navigation/navbar/navbar.component';
import { FooterComponent } from './navigation/footer/footer.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { TariffComponent } from './components/tariff/tariff.component';
import { ProgrammeComponent } from './components/programme/programme.component';
import { SpecialComponent } from './components/special/special.component';
import { AppRoutingModule } from './app-routing.module';
import { DateFieldComponent } from './components/programme/date-field/date-field.component';
import { MovieComponent } from './components/programme/movie/movie.component';
import { ContactComponent } from './components/contact/contact.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FilmsSlideComponent } from './components/dashboard/films-slide/films-slide.component';
import { SlideshowModule } from 'ng-simple-slideshow';
import { WildcardComponent } from './navigation/wildcard/wildcard.component';
import { ReservationComponent } from './components/reservation/reservation.component';
import { CookieService } from 'ngx-cookie-service';


@NgModule({
  declarations: [
    ReservationComponent,
    FilmsSlideComponent,
    AppComponent,
    NavbarComponent,
    FooterComponent,
    DashboardComponent,
    TariffComponent,
    ProgrammeComponent,
    SpecialComponent,
    DateFieldComponent,
    MovieComponent,
    ContactComponent,
    WildcardComponent
  ],
  imports: [
    SlideshowModule,
    MyMaterialsModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserModule,
    AppRoutingModule
  ],
  providers: [ CookieService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
