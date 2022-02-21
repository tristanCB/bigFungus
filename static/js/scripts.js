function refreshCart()
{
    cart =  JSON.parse(sessionStorage.getItem("cart"))
    if (cart == null) {
        return
    }
    cartElem = document.getElementById("Cart");
    cartElem.innerHTML = ''
    cart.forEach(element => {
        cartElem.innerHTML += 
        `<p>${element['name']} X ${element['qty']}</p>
        <input name="${element['prod']}" value="${element['qty']}" type="hidden"></input>
        `
    });

    // cartElem.innerHTML += 
    //     `<p>${prod['name']} ---> ${value}</p>
    //     <input name="${itemCode}" value="${value}" type="hidden"></input>
    //     `;

    refreshCartTotal();
    console.log(sessionStorage)
}

function addItem(prod, itemCode, productName) {
    console.log("Here")
    console.log(prod)
    var select = document.getElementById(productName).getElementsByClassName("amount")[0];
    var value = select.options[select.selectedIndex].value;

    cart =  JSON.parse(sessionStorage.getItem("cart"))

    if (cart == null) {
        cart = [{prod: itemCode, qty:value, name:prod['name']}]
    }
    else {
        var alreadyInCart = false;
        cart.forEach(element => {
            if (element["prod"] == itemCode){
                indexMatch = cart.indexOf(element);
                alreadyInCart = true;
            }
        });

        if (alreadyInCart) {
            cart[indexMatch] = {prod: itemCode, qty:value, name:prod['name']}
        }
        else{
            cart.push({prod: itemCode, qty:value, name:prod['name']})
        }
    }
    sessionStorage.setItem("cart", JSON.stringify(cart))
    refreshCart()
  }

function refreshCartTotal() {
    var tot = document.getElementById("Cart").childElementCount/2;
    var totElem = document.getElementById("CartTotal")
    if (tot == 0) {    
        totElem.textContent = "";
    }
    else{
        totElem.textContent = tot;
        displayCart()
    }
}
function displayCart(){
    document.getElementById("CartMenu").style.display = "block";
}
function clearCart() {
    document.getElementById("Cart").innerHTML = " ";
    sessionStorage.clear();
    refreshCartTotal();
    toogleCart();
}

function toogleCart() {
    var x = document.getElementById("CartMenu");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function getPage() {
    console.log(window.location.href)
    return window.location.href
}

window.onload = refreshCart();


