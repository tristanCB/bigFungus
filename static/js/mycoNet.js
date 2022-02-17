
function filter(e) {
    var filters = document.getElementsByClassName('selector')[0].children;
    console.log(filters)

    for (let item of filters) 
        {item.classList.remove('selected')};

    console.log(e)
    e.target.classList.add('selected');
    
    console.log(e.srcElement.innerHTML)
    var elements = document.querySelectorAll(`[class="paneWrap"]`);
    // var elements = document.querySelectorAll(`[data="${e.srcElement.innerHTML}"]`);
    elements.forEach((element) => {
        if (e.srcElement.innerHTML == "All") {
            element.style.display = 'inherit';
        }
        else{
            console.log({ element });
            console.log(element.getAttribute('data'))
            console.log(e.srcElement.innerHTML)

            if (element.getAttribute('data') != e.srcElement.innerHTML) {
                element.style.display = 'none';
            }
            else {
                element.style.display = 'inherit';
            }
        }
      });
    
}