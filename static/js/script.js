/* JQuery code from materialize.css */
$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      showClearBtn: "true",
      maxDate: new Date(),
    });
    $('.modal').modal();
  });