var updateBtns = document.getElementsByClassName("update-cart");

for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;

    var addMultipleNumber = 0;

    if (action == "addmultiple") {
      addMultipleNumber = this.dataset.addmultiple;
    }

    updateCookieItem(productId, action, addMultipleNumber);
  });
}

function updateCookieItem(productId, action, addMultipleNumber) {
  if (action == "add") {
    if (cart[productId] == undefined) {
      cart[productId] = { quantity: 1 };
    } else {
      cart[productId]["quantity"] += 1;
    }
  }

  if (action == "addmultiple") {
    if (cart[productId] == undefined) {
      cart[productId] = { quantity: parseInt(addMultipleNumber, 10) };
    } else {
      cart[productId]["quantity"] += parseInt(addMultipleNumber, 10);
    }
  }

  if (action == "remove") {
    cart[productId]["quantity"] -= 1;

    if (cart[productId]["quantity"] <= 0) {
      delete cart[productId];
    }
  }

  if (action == "delete") {
    delete cart[productId];
  }

  document.cookie = "cart" + "=" + JSON.stringify(cart) + ";domain=;path=/";
  location.reload();
}
