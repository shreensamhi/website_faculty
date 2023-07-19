document.getElementById("myButton").onclick = function () 
{
        location.href = "file:homepage";
        function myFunction() 
        {
            document.getElementById("button").innerHTML;
        };
}

function myFunction() 
{
    var enter, change, ul, li, a, i, textValue;
    enter = document.getElementById("search");
    change = enter.value.toUpperCase();
    ul = document.getElementById("unordered");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) 
    {
        a = li[i].getElementsByTagName("a")[0];
        textValue = a.textContent || a.innerText;
        if (textValue.toUpperCase().indexOf(change) > -1) 
        {
            li[i].style.display = "";
        } 
        else 
        {
            li[i].style.display = "none";
        }
    }
}

function showAlert() 
{
    var myText = "Are You Sure You Want To Delete The Data?";
    alert (myText);
}
function checkForm() 
{
    var studentname = document.getElementById("s").Value;
    var id = document.getElementById("i").Value;
    var gpa = document.getElementById("g").Value;
    var level = document.getElementById("l").Value;
    var email = document.getElementById("e").Value;
    var department = document.getElementById("t").Value;
    var phonenum = document.getElementById("n").Value;
    if(studentname === "")
    {
        alert("Error : student name cannot blank!");
        document.getElementById("s").focus();
        return false;
    }
    if (id!=" ")
    {
            alert("Error: please check that you have entered and confirmed your ID!");
            document.getElementById("i").focus();
            return false;
    
    }
    if(gpa==" ")
    {
        alert("Error : Your GPA cannot blank!");
        document.getElementById("g").focus();
        return false;
    }
    if(level>4 || level<1 || level=="")
    {
        alert("Error : Your Level isnot correct!");
        document.getElementById("l").focus();
        return false;
    }
    if(email=="")
    {
        alert("Error : Your email cannot blank!");
        document.getElementById("e").focus();
        return false;
    }
    if(department=""||department== Number)
    {
        alert("Error : Your department isnot correct!");
        document.getElementById("t").focus();
        return false;
    }
    if(phonenum==""||phonenum.length<11)
    {
        alert("Error : Your phonenumber isnot correct!");
        document.getElementById("n").focus();
        return false;
    }
}