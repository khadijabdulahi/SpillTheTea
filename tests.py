"""Flask app for testing."""

import unittest

from server import app
from model import connect_to_db, db, test_data

class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Set up test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///sample_data")

        # Create tables and add sample data
        db.create_all()
        test_data()
    
   
    def test_homepage(self):
        """Test homepage route."""


        response = self.client.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)
   
   
    def test_user_registration(self):
        """Test user registration"""
    
        response = self.client.post("/register",
                            data={"email":"test@test1.com", 
                            "password":"test1",
                            "firstname":"testuser"},
                            follow_redirects=True) 
        self.assertIn(b"Account created!", response.data)  
        
        
   
   
    def test_registration_existing_email(self):
        """Test user attempting to create an account with an existing email."""

        response = self.client.post("/register",
                                data={"email":"user@test.com",
                                "password":"existingemail"},
                                follow_redirects=True)
        self.assertIn(b"Cannot create an account with that email.", response.data)
        
        
        
    def test_login(self):
        """Test login page."""

        result = self.client.post("/login",
                                  data={"email": "user@test.com",
                                        "password": "testing"},
                                  follow_redirects=True)
        self.assertIn(b"Get Inspired!", result.data)
        
    
    
    def test_quiz(self):
        """Test quiz route."""


        response = self.client.get('/teaquiz', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        

    def tearDown(self):
        """Do at the end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        


if __name__ == "__main__":
    unittest.main()
    
      

    