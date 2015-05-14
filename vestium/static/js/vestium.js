function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(function() {

    var email_regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;      
    var username_regex = /^([a-zA-Z0-9_]{1,63})+$/;
    var email_error = false;
    var username_error = false;
    $("#signup_forms_submit").bind('click', function () {

      var email = $("#signup_email").val();
      var username = $("#signup_username").val();

      if (!email_regex.test(email) || !username_regex.test(username)){
        $("#signup_email").trigger('keyup');
        $("#signup_username").trigger('keyup');
        return false; 
      }

      $.ajax({
          type:"POST",
          data:{
            'username':username,
            'email':email
          },
          url: '/api/v1/register',//this is the default though, you don't actually need to always mention it
          success: function(response) {

            if(response.valid) {
            
              var stat = $('.footer_stat .number');
              stat.text(parseInt(stat.attr('data-users')) + 1);
              $("#signup_forms_submit span.account_btn").text("Your place has been reserved.");
              $("#signup_forms_submit").addClass('submitted');
              
               $("#signup_email").attr('disabled','disabled');
               $("#signup_username").attr('disabled','disabled');
               $("#signup_forms_submit").attr('disabled','disabled');


            } else {
              email_error = true;
              username_error = true;
           $("#signup_email").addClass('error');
           $("#signup_username").addClass('error');
            $("#signup_forms_submit").addClass('buttonError');
            $("#signup_forms_submit").attr('disabled','disabled');

            }
          }
         });
    });

    // $("#signup_email").bind('keyup', function () {

    //   if (!$(this).val()) {
    //     email_error = false;
    //     $($(this).next().removeClass('error'));



    //   } else if(email_regex.test($(this).val())){
    //     // Valid email, lets check if it already exists.  
    //     $($(this).next().removeClass('error'));
    //     email_error = false;


    //   } else {
    //     email_error = true;

    //     $($(this).next().addClass('error'));
    //     $("#signup_forms_submit").addClass('buttonError');
    //     $("#signup_forms_submit").attr('disabled','disabled');
    //   }

    // });

    // $("#signup_username").bind('keyup', function () {


    //   if (!$(this).val()) {
    //     username_error = false;
    //     $($(this).next().removeClass('error'));

    //   } else if(username_regex.test($(this).val())){
    //     // Valid email, lets check if it already exists.
    //     $($(this).next().removeClass('error'));
    //     username_error = false;


    //   } else {

    //     $($(this).next().addClass('error'));
    //   $("#signup_forms_submit").addClass('buttonError');
    //   $("#signup_forms_submit").attr('disabled','disabled');
    //   username_error = true;


    //   }

    // });


    $("#signup_email").bind('input blur', function () {

      var email = $("#signup_email");

      
      if(!email_regex.test(email.val())){
        $(email).next().addClass('error');
        email_error = true;
         $("#signup_forms_submit").addClass('buttonError');
         $("#signup_forms_submit").attr('disabled','disabled');
         username_error = true;
        return false;
      }


      $.ajax({
          type:"POST",
          data:{
            'email':email.val()
          },
          url: '/api/v1/check_email_address',//this is the default though, you don't actually need to always mention it
          success: function(response) {

            if(response.valid) {
              $("#signup_email").next().removeClass('error');

              email_error = false;

              if (!username_error){
                  $("#signup_forms_submit").removeClass('buttonError');
                  $("#signup_forms_submit").removeAttr('disabled');
              }
            } else {

              email_error = true;

              $("#signup_email").next().addClass('error');
              $("#signup_forms_submit").addClass('buttonError');
              $("#signup_forms_submit").attr('disabled','disabled');

            }
            

          }
      });
    });

    $("#signup_username").bind('input blur', function () {

      var username = $("#signup_username");

      if(!username_regex.test(username.val())){
        $(username).next().addClass('error');
        $("#signup_forms_submit").addClass('buttonError');
        $("#signup_forms_submit").attr('disabled','disabled');
        return false;
      }
      $.ajax({
          type:"POST",
          data:{
            'username':username.val(),
          },
          url: '/api/v1/check_username',//this is the default though, you don't actually need to always mention it
          success: function(response) {

            if(response.valid) {

              $("#signup_username").next().removeClass('error');

              username_error = false;

              if (!email_error){
                  $("#signup_forms_submit").removeClass('buttonError');
                  $("#signup_forms_submit").removeAttr('disabled');
              }

            } else {

              username_error = true;

              $("#signup_username").next().addClass('error');

              $("#signup_forms_submit").addClass('buttonError');
              $("#signup_forms_submit").attr('disabled','disabled');
            }

          }
      });
    });

    $('#signup_form').submit(function(){

      if ($("#signup_email").is(":focus")){

        $('#signup_username').trigger('touchstart'); 
    
        return false;

      } else { 

        if(!email_regex.test($("#signup_email").val())){
          return false;
        }

        if(!username_regex.test($("#signup_username").val())){
          return false;
        }

      }
    })

    $('input').on('touchstart', function () {
        $(this).focus();   // inside this function the focus works
    });

});