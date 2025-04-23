'use strict';

const p = document.querySelector('#trigger');
p.addEventListener('mouseover', function(evt){
    document.querySelector('#target').src = "img/picB.jpg";
});
p.addEventListener('mouseleave', function(evt){
    document.querySelector('#target').src = "img/picA.jpg";
});
