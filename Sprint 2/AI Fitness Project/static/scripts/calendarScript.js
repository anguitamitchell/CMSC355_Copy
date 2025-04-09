let display = document.querySelector(".display");
let previous = document.querySelector(".left");
let next = document.querySelector(".right");
let days = document.querySelector(".days");
let selected = document.querySelector(".selected");

let today = new Date();
let date = new Date(today);
let year = date.getFullYear();
let month = date.getMonth();


function calendarDisplay() {
  days.innerHTML = '';

  let formattedDate = date.toLocaleString("en-US", {
    month: "long",
    year: "numeric",
  });
  display.innerHTML = formattedDate;

  const firstDay = new Date(year, month, 1);
  const firstDayIndex = firstDay.getDay();

  const lastDay = new Date(year, month + 1, 0);
  const numberOfDays = lastDay.getDate();

  for (let x = 1; x <= firstDayIndex; x++) {
    let div = document.createElement("div");
    div.classList.add("days");
    div.innerHTML = "";
    days.appendChild(div);
  }

  for (let i = 1; i <= numberOfDays; i++) {
    let div = document.createElement("div");

    div.classList.add("day");
    div.innerHTML = i;
    days.appendChild(div);

    let currentDate = new Date(year, month, i);
    if (
      currentDate.getFullYear() === new Date().getFullYear() &&
      currentDate.getMonth() === new Date().getMonth() &&
      currentDate.getDate() === new Date().getDate()
    ) {
      div.classList.add("current-date");
    }
  }

  displaySelected();
}

function displaySelected() {
    const dayElements = document.querySelectorAll(".days div");
    dayElements.forEach((day) => {
      day.addEventListener("click", (e) => {
        const selectedDate = e.target.dataset.date;
        selected.innerHTML = `Selected Date : ${selectedDate}`;
        window.open("/Sprint 2/AI Fitness Project/templates/fitness-log.html", '_blank')
      });
    });
  }
  displaySelected();

previous.addEventListener("click", () => {
  month--;
  if (month < 0) {
    month = 11;
    year--;
  }
  date.setFullYear(year, month);
  calendarDisplay();
});

next.addEventListener("click", () => {
  month++;
  if (month > 11) {
    month = 0;
    year++;
  }
  date.setFullYear(year, month);
  calendarDisplay();
});

calendarDisplay();
