__Made__By__ = 'Zhir'

import requests, sys, time
from bs4 import BeautifulSoup

def banner():
    print("""{}

   *     (                                                      
 (  `    )\ )  (  (       (                       )             
 )\))(  (()/(  )\))(      )\   (       )       ( /(    (   (    
((_)()\  /(_))((_)()\   (((_)  )(   ( /(   (   )\())  ))\  )(   
(_()((_)(_))_  (()((_)  )\___ (()\  )(_))  )\ ((_)\  /((_)(()\  
|  \/  | |   \  | __|  ((/ __| ((_)((_)_  ((_)| |(_)(_))   ((_) 
| |\/| | | |) | |__ \   | (__ | '_|/ _` |/ _| | / / / -_) | '_| 
|_|  |_| |___/  |___/    \___||_|  \__,_|\__| |_\_\ \___| |_|   
                                                                

{}\n\tUsage:\n\tpython md5.py [HASH]\n{}""".format("="*75,"="*75,"="*75))


def gromweb(password):
    try:
        req = requests.get(url="https://md5.gromweb.com",params={"md5":password})
        source_code = req.content
        soup = BeautifulSoup(source_code,"html.parser")
        brute_text = soup.find_all("em",{"class":"long-content string"})
        plain_text = brute_text[0].text
        print("md5.gromweb.com ===> {}\n{}".format(plain_text,"="*75))
    except IndexError:
        print("md5.gromweb.com ===> Hash Don't Found!\n{}".format("=" * 75))
    except requests.ConnectionError or requests.ConnectTimeout:
        print("md5.gromweb.com ===> Connection Error!!!\n{}".format("=" * 75))

def my_addr(password):
    try:
        req = requests.post(url="http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php",data={"md5":password,"x":"21","y":"12"})
        source_code = req.content
        soup = BeautifulSoup(source_code,"html.parser")
        brute_text = soup.find_all("div",{"class":"white_bg_title"})
        plain_text = brute_text[1].text.split()[2]
        print("md5.my-addr.com ===> {}\n{}".format(plain_text,"="*75))
    except IndexError:
        print("md5.my-addr.com ===> Hash Don't Found!\n{}".format("="*75))
    except requests.ConnectionError or requests.ConnectTimeout:
        print("md5.my-addr.com ===> Connection Error!!!\n{}".format("=" * 75))

if __name__ == '__main__':
    try:
        start_time = time.time()
        hash_text = sys.argv[1].lower()
        banner()
        gromweb(hash_text)
        my_addr(hash_text)
    except IndexError:
        print("Please, Entry A Hash Text!")
    except:
        print("Error!")