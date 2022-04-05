const fetchLocation = () => {
  pincode = $("#id_pincode").val();
  const regx = /^\d+$/;
  if (pincode.match(regx)) {
    $.getJSON(
      " https://api.postalpincode.in/pincode/" + pincode,
      function (data) {
        if (data[0].PostOffice != null) {
          var resData = [
            data[0].PostOffice[0].Name,
            data[0].PostOffice[0].District,
          ];
          $("#id_district").val(resData[1]);
          $("#id_city").append(`<option value="${resData[0]}" selected>
              ${resData[0]}
         </option>`);
        }
        else {
          Toastify({
            text: "Error: Invalid Pincode!",
            duration: 3000,
            newWindow: false,
            gravity: "bottom", // `top` or `bottom`
            position: "right", // `left`, `center` or `right`
            stopOnFocus: true, // Prevents dismissing of toast on hover
            style: {
              background: "red",

            },
            // Callback after click
          }).showToast();
        }
      }
    );
  }
  else {
    Toastify({
      text: "Error: Invalid Pincode!",
      duration: 3000,
      newWindow: false,
      gravity: "bottom", // `top` or `bottom`
      position: "right", // `left`, `center` or `right`
      stopOnFocus: true, // Prevents dismissing of toast on hover
      style: {
        background: "red",

      },
      // Callback after click
    }).showToast();
  }
};



$(document).ready(function () {
  $("#id_city").append('<option value="init" selected>Select City</option>');
  $('#id_district').change(function () {
    var optionSelect = $(this).find('option:selected')
    var valueSelected = optionSelect.val()
    district = optionSelect.text()
    data = { 'district': district }
    $.ajax({
      url: '/location/getDistrict/',
      data: data,
      type: 'get',
      success: function (result) {
        var data = JSON.parse(result)
        $("#id_city option").remove();
        if (data.length > 0)
          for (var i = data.length - 1; i >= 0; i--) {
            $("#id_city").append('<option value=' + data[i].name + '>' + data[i].name + '</option>');
          }
      }
    });
  })
})
