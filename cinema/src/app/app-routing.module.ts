import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProgrammeComponent } from './components/programme/programme.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { TariffComponent } from './components/tariff/tariff.component';
import { SpecialComponent } from './components/special/special.component';
import { ContactComponent } from './components/contact/contact.component';
import { WildcardComponent } from './navigation/wildcard/wildcard.component';
import { AuthGuard } from './shared/services/guards/auth.guard';
import { ReservationComponent } from './components/reservation/reservation.component';

const routes: Routes = [
  { path: '', component: DashboardComponent },
  { path: 'programme', component: ProgrammeComponent },
  { path: 'programme/:caption', component: ReservationComponent, canActivate: [AuthGuard] },
  { path: 'tariff', component: TariffComponent },
  { path: 'special', component: SpecialComponent },
  { path: 'contact', component: ContactComponent },
  { path: '**', component: WildcardComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ],
  providers: [ AuthGuard ]
})
export class AppRoutingModule { }
