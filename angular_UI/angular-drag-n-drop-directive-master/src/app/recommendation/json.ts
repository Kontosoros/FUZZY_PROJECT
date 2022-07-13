export const json = {
  pages: [
    {
      elements: [
        {
          type: "panel",
          name: "age",
          elements: [
            {
              type: "text",
              name: "age",
              title: "Age:",
              isRequired: true,
              inputType: "number",
              min: 0,
              max: 100,
            },
            {
              type: "text",
              name: "Cigarettes",
              title: "Cigarettes per Day (0 - 50):",
              startWithNewLine: false,
              isRequired: true,
              inputType: "number",
              min: 0,
              max: 50,
            },
          ],
          questionTitleLocation: "top",
          title: "Age & Cigarettes",
        },
        {
          type: "panel",
          name: "panel2",
          elements: [
            {
              type: "text",
              name: "Exercise",
              title: "Exercise per Weeks (Days):",
              startWithNewLine: false,
              isRequired: true,
              inputType: "number",
              min: 0,
              max: 7,
            },
            {
              type: "text",
              isRequired: true,
              name: "Eating unhealthy",
              startWithNewLine: false,
              inputType: "number",
              title: "Eat Fast Food (Times per Week):",
              min: 0,
              max: 7,
            },
            {
              type: "text",
              isRequired: true,
              name: "Anxiety",
              startWithNewLine: false,
              inputType: "number",
              title: "Anxiety (0 -100):",
              min: 0,
              max: 100,
            },
          ],
          questionTitleLocation: "top",
          title: "Exercise, Anxiety & Fast Food",
        },
      ],
    },
  ],
  showProgressBar: "top",
  showQuestionNumbers: "on",
  title: "Daily Habits",
};
