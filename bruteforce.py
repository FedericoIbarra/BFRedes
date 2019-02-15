
import requests
import hashlib


def hashing(msg):
    result = hashlib.sha1(msg.encode())
    return result.hexdigest().upper()

def sendrequest(msg, password):
    url = "http://app-dot-crypto-challenge-spring-2019.appspot.com/bruteforce"
    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "16f8aade-7c5a-4a0b-a868-34c9d8fd50a5"
        }

    querystring = {"password":password}
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    while(response.status_code != 200):
        print(msg + str(response.status_code))
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    html_len = len(response.text)
    print(msg  + ' '+ password + ' ' + str(response.status_code) + ' '+ str(html_len))
    if html_len != 351:
        f = open("password.txt", "a+")
        f.write(response.text+"\n")
        f.write(password+"\n")
        f.write(msg+"\n")
        f.close()
        print(response.text)
        print(password)
        print(msg)
        quit()

def bruteforce(min_letter, max_letter):
    for i in range(min_letter, max_letter):
        for x in range(97, 123):
            for y in range(97, 123):
                for z in range(97, 123):
                    msg = chr(i) + chr(x) + chr(y) + chr(z)
                    sendrequest(msg, hashing(msg))


def crunch():
    f = open('words4.txt', 'r')
    for line in f:
        line = line.replace('\n', '')
        sendrequest(line, hashing(line))

if __name__ == '__main__':
    bruteforce(102, 104)
    
                
                    


                


