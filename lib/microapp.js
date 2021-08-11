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

function fill_images(ele_name, index) {
    var recent = document.getElementById(ele_name);
    var more = document.getElementById(ele_name+'-hidden');
    var imgs = ['f.jpg', 'm.jpg', 'f.jpg', 'm.jpg','f.jpg', 'm.jpg', 'f.jpg', 'm.jpg'];
    more.value = index + imgs.length;

    for (var i=0; i<imgs.length; i++) {
        var ele = document.createElement('img');
        var dd = document.createElement('div');
        dd.classList.add('grid-item');
        ele.setAttribute('src', imgs[i]);
        ele.setAttribute('style', 'width: 72px; height: 72px');
        dd.appendChild(ele)
        recent.appendChild(dd);
        
    }

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
