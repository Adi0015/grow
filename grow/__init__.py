import  argparse
import  json
from  termcolor import  colored
from  getpass import  getpass
from  grow.scraper import  Linkedin_tool
from  cryptography.fernet import  Fernet
import  pkg_resources

def get_version():
    try:
        version = pkg_resources.get_distribution("grow").version
    except pkg_resources.DistributionNotFound:
        version = "Unknown"
    return version


def banner():
    version = get_version()
    print(f'''

 ██████╗ ██████╗  ██████╗ ██╗    ██╗
██╔════╝ ██╔══██╗██╔═══██╗██║    ██║
██║  ███╗██████╔╝██║   ██║██║ █╗ ██║
██║   ██║██╔══██╗██║   ██║██║███╗██║
╚██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝     
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝    {colored('v'+version, 'cyan')}
      ''')    


def main():
    parser = argparse.ArgumentParser(description='Grow In Your Life')
    parser.add_argument('--login', action='store_true', help='Login to LinkedIn')
    parser.add_argument('--logout', action='store_true', help='Logout from LinkedIn')
    parser.add_argument('--profiles', metavar='COMPANY_NAME', help='Search for profiles associated with a company')
    args = parser.parse_args()

    linkedin_tool = Linkedin_tool()

    if args.login:
        if linkedin_tool.checkLogin()  :
          print("Already you are logged in to Linkedin")
          # print(type(linkedin_tool.LINKEDIN))
        else:  
          email = input("Enter your LinkedIn email: ")
          password = input("Enter your LinkedIn password: ")
          linkedin_tool.loginLinkedin(email, password)
          

    elif args.logout:
        linkedin_tool.logoutLinkedin()
        # print(type(linkedin_tool.__class__.LINKEDIN))

    elif args.profiles:
        linkedin_tool.find_profiles_by_company(args.profiles)
    else:
        banner()
        # parser.print_help()

if __name__ == "__main__":
    main()





