# webclient

I simulated a WebBrowser in webclient.py

## Features

* print http request headers
* print http request cookies
* print http request post data
* decode gzipped response

## usage

see test_webclient.py

result like this:

----> Http Request Prepared Cookies in cookiejar---->
    Currently have 0 cookies

----> Http Request Sended ---->

GET / HTTP/1.1
Accept-Language: zh-cn
Accept-Encoding: gzip;deflate
Connection: close
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31
Accept-Charset: GBK,utf-8;q=0.7,*;q=0.3
Host: www.google.com
    Currently have 0 cookies

<---- Http Response Recieved <----
302 *
Location: http://www.google.com.hk/url?sa=p&hl=zh-CN&pref=hkredirect&pval=yes&q=http://www.google.com.hk/&ust=1379944390649501&usg=AFQjCNHQuIwS2gTuvUgmZyHi52rNtQbhtQ
Cache-Control: private
Content-Type: text/html; charset=UTF-8
Set-Cookie: PREF=ID=d5831c207cce3f95:FF=0:NW=1:TM=1379944360:LM=1379944360:S=kmuMwILu01XohT0S; expires=Wed, 23-Sep-2015 13:52:40 GMT; path=/; domain=.google.com
Date: Mon, 23 Sep 2013 13:52:40 GMT
Server: gws
Content-Length: 376
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Alternate-Protocol: 80:quic
Connection: close

I will jumped
it jumps!---->
    http://www.google.com.hk/url?sa=p&hl=zh-CN&pref=hkredirect&pval=yes&q=http://www.google.com.hk/&ust=1379944390649501&usg=AFQjCNHQuIwS2gTuvUgmZyHi52rNtQbhtQ

----> Http Request Prepared Cookies in cookiejar---->
Set-Cookie3: PREF="ID=d5831c207cce3f95:FF=0:NW=1:TM=1379944360:LM=1379944360:S=kmuMwILu01XohT0S"; path="/"; domain=".google.com"; path_spec; domain_dot; expires="2015-09-23 13:52:40Z"; version=0
    Currently have 1 cookies

----> Http Request Sended ---->
GET /url?sa=p&hl=zh-CN&pref=hkredirect&pval=yes&q=http://www.google.com.hk/&ust=1379944390649501&usg=AFQjCNHQuIwS2gTuvUgmZyHi52rNtQbhtQ HTTP/1.1
Accept-Language: zh-cn
Accept-Encoding: gzip;deflate
Connection: close
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31
Accept-Charset: GBK,utf-8;q=0.7,*;q=0.3
Host: www.google.com.hk
    Currently have 1 cookies

<---- Http Response Recieved <----
302 *
X-Frame-Options: ALLOWALL
Location: http://www.google.com.hk/
Cache-Control: private
Content-Type: text/html; charset=UTF-8
Set-Cookie: PREF=ID=e69e773423c7f927:FF=2:LD=zh-CN:NW=1:TM=1379944360:LM=1379944360:S=lqkay7xlIc3L6mQr; expires=Wed, 23-Sep-2015 13:52:40 GMT; path=/; domain=.google.com.hk
Set-Cookie: NID=67=rp4Z4N-iTO2nNonFVZOIdobtthvfzNXNJrKXlP5vEuinctokGyePyOuSHy3l7LRTE5Ipj2iJhJq8fvCVZjzCpX_lTRZ2BE1_15eMq53jNn_jpaTEa5-lVMAL41tbx9AA; expires=Tue, 25-Mar-2014 13:52:40 GMT; path=/; domain=.google.com.hk; HttpOnly
P3P: CP="This is not a P3P policy! See http://www.google.com/support/accounts/bin/answer.py?hl=en&answer=151657 for more info."
Date: Mon, 23 Sep 2013 13:52:40 GMT
Server: gws
Content-Length: 222
X-XSS-Protection: 1; mode=block
Alternate-Protocol: 80:quic
Connection: close

I will jumped
it jumps!---->
    http://www.google.com.hk/

----> Http Request Prepared Cookies in cookiejar---->
Set-Cookie3: PREF="ID=d5831c207cce3f95:FF=0:NW=1:TM=1379944360:LM=1379944360:S=kmuMwILu01XohT0S"; path="/"; domain=".google.com"; path_spec; domain_dot; expires="2015-09-23 13:52:40Z"; version=0
Set-Cookie3: NID="67=rp4Z4N-iTO2nNonFVZOIdobtthvfzNXNJrKXlP5vEuinctokGyePyOuSHy3l7LRTE5Ipj2iJhJq8fvCVZjzCpX_lTRZ2BE1_15eMq53jNn_jpaTEa5-lVMAL41tbx9AA"; path="/"; domain=".google.com.hk"; path_spec; domain_dot; expires="2014-03-25 13:52:40Z"; HttpOnly=None; version=0
Set-Cookie3: PREF="ID=e69e773423c7f927:FF=2:LD=zh-CN:NW=1:TM=1379944360:LM=1379944360:S=lqkay7xlIc3L6mQr"; path="/"; domain=".google.com.hk"; path_spec; domain_dot; expires="2015-09-23 13:52:40Z"; version=0
    Currently have 3 cookies

----> Http Request Sended ---->
GET / HTTP/1.1
Accept-Language: zh-cn
Accept-Encoding: gzip;deflate
Connection: close
User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31
Accept-Charset: GBK,utf-8;q=0.7,*;q=0.3
Host: www.google.com.hk
Cookie: PREF=ID=e69e773423c7f927:FF=2:LD=zh-CN:NW=1:TM=1379944360:LM=1379944360:S=lqkay7xlIc3L6mQr; NID=67=rp4Z4N-iTO2nNonFVZOIdobtthvfzNXNJrKXlP5vEuinctokGyePyOuSHy3l7LRTE5Ipj2iJhJq8fvCVZjzCpX_lTRZ2BE1_15eMq53jNn_jpaTEa5-lVMAL41tbx9AA
    Currently have 3 cookies

<---- Http Response Recieved <----
200 *
Date: Mon, 23 Sep 2013 13:52:41 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=UTF-8
Set-Cookie: PREF=ID=e69e773423c7f927:U=2280b7f619a03e86:FF=2:LD=zh-CN:NW=1:TM=1379944360:LM=1379944361:S=mPXFeE4hCGHo9uF1; expires=Wed, 23-Sep-2015 13:52:41 GMT; path=/; domain=.google.com.hk
Content-Encoding: gzip
Server: gws
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Alternate-Protocol: 80:quic
Connection: close
    Currently have 3 cookies

<type 'str'>
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage"><head><meta content="/images/google_favicon_128.png" itemprop="image"><title>Google</title><script>(function(){
window.google={kE