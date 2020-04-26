import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProgrammeComponent } from './programme.component';
import { MyMaterialsModule } from 'src/app/my-materials.module';
import { DateFieldComponent } from './date-field/date-field.component';
import { MovieComponent } from './movie/movie.component';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

describe('ProgrammeComponent', () => {
  let component: ProgrammeComponent;
  let fixture: ComponentFixture<ProgrammeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProgrammeComponent, DateFieldComponent, MovieComponent ],
      imports: [ MyMaterialsModule, HttpClientModule, BrowserAnimationsModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProgrammeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
