#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User-signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">User-Signup</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

header = "<h3>User Signup</h3>"

        # a form for entering signup information
        # fields must include: Username, Password, Verify Password, and E-mail
form = """
        <form method="post">
            <label>
                Username: 
                <input type="text" name="username" value = %(username)s />
            </label> <br>
            <label>
                Password:
                <input type="text" name="password" value =  ""/>
            </label><br>
            <label>
                Verify Password:
                <input type="text" name="verify_password" value = ""/>
            </label><br>
            <label>
                E-mail:
                <input type="text" name="e_mail" value = %(e_mail)s />
            </label>
            <br>
            <input type="submit" value="Sign Up!"/>
            <div style = "color : red">%(error)s</div>
        </form>
        """

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.write_form()

    def write_form(self, error = "", username="",e_mail=""):
        self.response.out.write(header + form % {"error": error, "username": username, "e_mail" : e_mail})

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify_password = self.request.get("verify_password")
        e_mail = self.request.get("e_mail")

        if password == "" or e_mail == "" or username == "":
            self.write_form("Please enter your information into the fields provided.", username, e_mail)
        elif password != verify_password:
            self.write_form("Please verify your password.", username, e_mail)
        elif "@" and "." not in e_mail:
            self.write_form("Please enter a valid e-mail.", username, e_mail)
        else:
            self.redirect('/add')

class AddUser(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
    """
    def get(self):
    # if we didn't redirect by now, then all is well
        confirmation = "Thank you for signing up!"
        content = page_header + "<p>" + confirmation + "</p>"
        self.response.out.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddUser)
], debug=True)
