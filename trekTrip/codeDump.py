'''
Created on Jul 21, 2015

@author: Florida

This is a code dump; Mainly to keep track of where the code to be deleted
is being dumped for possible future use;
'''



'''
#fetchCredentialsDB(self) ;
        #logOutB=self.request.get('logOutButton');
        #strB=str(logOutB);
        
        #if fetchCredentialsDB(self)==True:
        #loggedIn='Logged In';
        #template_values.update({'firstName':firstName,'lastName':lastName,'loginForm':logOut, 'homeLink':'/userHome'});
      #  else:
      
       #session=get_current_session();
        #session.terminate()
        
        
        #logOutB=self.request.get('logOutButton');
        #strB=str(logOutB);
        
        # if logout text was submitted properly, this should log out;
        if fetchCredentialsDB(self)==True:
            # Check for another button because the credentials are still good. Login is still working;
            loggedIn='Logged In';
            template_values.update({'firstName':firstName,'lastName':lastName,'loginForm':logOut, 'homeLink':'/userHome'});
            getComments(self);
            template_values.update({'comments':comments});
            template=jinja_environment.get_template('userHome.html');
            self.response.out.write(template.render(template_values));
        else:
            
            template=jinja_environment.get_template('default.html');
            session=get_current_session();
            session['userName']=userName;
            logInfo=str(session['userName']);
            session.terminate()
            template_values.update({'firstName':'','lastName':'','loginForm':loginForm, 'homeLink':'/default','testP':logInfo});
            template_values.update({'backgroundImg':defaultBackgroundImg});
            self.response.out.write(template.render(template_values));
        
        
        #template_values.update({'firstName':firstName,'lastName':lastName,'loginForm':loggedIn});
        #getComments(self);
        #template_values.update({'comments':comments});
        #template=jinja_environment.get_template('userHome.html');
        #self.response.out.write(template.render(template_values));
        
        
        
        
<div class="loginForm">
    <form method ="post">
        <label for="userName"> Username: </label>
        <input name="userNameLogin" type="text" value="user"><br/>
        <label for="password"> Password: </label>
        <input name="password" type="text" value="pass"> <br/>
    <input name="loginButton" type="submit" value="Login">

    </form>

</div>


<div id=VenueCreation class="VenueCreation">
    <form method="post">
        <input name="venueName" class="rounded" type="text" placeholder="VenueName"> <br/> <br/>
        <input name="venueType" class="rounded" type="text" placeholder="Bar,Club,Restaurant ...?"> <br/> <br/>
        <textarea name="VenueDescription" rows="4" cols="50" placeholder="Description" class="roundedTextArea"></textarea> <br/> <br/>
        <input name="venueAddress" class="rounded" type="text" placeholder="Address"> <br/> <br/>
        <input name="venueCity" class="rounded" type="text" placeholder="City"> <br/> <br/>
        <select name = venueState class="roundedSelect" placeholder="State">
            <option value="">Choose State</option>
            <option value="AL">Alabama</option>
            <option value="AK">Alaska</option>
            <option value="AZ">Arizona</option>
            <option value="AR">Arkansas</option>
            <option value="CA">California</option>
            <option value="CO">Colorado</option>
            <option value="CT">Connecticut</option>
            <option value="DE">Delaware</option>
            <option value="DC">District Of Columbia</option>
            <option value="FL">Florida</option>
            <option value="GA">Georgia</option>
            <option value="HI">Hawaii</option>
            <option value="ID">Idaho</option>
            <option value="IL">Illinois</option>
            <option value="IN">Indiana</option>
            <option value="IA">Iowa</option>
            <option value="KS">Kansas</option>
            <option value="KY">Kentucky</option>
            <option value="LA">Louisiana</option>
            <option value="ME">Maine</option>
            <option value="MD">Maryland</option>
            <option value="MA">Massachusetts</option>
            <option value="MI">Michigan</option>
            <option value="MN">Minnesota</option>
            <option value="MS">Mississippi</option>
            <option value="MO">Missouri</option>
            <option value="MT">Montana</option>
            <option value="NE">Nebraska</option>
            <option value="NV">Nevada</option>
            <option value="NH">New Hampshire</option>
            <option value="NJ">New Jersey</option>
            <option value="NM">New Mexico</option>
            <option value="NY">New York</option>
            <option value="NC">North Carolina</option>
            <option value="ND">North Dakota</option>
            <option value="OH">Ohio</option>
            <option value="OK">Oklahoma</option>
            <option value="OR">Oregon</option>
            <option value="PA">Pennsylvania</option>
            <option value="RI">Rhode Island</option>
            <option value="SC">South Carolina</option>
            <option value="SD">South Dakota</option>
            <option value="TN">Tennessee</option>
            <option value="TX">Texas</option>
            <option value="UT">Utah</option>
            <option value="VT">Vermont</option>
            <option value="VA">Virginia</option>
            <option value="WA">Washington</option>
            <option value="WV">West Virginia</option>
            <option value="WI">Wisconsin</option>
            <option value="WY">Wyoming</option>
        </select> <br /> <br/>
        <div class="registerButton">
        <input type="submit" class="searchButton" value="Create Venue">
        </div>
    </form>
    </div>
    
    
        {% for v in venues %}
                        <p> {{v}} </p>
                    {% endfor %}
                </p>
    
    
    while (i<Number({{lengthOfPlaces}}))
                          {
                              //document.getElementById("AttractionTestDiv").innerHTML=i+'<br>';
                              
                              //location= new google.maps.LatLng(
                              
                  
                              i++;
                          }

'''