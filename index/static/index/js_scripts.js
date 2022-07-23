//This function will initalize the page

function pageInit() {
  let url = window.location.pathname;

  //This will set the navigation header with the right class dependent on location

  switch (url) {
    case "/":
      let home = document.getElementById("homeLink");
      home.classList.replace("link-dark", "link-secondary");
      break;

    case "/contact_us/":
      let contactUs = document.getElementById("contactUsLink");
      contactUs.classList.replace("link-dark", "link-secondary");
      break;

    case "/conference/":
      let conference = document.getElementById("conferenceLink");
      conference.classList.replace("link-dark", "link-secondary");
      break;

    case "/about_us/":
      let aboutUs = document.getElementById("aboutUsLink");
      aboutUs.classList.replace("link-dark", "link-secondary");
      break;

    case "/sponsor/":
      let sponsor = document.getElementById("sponsorLink");
      sponsor.classList.replace("link-dark", "link-secondary");
      break;

    case "/subscribe/":
      let subscribe = document.getElementById("subscribeLink");
      subscribe.classList.replace("link-dark", "link-secondary");
      break;

    case "/shoey/":
      let shoey = document.getElementById("shoeyLink");
      shoey.classList.replace("link-dark", "link-secondary");
      break;
  }
}
