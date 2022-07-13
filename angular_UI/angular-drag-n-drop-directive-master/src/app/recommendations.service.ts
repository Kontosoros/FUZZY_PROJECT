import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable({
  providedIn: "root",
})
export class RecommendationsService {
  constructor(private http: HttpClient) {}

  recommendationService(item: any) {
    console.log("i am here");

    const formData = new FormData();
    formData.append("form", item);
    console.log(item);
    return this.http.post("http://127.0.0.1:5000/recommendations", formData);
  }
}
