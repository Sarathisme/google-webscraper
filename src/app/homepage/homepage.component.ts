import {Component, Inject, OnInit} from '@angular/core';
import {Router} from '@angular/router';
import {SearchService} from '../search.service';
import {DOCUMENT} from '@angular/common';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

  constructor(private route: Router, private service: SearchService, @Inject(DOCUMENT) private document: any) { }

  query = '';
  logo = '../assets/static/images/google.png';

  onEnter() {
    if (this.query.trim().length >= 1) {
      this.route.navigateByUrl('/search/' + this.query);
    }
  }
  feelingLucky() {
    if (this.query.trim().length >= 1) {
      this.service.getResults(this.query).subscribe(response => this.document.location.href = response.results[0].link);
    }
  }
  ngOnInit() {
  }
}
