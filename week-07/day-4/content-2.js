var lastParContent = document.getElementsByTagName('p');
for (var i = 0; i < lastParContent.length; i++) {
  lastParContent[i].innerHTML = lastParContent[lastParContent.length - 1].innerHTML;
}
