
$(document).ready(function () {
    $("#pass1, #pass2").keyup(checkPasswordMatch);
    function checkPasswordMatch() {
            var password = $("#pass1").val();
            var confirmPassword = $("#pass2").val();

            if (password != confirmPassword)
                $("#alert").html("Passwords do not match!");
            else
                $("#alert").html("Passwords match.");
        }
});