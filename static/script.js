$(document).ready(function() {
  $('#checkBtn').click(function() {
      var password = $('#password').val();
      $.ajax({
          type: 'POST',
          contentType: 'application/json',
          url: '/check_password_strength',
          data: JSON.stringify({password: password}),
          success: function(response) {
              var strength = response.score;
              var feedback = response.feedback;
              var isCommonPassword = response.common_password;

              $('#strengthMeter').removeClass().addClass('strength-' + strength).text('Strength: ' + strength);
              
              // Display feedback
              var feedbackText = feedback.join('<br>');
              if (isCommonPassword) {
                  feedbackText += '<br>This password is commonly used. Please choose a more secure one.';
              }
              $('#feedback').html(feedbackText);
          }
      });
  });
});
