import { TestBed, getTestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

import { ApiHandlerService } from './api-handler.service';

describe('ApiHandlerService', () => {
  let injector: TestBed;
  let service: ApiHandlerService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ HttpClientTestingModule ],
      providers: [ ApiHandlerService ]
    });
    injector = getTestBed();
    service = injector.get(ApiHandlerService);
    httpMock = injector.get(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should return expected list', () => {
    const dummyList = [
      { caption: 'Mateusz' },
      { caption: 'Jakub' }
    ];

    service.fetchList('some_url').subscribe(movies => {
      expect(movies.length).toBe(2);
      expect(movies).toEqual(dummyList);
    });

    const req = httpMock.expectOne('some_url');
    expect(req.request.method).toBe('GET');
    req.flush(dummyList);
  });

  it('should return expected list', () => {
    const dummyData = { caption: 'Mateusz' };

    service.fetchData('some_url').subscribe(movie => {
      expect(movie).toEqual(dummyData);
    });

    const req = httpMock.expectOne('some_url');
    expect(req.request.method).toBe('GET');
    req.flush(dummyData);
  });

  it('should post some data', () => {
    const dummyData = { caption: 'Mateusz' };

    service.postData('some_url', dummyData).subscribe(movie => {
      expect(movie).toEqual(dummyData);
    });

    const req = httpMock.expectOne('some_url');
    expect(req.request.method).toBe('POST');
    req.flush(dummyData);
  });
});
