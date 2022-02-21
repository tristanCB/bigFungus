$(document).ready(function(){
    $('.toggler').on('click','div', function(){
    //   $(this).parent().children().toggle();  //swaps the display:none between the two spans
    console.log($(this))
    console.log($(this).parent().parent())
    console.log($(this).parent().parent().next().css('display'))
    if( $(this).parent().parent().next().css('display') != 'none') {
        $(this).html('<p>See More</p>')
        $(this).css("opacity", "");
        $(this).parent().parent().css("background-color", "")
        $(this).parent().parent().css("box-shadow", "")
    }

    else{
        $(this).html('<p>See Less</p>')
        $(this).css("opacity", 100);
        $(this).parent().parent().css("background-color", "rgba(209, 191, 155, 0.5)")
        $(this).parent().parent().css("box-shadow", "0 0 20px rgba(148, 135, 110, 0.788)")
    }
    // console.log($(this).parent().parent().next())
    // console.log($(this).parent().parent().parent().next())
    console.log("----------------------")
    //$(this).parent().next().slideToggle()



    $(this).parent().parent().siblings().not(".toggled_content").slideToggle();  //swap the display of the main content with slide action
    $(this).parent().parent().next().slideToggle()
});
});

function changeTile(elem) {
    console.log(elem)
    // console.log("==============")
    // if (elem.classList.contains("selected")) {
    //     elem.getElementsByClassName("overlay")[0].style.opacity = 0;
    //     elem.getElementsByClassName("overlay")[0].firstChild.textContent = "See More"
    // }
    // else {
    //     elem.getElementsByClassName("overlay")[0].style.opacity = 100;
    //     elem.getElementsByClassName("overlay")[0].firstChild.textContent = "See Less"
    //     elem.classList.add("selected");
    // }
    // for (const element of document.getElementsByClassName("selected")) {
    //     element.classList.remove("selected");
    // }
}