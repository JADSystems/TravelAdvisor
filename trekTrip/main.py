

import webapp2

import jinja2;
import os,sys;
import MySQLdb;
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers
from gaesessions import get_current_session;

# defining the jinja2 hook to utilize for accessing the templates;

jinja_environment= jinja2.Environment(
                                      
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"));

# Defining globals;

greetings= '';
firstName='';
lastName='';
comments='';
loginForm='''
<div class="loginForm">
    <form method ="post">
        <label for="userName"> Username: </label>
        <input name="userName" type="text" value="root"><br/>
        <label for="password"> Password: </label>
        <input name="password" type="text" value="pass0"> <br/>
    <input name="loginButton" type="submit" value="Login">

    </form>

</div>

'''
logOut='''
<form method ="post">
    <input name="userName" type="hidden" value=" ">
    <input name="logOutButton" type="submit" value="LogOut">
</form>
'''


    
    
# defining default variable to go into template_values;
dummyvalue="<p>dummy Paragraph</p>";
defaultBackgroundImg='''
<img src="/images/brooklynBridge0.jpg" >

'''
testText='';    # This string was produced to make tests and debugging from the DB;

# defining the default template_values;

template_values={
                         
             'firstName':'',
             'lastName':'',
             'testP':dummyvalue,
             'greetings': greetings,
             'loginForm':loginForm,
             'comments':comments,
             
             
             
             };
             
#----------------------------------------------------------      
def fetchCredentialsDB(web):
    # Web will be the variable self passed through to be used; 
    global firstName,lastName;
    session=get_current_session();
    userName=session.get('userName',' ');
    password=session.get('password',' ');
    env = os.getenv('SERVER_SOFTWARE');
    if (env and env.startswith('Google App Engine/')):
        # Connecting from App Engine
        db = MySQLdb.connect(
        unix_socket='/cloudsql/trektip:trektipsql',
        user='root',passwd='TfReETO88zFyArUa65za');
    else:
        # Connecting from an external network.
        # Make sure your network is whitelisted
        db = MySQLdb.connect(
        host='173.194.248.180',
        port=3306,
        user='root',
        passwd='TfReETO88zFyArUa65za');
    cursor=db.cursor();
    
    #username=web.request.get("username");
    #passKey=web.request.get("password");
    getUserName='''
        select trektip.User.userName from trektip.User
        where trektip.User.userName='%s';
    '''%userName;
    cursor.execute(getUserName);
    userNameDB='';
    userNameDB+=str(cursor.fetchone());
    if userNameDB.__contains__(userName):
        
        firstName=userNameDB+'firstName';
        lastName=userNameDB+'lastName';
    else:
        
        return False;
   
    
#         for i in cursor.fetchall():
#             firstName+=str(i);
   
    getPassword='''
        select trektip.User.passKey from trektip.User
        where trektip.User.userName='%s';
    '''%userName;
    cursor.execute(getPassword);
    passwordDB='';

    passwordDB+=str(cursor.fetchone());
    if passwordDB.__contains__(password):
        
        return True;
    else:
        
        return False;
    
#----------------------------------------------------------

def getComments(web):
    global comments;
    session=get_current_session();
    userName=session.get('userName',' ');
    env = os.getenv('SERVER_SOFTWARE');
    if (env and env.startswith('Google App Engine/')):
        # Connecting from App Engine
        db = MySQLdb.connect(
        unix_socket='/cloudsql/trektip:trektipsql',
        user='root',passwd='TfReETO88zFyArUa65za');
    else:
        # Connecting from an external network.
        # Make sure your network is whitelisted
        db = MySQLdb.connect(
        host='173.194.248.180',
        port=3306,
        user='root',
        passwd='TfReETO88zFyArUa65za');
    cursor=db.cursor();
    
    #username=web.request.get("username");
    #passKey=web.request.get("password");
    getAllComments='''
        SELECT distinct c.ID, c.rating, c.infoID, i.infoText
        FROM trektip.Comment c, trektip.User u, trektip.Information i
        where c.userName='%s'
        and u.userName='%s'
        and c.ID=i.commentID;
    '''%(userName,userName);
    cursor.execute(getAllComments);
    comments='<h2>COMMENTS</h2> <BR/>';
    for r in cursor.fetchall():
        comments+= str(r)+'<br/>';
    
    
    
    
    
    

#----------------------------------------------------------
        
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template=jinja_environment.get_template('testLogin.html');
        self.response.out.write(template.render(template_values));            


#----------------------------------------------------------

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #fetchCredentialsDB(self) ;
        logOutB=self.request.get('logOutButton');
        #strB=str(logOutB);
        
        if fetchCredentialsDB(self)==True:
            loggedIn='Logged In';
            template_values.update({'firstName':firstName,'lastName':lastName,'loginForm':logOut});
        else:
            template_values.update({'firstName':'','lastName':'','loginForm':loginForm});
            
        template_values.update({'backgroundImg':defaultBackgroundImg});
        template=jinja_environment.get_template('default.html');
        self.response.out.write(template.render(template_values));
  
        
    def post(self):
        
        logOutB=self.request.get('logOutButton');
        #strB=str(logOutB);
        session=get_current_session();
        userName=self.request.get('userName');
        password=self.request.get('password');
        session['userName']=userName;
        session['password']=password;
        if fetchCredentialsDB(self)==True:
            loggedIn='';
            template_values.update({'firstName':firstName,'lastName':lastName,'loginForm':logOut});
        else:
            template_values.update({'testP':'Error in Credentials'});
            template=jinja_environment.get_template('default.html');
            self.response.out.write(template.render(template_values));
            return;
            
        #template_values.update({'firstName':firstName,'lastName':lastName,'loginForm':loggedIn});
        getComments(self);
        template_values.update({'comments':comments});
        template=jinja_environment.get_template('userHome.html');
        self.response.out.write(template.render(template_values));
i=0;

#----------------------------------------------------------        
class TestHandler(webapp2.RequestHandler):
    
    def get(self):
        template=jinja_environment.get_template('test.html');
        self.response.out.write(template.render(template_values));
    def post(self):
        env = os.getenv('SERVER_SOFTWARE')
        if (env and env.startswith('Google App Engine/')):
            # Connecting from App Engine
            db = MySQLdb.connect(
            unix_socket='/cloudsql/trektip:trektipsql',
            user='root',passwd='TfReETO88zFyArUa65za');
        else:
            # Connecting from an external network.
            # Make sure your network is whitelisted
            db = MySQLdb.connect(
            host='173.194.248.180',
            port=3306,
            user='root',
            passwd='TfReETO88zFyArUa65za');
        cursor=db.cursor();
        #img=self.request.get('imgIn');
        img='';
        imgB=self.request.get('imgButton');
        if imgB=='Submit':
            img='';
            img1URL=blobstore.create_upload_url('/uploadBlob');
            #img=open('brooklynBridge0.jpg','rb');
            query='''
            update trektip.Information as info
            set info.infoType='%s',
            info.infoText='test0'
            where info.ID=1;
            
        '''
        #cursor.execute()
        global i;
        i=i+1;
        testText='Testing from post; %s'%str(i);
        template_values.update({'testText':testText,'testImg':img});
        template=jinja_environment.get_template('test.html');
        self.response.out.write(template.render(template_values));
#----------------------------------------------------------
class UserHomeHandler(webapp2.RequestHandler):
    def get(self):
        logOutB=self.request.get('logOutButton');
        
            
        getComments(self);
        template_values.update({'comments':comments});
        template=jinja_environment.get_template('userHome.html');
        self.response.out.write(template.render(template_values));
        
    def post(self):
        
        #logOutB=self.request.get('logOutButton');
        if fetchCredentialsDB(self)==True:
            loggedIn='Logged In';
            template_values.update({'firstName':firstName,'lastName':lastName,'loginForm':logOut});
            getComments(self);
            template_values.update({'comments':comments});
            template=jinja_environment.get_template('userHome.html');
            self.response.out.write(template.render(template_values));
        else:
            template_values.update({'firstName':'','lastName':'','loginForm':loginForm});
            template_values.update({'backgroundImg':defaultBackgroundImg});
            template=jinja_environment.get_template('default.html');
            self.response.out.write(template.render(template_values));
        
    
#----------------------------------------------------------       
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/default', MainHandler),
    ('/userHome', UserHomeHandler),
    ('/test',TestHandler),
    ('/login',LoginHandler)
], debug=True)
