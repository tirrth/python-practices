var wishListBtns = document.getElementsByClassName("update-wish");

for (i = 0; i < wishListBtns.length; i++) {
  wishListBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;

    updateWishList(productId);
  });
}

function updateWishList(productId) {
  if (!wish_list.includes(productId)) {
    wish_list.push(productId);
    document.cookie =
      "wish_list" + "=" + JSON.stringify(wish_list) + ";domain=;path=/";
  }
  location.reload();
}
