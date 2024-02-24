import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from linkedin_api import Linkedin
from grow.credentials  import  CredentialManager
# from  grow.credentials import CredentialManager


class Linkedin_tool:
    def __init__(self): 
        self.credential_manager = CredentialManager()
        self.LINKEDIN = None
        if self.checkLogin():
            self.LINKEDIN = self.autoLogin()


    def autoLogin(self):
        self.key, self.encrypted_credentials = self.credential_manager.load_credentials()
        if self.key and self.encrypted_credentials:
            self.email, self.password = self.credential_manager.decrypt_credentials(self.key, self.encrypted_credentials)
            return  Linkedin(self.email, self.password)


    def checkLogin(self):
        return os.path.exists(self.credential_manager.filename)


    def Credentials(self, email, password):
        key = self.credential_manager.generate_key()
        encrypted_credentials = self.credential_manager.encrypt_credentials(key, email, password)
        self.credential_manager.save_credentials(key, encrypted_credentials)


    def loginLinkedin(self, email, password):    
        self.Credentials(email, password)
        self.LINKEDIN = Linkedin(email, password)
        # Set LINKEDIN attribute of the class instance
        self.__class__.LINKEDIN = self.LINKEDIN


    def logoutLinkedin(self):
        if self.checkLogin() :
          self.credential_manager.wipe_credentials()
          self.LINKEDIN = None
          self.__class__.LINKEDIN = self.LINKEDIN
          print("Successfully logged out from LinkedIn.")
        else:
          print("Already logged out from LInkedin")




#! connet database with mongobd
    #?  > every single data fecthed into database
#! proflies current comapny
    #?  >search for proflies company wise lot of 30 mail
    #?  >should be non repeating for next slot nexy day of same comapny
    #?  >for each comapny new databse will eill be there
#! Genrate emails of the profiles:
    #?  >automation for sending request for job ad insternship 
    #?  >subject and connection can be changed dynamicly
#! companys id  (Linkedin)
    #?  >keep tracking for layoff and new and job opening in that company 
    #?  >can work as wish list 
#! job (Linkedin)
    #?  >search for for specific role
    #?  >will auto apply on easy apply and and tailor the resume accordingly using LLM
    #?  >not EASY APPLY link will be saved in json file
#! resume builder
    #?  >tailor the resume according to job description 
    #?  >using latex or overleaf
#! diff job web
    #?  >make diff job json file every day from each website that i will select
    #?  >and if do the resume tailoring  

         












    


    # def find_profiles_by_company(self, company_name):
    #     if not self.logged_in:
    #         print("You need to login first.")
    #         return

    #     companys_Proflies = f"https://www.linkedin.com/search/results/people/?keywords={company_name}&origin=GLOBAL_SEARCH_HEADER"
    #     response = self.client.get(companys_Proflies)
        
    #     if response.status_code == 200:
    #         # Parse the search results page and extract relevant information
    #         soup = BeautifulSoup(response.content, "html.parser")
    #         profile_names = [name.text.strip() for name in soup.find_all(class_="entity-result__title-text")]
    #         profile_roles = [role.text.strip() for role in soup.find_all (class_="entity-result__primary-subtitle")]

    #         # Create a DataFrame
    #         df = pd.DataFrame({
    #             "Profile Name": profile_names,
    #             "Profile Role": profile_roles
    #         })

    #         print(df)
    #     else:
    #         print("Failed to fetch search results.")


            
