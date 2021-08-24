var Ayoba = getAyoba();

if (typeof(Storage) !== "undefined") {
    alert('Hurray');
} else {
    // Sorry! No Web Storage support..
    alert('Shit man');
}


function getAccordion() {
    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        } 
        /*if (panel.style.display === "block") {
        panel.style.display = "none";
        } else {
        panel.style.display = "block";
        }*/
    });
    }

}

function fill_images(ele_name, data, last) {
    var recent = document.getElementById(ele_name);
    var more = document.getElementById(ele_name+'-hidden');
    var imgs = data;
    more.value = last;

    for (var i=0; i<imgs.length; i++) {
        var source = "https://6uahgo.deta.dev/api/gif_access/v1/" + imgs[i];
        var ele = document.createElement('img');
        var dd = document.createElement('div');
        dd.classList.add('grid-item');
        ele.setAttribute('src', source);
        ele.setAttribute('style', 'width: 72px; height: 72px');
        ele.setAttribute('onclick', 'compose(this.src)')
        dd.appendChild(ele);
        recent.appendChild(dd);
        
    }

}

function createAccordion(data) {

    var main_accord = document.getElementById('accordion');
    var name = "";
    for (name in data) {
        var btn = document.createElement('button');
        btn.classList.add('accordion');
        btn.innerText = name;
        main_accord.appendChild(btn);

        var panel = document.createElement('div');
        panel.classList.add('panel');

        var cont = document.createElement('div');
        cont.classList.add('grid-container');
        cont.setAttribute('id', name);

        panel.appendChild(cont);

        var o_div = document.createElement('div');

        var a = document.createElement('a');
        a.setAttribute('href', '#');
        a.setAttribute('onclick', 'getMore(this.nextElementSibling.value, this.parentElement.parentElement)');
        a.innerText = "More";

        o_div.appendChild(a);

        var hidd = document.createElement('input');
        hidd.setAttribute('type', 'hidden')
        hidd.setAttribute('id', name+'-hidden');

        o_div.appendChild(hidd);

        panel.appendChild(o_div);
        main_accord.appendChild(panel);

        var items = data[name]['items'];
        var last = data[name]['last'];

        fill_images(name, items, last);

    }

    getAccordion();

}

function getImages() {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var obj = JSON.parse(this.responseText);
            createAccordion(obj);
        }
    };
    xhttp.open("GET", "https://6uahgo.deta.dev/api/gif_access/v1/gifs", true);
    xhttp.send();

}



function getMore(start_ind, panel) {
    fill_images('funny', start_ind);
    panel.style.maxHeight = panel.scrollHeight + "px";
}


/**
* Determine the mobile operating system and returns the
* proper javascript interface
*/
function getAyoba() {
   var userAgent = navigator.userAgent || navigator.vendor || window.opera;
 
   // Windows Phone must come first because its UA also contains "Android"
   if (/windows phone/i.test(userAgent)) {
       return null;
   }
 
   if (/android/i.test(userAgent)) {
       return Android;
   }
 
   // iOS detection from: http://stackoverflow.com/a/9039885/177710
   if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
       return null; // todo
   }
 
   return "unknown";
}

function sayHello() {
    //alert('Hello Ayoba!');
}
