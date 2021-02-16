window.onload = function(){
  var gSearch = document.getElementById("gSearch");
  let storedLogo = localStorage.getItem('preferredEngine');
  let currentLogo;

  if (!storedLogo)
  {
    currentLogo = document.getElementById("engineLogo").src;
    localStorage.setItem('preferredEngine', currentLogo);
  } else
  {
    if (storedLogo.indexOf("duck.svg") != -1)
    {
      document.getElementById("engineLogo").src = "icons/google.svg";
      gSearch.children[0].action = 'https://google.com/search';
    } else
    {
      document.getElementById("engineLogo").src = "icons/duck.svg";
      gSearch.children[0].action = 'https://duckduckgo.com/';
    }
  }
}