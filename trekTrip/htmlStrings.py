'''
Created on Jul 21, 2015

@author: Florida

This is where the html string definitions are;
'''


   
    
# defining default variable to go into template_values;
dummyvalue="<p>dummy Paragraph</p>";
defaultBackgroundImg='''
<img src="/images/blank.jpg" >

'''
testText='';    # This string was produced to make tests and debugging from the DB;

# defining the default template_values;

homeLink='''/default''';
greetings= '';
firstName='';
lastName='';
userName=' ';
comments='';
loginForm='''

'''
logOut='''
    
   
    <script>
        function logOut()
    {
        
        document.getElementsByName("userName")[0].value="logOut";
        document.getElementsByName("logOutButton")[0].value="ON";
        
        //document.getElementById("demo").innerHTML =document.getElementsByName("userName")[0].value;
        //location.reload(); //reloading the page to have the changes iterated;
    }
    </script>
    <form method ="post">
        <input name="userName" type="text" value=" ">
        <input name="logOutButton" type="text" value=" ">
        <button  onclick="logOut()">logOut</button>
    </form>
'''



template_values={
                         
             'firstName':'',
             'lastName':'',
             'testP':dummyvalue,
             'greetings': greetings,
             'loginForm':loginForm,
             'comments':comments,
             
             
             
             };
             