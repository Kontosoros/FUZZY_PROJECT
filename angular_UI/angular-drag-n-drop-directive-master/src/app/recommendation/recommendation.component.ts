import { Component, Input, EventEmitter, Output, OnInit } from "@angular/core";
import { json } from "./json";
import "survey-angular/defaultV2.css";
import * as Survey from "survey-angular";

import "survey-angular/defaultV2.css";
import { RecommendationsService } from "../recommendations.service";
import { Router } from "@angular/router";
import { openStdin } from "process";
Survey.StylesManager.applyTheme("defaultV2");
// @Component({
//   // tslint:disable-next-line:component-selector
//   selector: "survey",
//   template: `<div class="survey-container contentcontainer codecontainer">
//     <div id="surveyElement"></div>
//   </div>`,
// })

@Component({
  selector: "app-recommendation",
  templateUrl: "./recommendation.component.html",
  styleUrls: ["./recommendation.component.scss"],
})
export class RecommendationComponent implements OnInit {
  constructor(
    private recommendService: RecommendationsService,
    private router: Router
  ) {}
  result: string[] = [];
  results;
  @Output() submitSurvey = new EventEmitter<any>();
  @Input()
  alertResults(sender) {
    this.results = JSON.stringify(sender.data);
    alert(this.results);
  }
  ngOnInit() {
    const survey = new Survey.Model(json);
    var storageName = "survey_patient_history";

    function saveSurveyData(survey) {
      var data = survey.data;
      data.pageNo = survey.currentPageNo;
      window.localStorage.setItem(storageName, JSON.stringify(data));
    }

    function clearSurveyData(survey) {
      var data = survey.data;
      data.pageNo = 1;
      data = "";
      window.localStorage.setItem(storageName, JSON.stringify(data));
    }
    survey.onPartialSend.add(function (sender) {
      saveSurveyData(sender);
    });

    survey.onComplete.add(function (sender, options) {
      saveSurveyData(sender);
      const results = JSON.stringify(sender.data);
    });
    survey.sendResultOnPageNext = true;
    var prevData = window.localStorage.getItem(storageName) || null;
    if (prevData) {
      var data = JSON.parse(prevData);
      survey.data = data;
      if (data.pageNo) {
        survey.currentPageNo = data.pageNo;
      }
    }
    survey.focusFirstQuestionAutomatic = true;
    survey.onComplete.add(function (sender, options) {
      //Show message about "Saving..." the results
      options.showDataSaving(); //you may pass a text parameter to show your own text
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "http://127.0.0.1:5000/recommendations");
      xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
      xhr.onload = xhr.onerror = function () {
        if (xhr.status == 200) {
          options.showDataSavingSuccess();
          // you may pass a text parameter to show your own text
          // Or you may clear all messages:
          // options.showDataSavingClear();
          clearSurveyData(sender);
        } else {
          //Error
          options.showDataSavingError();
          // you may pass a text parameter to show your own text
        }
      };
      console.log(sender.data);
      xhr.send(JSON.stringify(sender.data));
      if (xhr.readyState == XMLHttpRequest.DONE) {
        this.result.push(xhr.responseText as string);
        // console.log(this.result);
      }
    });
    Survey.SurveyNG.render("surveyElement", { model: survey });
  }
}
