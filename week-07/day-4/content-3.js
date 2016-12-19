var paragraphs = document.getElementsByTagName('p');
var secondPar = document.getElementsByClassName('output1');
var thirdPar = document.getElementsByClassName('output2');

secondPar.innerHTML = paragraphs[0].textContent;
thirdPar.innerHTML = paragraphs[0].innerHTML;
