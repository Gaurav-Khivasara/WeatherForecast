const placeField = document.getElementById("place"), place = placeField.getAttribute("data-city");
if(!placeField.getAttribute("data-error")) {
  placeField.value = place.charAt(0).toUpperCase() + place.slice(1).toLowerCase();
  placeField.style.borderTopRightRadius = "0";
  placeField.style.borderTopLeftRadius = "0";
  placeField.width = "100px";
  placeField.style.boxShadow = "0 0 30px 1px white inset";
}
else
  placeField.focus();
