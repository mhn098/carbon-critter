import { TestBed } from '@angular/core/testing';

import { CCService } from './cc.service';

describe('FunctionService', () => {
  let service: CCService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CCService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
