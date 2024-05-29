// $(document).ready(function () {
//   // jQuery code

//   //////////////////////// Prevent closing from click inside dropdown
//   $(document).on("click", ".dropdown-menu", function (e) {
//     e.stopPropagation();
//   });

//   // make it as accordion for smaller screens
//   if ($(window).width() < 992) {
//     $(".dropdown-menu a").click(function (e) {
//       e.preventDefault();
//       if ($(this).next(".submenu").length) {
//         $(this).next(".submenu").toggle();
//       }
//       $(".dropdown").on("hide.bs.dropdown", function () {
//         $(this).find(".submenu").hide();
//       });
//     });
//   }
// });
(function ($) {
  $(".dropdown-menu a.dropdown-toggle").on("click", function (e) {
    if (!$(this).next().hasClass("show")) {
      $(this)
        .parents(".dropdown-menu")
        .first()
        .find(".show")
        .removeClass("show");
    }
    var $subMenu = $(this).next(".dropdown-menu");
    $subMenu.toggleClass("show");

    $(this)
      .parents("li.nav-item.dropdown.show")
      .on("hidden.bs.dropdown", function (e) {
        $(".dropdown-submenu .show").removeClass("show");
      });

    return false;
  });
});
