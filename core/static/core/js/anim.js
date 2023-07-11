// NAV BAR //
$(document).ready(function() {
  var visible= $("#navitems").is(":visible");
  var visible= $("#navitems2").is(":visible");
  $('.navbar').removeClass('bg-dark').addClass('bg-transparent');
  $('.inb').removeClass('btn-outline-danger').addClass('btn-danger');
  $("#navitems2").show();
  $("#navitems").hide();
});

$(document).scroll(function() {

if ($(this).scrollTop() < 100) {
  $('.navbar').removeClass('bg-dark').addClass('bg-transparent');
  $('.inb').removeClass('btn-outline-danger').addClass('btn-danger');
  $("#navitems2").show();
  $("#navitems").hide();
} else {
  $('.navbar').removeClass('bg-transparent').addClass('bg-dark');
  $('.inb').removeClass('btn-danger').addClass('btn-outline-danger');
  $("#navitems2").hide();
  $("#navitems").show();
}
});

