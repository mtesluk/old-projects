import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TariffComponent } from './tariff.component';
import { HttpClientModule } from '@angular/common/http';

describe('TariffComponent', () => {
  let component: TariffComponent;
  let fixture: ComponentFixture<TariffComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TariffComponent ],
      imports: [ HttpClientModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TariffComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
