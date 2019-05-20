import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {SearchService} from '../search.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private service: SearchService,
    private router: Router
  ) {}

  query = '';
  results = [];
  loading = true;
  logo = '../assets/static/images/google.png';

  ngOnInit() {
    this.query = this.route.snapshot.paramMap.get('query');
    this.getResults();
  }
  onEnter() {
    if (this.query.trim().length >= 1) {
      this.router.navigateByUrl('/search/' + this.query);
      this.loading = true;
      this.results = [];
      this.getResults();
    }
  }
  getResults() {
    if (this.query.trim().length >= 1) {
      this.service.getResults(this.query).subscribe(response => {
        this.results = response.results;
        this.loading = false;
      });
    }
  }
}
