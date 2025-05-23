/*! For license information please see clinic-dashboard.js.LICENSE.txt */
"use strict";
document.addEventListener("DOMContentLoaded", function () {
  window.randomScalingFactor = function () {
    return Math.round(20 * Math.random());
  };
  var a = document.getElementById("areachartblue1").getContext("2d"),
    o = a.createLinearGradient(0, 0, 0, 65);
  o.addColorStop(0, "rgba(1, 94, 194, 0.85)"),
    o.addColorStop(1, "rgba(0, 197, 221, 0)");
  var t = {
      type: "bar",
      data: {
        labels: ["1", "2", "3", "4", "5", "7", "8"],
        datasets: [
          {
            label: "# of Votes",
            data: [
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
            ],
            radius: 0,
            backgroundColor: o,
            borderColor: "#015EC2",
            borderWidth: 0,
            borderRadius: 4,
            fill: !0,
            tension: 0.5,
          },
        ],
      },
      options: {
        maintainAspectRatio: !1,
        plugins: { legend: { display: !1 }, tooltip: { enabled: !1 } },
        scales: { y: { display: !1, beginAtZero: !0 }, x: { display: !1 } },
      },
    },
    r =
      (new Chart(a, t),
      document.getElementById("areachartred1").getContext("2d")),
    n = r.createLinearGradient(0, 0, 0, 65);
  n.addColorStop(0, "rgba(240, 61, 79, 0.85)"),
    n.addColorStop(1, "rgba(255, 223, 220, 0)");
  var e = {
      type: "bar",
      data: {
        labels: ["1", "2", "3", "4", "5", "7", "8"],
        datasets: [
          {
            label: "# of Votes",
            data: [
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
            ],
            radius: 0,
            backgroundColor: n,
            borderColor: "#f03d4f",
            borderWidth: 0,
            borderRadius: 4,
            fill: !0,
            tension: 0.5,
          },
        ],
      },
      options: {
        maintainAspectRatio: !1,
        plugins: { legend: { display: !1 }, tooltip: { enabled: !1 } },
        scales: { y: { display: !1, beginAtZero: !0 }, x: { display: !1 } },
      },
    },
    d =
      (new Chart(r, e),
      document.getElementById("areachartgreen1").getContext("2d")),
    l = d.createLinearGradient(0, 0, 0, 65);
  l.addColorStop(0, "rgba(145, 195, 0, 0.85)"),
    l.addColorStop(1, "rgba(176, 197, 0, 0)");
  var i = {
      type: "bar",
      data: {
        labels: ["1", "2", "3", "4", "5", "7", "8"],
        datasets: [
          {
            label: "# of Votes",
            data: [
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
            ],
            radius: 0,
            backgroundColor: l,
            borderColor: "#91C300",
            borderWidth: 0,
            borderRadius: 4,
            fill: !0,
            tension: 0.5,
          },
        ],
      },
      options: {
        maintainAspectRatio: !1,
        plugins: { legend: { display: !1 }, tooltip: { enabled: !1 } },
        scales: { y: { display: !1, beginAtZero: !0 }, x: { display: !1 } },
      },
    },
    c =
      (new Chart(d, i),
      document.getElementById("areachartyellow1").getContext("2d")),
    s = c.createLinearGradient(0, 0, 0, 65);
  s.addColorStop(0, "rgba(253, 100, 0, 0.85)"),
    s.addColorStop(1, "rgba(253, 186, 0, 0)");
  var g = {
      type: "bar",
      data: {
        labels: ["1", "2", "3", "4", "5", "7", "8"],
        datasets: [
          {
            label: "# of Votes",
            data: [
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
              randomScalingFactor(),
            ],
            radius: 0,
            backgroundColor: s,
            borderColor: "#fdba00",
            borderWidth: 0,
            borderRadius: 4,
            fill: !0,
            tension: 0.5,
          },
        ],
      },
      options: {
        maintainAspectRatio: !1,
        plugins: { legend: { display: !1 }, tooltip: { enabled: !1 } },
        scales: { y: { display: !1, beginAtZero: !0 }, x: { display: !1 } },
      },
    },
    p =
      (new Chart(c, g),
      document.getElementById("patientsummary").getContext("2d")),
    m =
      (p.createLinearGradient(0, 0, 0, 120),
      {
        type: "line",
        data: {
          labels: [
            "10:30",
            "11:00",
            "11:30",
            "12:00",
            "12:30",
            "01:00",
            "01:30",
          ],
          datasets: [
            {
              label: "# of Votes",
              data: [
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
              ],
              radius: 0,
              backgroundColor: "rgba(0, 0, 0, 0)",
              borderColor: "#5840ef",
              borderWidth: 2,
              fill: !0,
              tension: 0.5,
            },
          ],
        },
        options: {
          maintainAspectRatio: !1,
          plugins: { legend: { display: !1 } },
          scales: {
            y: { display: !1, beginAtZero: !0 },
            x: { grid: { display: !1 }, display: !0, beginAtZero: !0 },
          },
        },
      }),
    b = new Chart(p, m);
  setInterval(function () {
    m.data.datasets.forEach(function (a) {
      a.data = a.data.map(function () {
        return randomScalingFactor();
      });
    }),
      b.update();
  }, 3e3);
  new Swiper(".swipernonav", {
    slidesPerView: "auto",
    spaceBetween: 16,
    autoplay: { delay: 2e3, disableOnInteraction: !1 },
  }),
    new Swiper(".swiperautononav", {
      slidesPerView: "auto",
      spaceBetween: 0,
      autoplay: !1,
      mousewheel: !0,
    });
  $("#inlinewrap1").daterangepicker(
    {
      singleDatePicker: !0,
      minYear: 2023,
      autoApply: !0,
      linkedCalendars: !1,
      alwaysShowCalendars: !0,
      parentEl: ".inlinewrap1",
      startDate: "19/03/2024",
      endDate: "25/03/2024",
      opens: "center",
      buttonClasses: "btn",
      drops: "up",
      locale: { format: "DD/MM/YYYY" },
      applyButtonClasses: "btn-theme",
      cancelClass: "btn-light",
    },
    function (a, o, t) {}
  ),
    $("#inlinewrap1").length > 0 && $("#inlinewrap1").click();
});
