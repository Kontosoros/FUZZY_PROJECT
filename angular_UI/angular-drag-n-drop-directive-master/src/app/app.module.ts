import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { HttpClientModule } from "@angular/common/http";
import { AppComponent } from "./app.component";
import { DndDirective } from "./direcitves/dnd.directive";
import { ProgressComponent } from "./components/progress/progress.component";
import { NgSpinnerModule } from "ng-bootstrap-spinner";
import { AppRoutingModule, routingComponents } from "./app-routing.module";

@NgModule({
  declarations: [
    AppComponent,
    DndDirective,
    ProgressComponent,
    routingComponents,
  ],
  imports: [NgSpinnerModule, BrowserModule, HttpClientModule, AppRoutingModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
