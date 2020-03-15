function validate_signup_pat() {
       var returnval = true;
       var x = document.getElementById("form");
       var aadhar = document.getElementById("aadhar").value;


            if(aadhar_len!=12)
            {
                alert("Enter 12 Digit Aadhar number");
                aadhar.focus() ;
                returnval = false;

            }


       var phoneno= document.getElementById("phone_number").value;
       var phone_len = phoneno.length;
       if(!phoneno.match(numbers))
            {
               alert("Mobile no must be Digit");
               returnval = false;
            }
            if(phone_len!=10)
            {
                alert("Enter 10 Digit Mobile No");
                returnval = false;
            }


       var pass_val = document.getElementById("password").value;
        var confirm_val = document.getElementById("confirm").value;
        if (pass_val != confirm_val) {
            alert("Passwords do not match.");
            returnval = false;
        }

        if(returnval == true)
        {
                x.action="/account/signup_pat/";
        }
        else
        {
            x.action="patient.html";
        }
}