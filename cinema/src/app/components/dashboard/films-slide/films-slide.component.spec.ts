import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FilmsSlideComponent } from './films-slide.component';
import { SlideshowModule } from 'ng-simple-slideshow';
import { HttpClientModule } from '@angular/common/http';

describe('FilmsSlideComponent', () => {
  let component: FilmsSlideComponent;
  let fixture: ComponentFixture<FilmsSlideComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FilmsSlideComponent ],
      imports: [ SlideshowModule, HttpClientModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FilmsSlideComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
