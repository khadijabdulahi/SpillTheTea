"""Flask app for testing."""

import unittest

from server import app
from model import connect_to_db, db, test_data

class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Set up test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///sample_data")

        db.create_all()
        test_data()
    
   
    def test_homepage(self):
        """Test homepage route."""

        response = self.client.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)
   
   
    def test_quiz(self):
        """Test quiz route."""

        response = self.client.get('/teaquiz', content_type="html/text")
        self.assertEqual(response.status_code, 200)
        
   
    def test_search(self):
        """Test search route."""

        response = self.client.get('/search', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    
    
    def test_all_teas(self):
        """Test all teas route."""

        response = self.client.get('/teas', content_type="html/text")
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
    
   
    def test_tea_title (self):
        """Test all_tea page. Makes sure name of tea is appearing."""
        
        result = self.client.get("/teas", data={"name": "chaitea"})
        self.assertIn(b"chaitea", result.data)


    def tearDown(self):
        """Do at the end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        

if __name__ == "__main__":
    unittest.main()
    
      

    