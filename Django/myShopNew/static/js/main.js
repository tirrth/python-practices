/* ===============================================================
         PRODUCT QUNATITY
=============================================================== */
function incBtnFn(incBtn) {
  const value = parseInt(incBtn.previousElementSibling.value, 10);
  incBtn.previousElementSibling.setAttribute("value", value + 1);

  incBtn.parentNode.parentNode.parentNode.nextElementSibling.childNodes[0].nextElementSibling.setAttribute(
    "data-addmultiple",
    value + 1
  );

  incBtn.previousElementSibling.previousElementSibling.style.opacity = "1";
}

function decBtnFn(decBtn) {
  const value = parseInt(decBtn.nextElementSibling.value, 10);
  if (value > 1) {
    decBtn.nextElementSibling.setAttribute("value", value - 1);

    decBtn.parentNode.parentNode.parentNode.nextElementSibling.childNodes[0].nextElementSibling.setAttribute(
      "data-addmultiple",
      value - 1
    );
  }

  if (value == 2) {
    decBtn.style.opacity = "0.2";
  }
}

function onAddMultipleChange(inputEle) {
  inputEle.setAttribute("value", inputEle.value);

  inputEle.parentNode.parentNode.parentNode.nextElementSibling.childNodes[0].nextElementSibling.setAttribute(
    "data-addmultiple",
    inputEle.value
  );
}

$(function () {


  /*------------------
      Background Set
  --------------------*/
  $('.set-bg').each(function () {
    var bg = $(this).data('setbg');
    $(this).css('background-image', 'url(' + bg + ')');
  });

  /* ===============================================================
         LIGHTBOX
      =============================================================== */
  lightbox.option({
    resizeDuration: 200,
    wrapAround: true,
  });

  /* ===============================================================
         PRODUCT SLIDER
      =============================================================== */
  $(".product-slider").owlCarousel({
    items: 1,
    thumbs: true,
    thumbImage: false,
    thumbsPrerendered: true,
    thumbContainerClass: "owl-thumbs",
    thumbItemClass: "owl-thumb-item",
  });

  /* ===============================================================
           BOOTSTRAP SELECT
        =============================================================== */
  $(".selectpicker").on("change", function () {
    $(this)
      .closest(".dropdown")
      .find(".filter-option-inner-inner")
      .addClass("selected");
  });

  /* ===============================================================
           TOGGLE ALTERNATIVE BILLING ADDRESS
        =============================================================== */
  $("#alternateAddressCheckbox").on("change", function () {
    var checkboxId = "#" + $(this).attr("id").replace("Checkbox", "");
    $(checkboxId).toggleClass("d-none");
  });

  /* ===============================================================
           DISABLE UNWORKED ANCHORS
        =============================================================== */
  $('a[href="#"]').on("click", function (e) {
    e.preventDefault();
  });
});

/* ===============================================================
     COUNTRY SELECT BOX FILLING
  =============================================================== */
// $.getJSON("js/countries.json", function (data) {
//   $.each(data, function (key, value) {
//     var selectOption =
//       "<option value='" +
//       value.name +
//       "' data-dial-code='" +
//       value.dial_code +
//       "'>" +
//       value.name +
//       "</option>";
//     $("select.country").append(selectOption);
//   });
// });
