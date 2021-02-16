function toggleEngine() {
  var gSearch = document.getElementById("gSearch");
  var logo = document.getElementById("engineLogo").src;
  localStorage.setItem('preferredEngine', logo);

  if (logo.indexOf("duck.svg") != -1) {
    document.getElementById("engineLogo").src = "icons/google.svg";
    gSearch.children[0].action = 'https://google.com/search';
  } else {
    document.getElementById("engineLogo").src = "icons/duck.svg";
    gSearch.children[0].action = 'https://duckduckgo.com/';
  }
  document.getElementById("textField").innerHTML = null;
}

// let set_weather = () => {
//   fetch('https://wttr.in/?format="%C:%f"')
//   .then(response => response.text())
//   .then(
//       data => {
//         data = data.replaceAll('"', '').split(':');
//         document.getElementById('temprature').innerHTML = data[1].substring(1, data[1].length-2) + "&deg;c";
//         document.getElementById('weatherdescription').innerHTML = data[0];
//         localStorage.setItem('temperature', data[1].substring(1, data[1].length-2) + "&deg;c");
//         localStorage.setItem('weatherdescription', data[0]);
//       }
//   ).catch(error => {
//     var temperature = localStorage.getItem('temperature');
//     var description = localStorage.getItem('weatherdescription');
//     if (!temperature && !description){
//       document.getElementById('temprature').innerHTML = "Weather Not Available";
//     }
//     else{
//       document.getElementById('temprature').innerHTML = temperature;
//       document.getElementById('weatherdescription').innerHTML = description;
//     }
//   });
// }

// set_weather();