#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Encore Hu, <huyoo353@126.com>'
''' for update, goto https://github.com/encorehu/webclient '''

import sys
import os

import httplib, urllib2, urllib, socket
import cookielib
import StringIO
import gzip

import logging

logger = logging.getLogger("webclient")
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

fmt = logging.Formatter('%(message)s')
sh.setFormatter(fmt)

logger.addHandler(sh)
'''
http code
1xx - informational
2xx - success
3xx - redirection
4xx - client error
5xx - server error
'''
class MyHTTPConnection(httplib.HTTPConnection):
    def send(self, s):
        logger.debug('\n----> Http Request Sended ---->')
        logger.debug( s )  # or save them, or whatever!
        httplib.HTTPConnection.send(self, s)

class MyHTTPSConnection(httplib.HTTPSConnection):
    def send(self, s):
        logger.debug( '+'*80 )
        logger.debug( s )  # or save them, or whatever!
        httplib.HTTPSConnection.send(self, s)

class MyHTTPHandler(urllib2.HTTPHandler):
    def http_open(self, req):
        logger.debug(req)
        return self.do_open(MyHTTPConnection, req)

    def https_open(self, req):
        logger.debug(req)
        return self.do_open(MyHTTPSConnection, req)

class MyHTTPErrorProcessor(urllib2.HTTPErrorProcessor):

    def http_response(self, request, response):
        code, msg, hdrs = response.code, response.msg, response.info()
        logger.debug( '\n<---- Http Response Recieved <----' )
        logger.debug( str(code)+' *' )
        logger.debug( hdrs )

        return urllib2.HTTPErrorProcessor.http_response(self, request, response)

    https_response = http_response

class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):

    def redirect_request(self, req, fp, code, msg, hdrs,newurl):
        if req.get_method()=='HEAD':
            logger.info( 'it jumps!---->\n    %s' % newurl )
            newreq=urllib2.HTTPRedirectHandler.redirect_request(self, req, fp, code, msg, hdrs, newurl)
            newreq.get_method = lambda : 'HEAD'
            return newreq
        else:
        logger.info( 'it jumps!---->\n    %s' % newurl )
        return urllib2.HTTPRedirectHandler.redirect_request(self, req, fp, code, msg, hdrs,newurl)

    def http_error_302(self, req, fp, code, msg, headers):
        logger.debug( 'I will jumped')
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)

    http_error_301 = http_error_303 = http_error_307 = http_error_302

class MyHTTPCookieProcessor(urllib2.HTTPCookieProcessor):

    def http_request(self, request):
        logger.debug( '\n----> Http Request Cookies Prepared in cookiejar---->' )
        logger.debug( self.cookiejar.as_lwp_str() )
        logger.debug( "    Currently have %d cookies\n" % len(self.cookiejar) )
        #cannot use super, HTTPCookieProcessor isnot new style class
        #return super(MyHTTPCookieProcessor, self).http_request(request)
        return urllib2.HTTPCookieProcessor.http_request(self, request)

    def http_response(self, request, response):
        logger.debug( "    Currently have %d cookies\n" % len(self.cookiejar) )
        return urllib2.HTTPCookieProcessor.http_response(self, request, response)

class HttpResponse(object):
    status_code = 0
    headers     = {}
    encoding    = ''
    content     = None

    def __init__(self, *args, **kwargs):
        pass

    def json(self):
        return None

class HeadRequest(urllib2.Request):
    def get_method(self):
        return "HEAD"


class WebBrowser(object):

    _headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31",
                "Accept-Charset":'GBK,utf-8;q=0.7,*;q=0.3',
                "Accept-Language":"zh-cn",
                "Accept-Encoding":"gzip,deflate",
                "Connection":"keep-alive"
    }

    _data = None

    _referer = None

    _cookies = {}

    COOKIEFILE='./cookie.lwp'

    opener = None

    def __init__(self, cookiejar = None, proxy = None):

        if cookiejar is None:
            cookiejar = cookielib.LWPCookieJar()
        self.cookiejar = cookiejar
        if os.path.isfile(self.COOKIEFILE):
            # if we have a cookie file already saved
            # then load the cookies into the Cookie Jar
            self.cookiejar.load(self.COOKIEFILE)
        else:
            print 'the cookie file(%s) is missing' % self.COOKIEFILE

        if proxy:
            if proxy.startswith('http://'):
                proxyserver = proxy
            else:
                proxyserver = 'http://%s' % proxy
            self.opener = urllib2.build_opener(urllib2.ProxyHandler({'http':proxyserver,'https':proxyserver}), MyHTTPHandler, MyHTTPRedirectHandler, MyHTTPErrorProcessor, MyHTTPCookieProcessor(self.cookiejar))
        else:
        self.opener = urllib2.build_opener(MyHTTPHandler, MyHTTPRedirectHandler, MyHTTPErrorProcessor, MyHTTPCookieProcessor(self.cookiejar))

    def _add_cookie(self, key, value):
        self._cookies.update({key:value})
        cookie_string = ';'.join(map(lambda x:'%s=%s'%(x[0],x[1]),self._cookies.items()))
        self.opener.addheaders.append(('Cookie', cookie_string))

    def _request(self, url, data=None, headers=None, cookies=None, referer=None, ajax = False, method = 'GET'):
        if headers:
            self._headers.update(headers)

        if referer:
            self._headers.update({'Referer': referer})

        if data:
            if isinstance(data,dict):
                try:
                    data = urllib.urlencode(data)
                except:
                    data = None
                    logger.error('your POST DATA has unicode, you MUST encode to utf-8')

            if isinstance(data,str):
                logger.debug( '\n----> Http Request Prepared Data ---->' )
                logger.debug( 'data: '+data )

        method = method.upper()
        if method == 'HEAD':
            req = HeadRequest(url=url, data=data, headers = self._headers )
        else:
            req = urllib2.Request(url=url, data=data, headers = self._headers )

        if cookies:
            if type(cookies) == str:
                if not req.has_header("Cookie"):
                    # this can avoid cookiejar set request\' s Cookie header.
                    # because this operation is ahead the cookiejar to do the samething
                    # but, attention: the cookies donot saved into cookiejar now.
                    req.add_unredirected_header("Cookie", cookies)
                #else:
                #    print 'req has header:cookie'
            else:
                # cookies should be string, like 'A=balabala;b=bala;...'
                logger.warning('cookies only support string, which comes from your WebBrowser request header')

        ###logger.debug(str(req.header_items()))

        if ajax:
            if not req.has_header('x-requested-with'):
                req.add_unredirected_header('x-requested-with', 'XMLHttpRequest')

        try:
            response = self.opener.open(req)
        except urllib2.HTTPError,e:
            content = 'ERROR %s' % e
        except urllib2.URLError, e:
            content = 'ERROR %s' % e
        except socket.timeout, e:
            content = 'ERROR %s' % e
        else:
            if os.path.isfile(self.COOKIEFILE):
                self.cookiejar.save(self.COOKIEFILE)
            else:
                try:
                    self.cookiejar.save(self.COOKIEFILE)
                except:
                    pass

            if response.info().get('Content-Encoding') == 'gzip':
                #content = gzip.decompress(response.read())

                compressed_data = response.read()
                ###compressed_stream = StringIO.StringIO()
                ###compressed_stream.write(response.read())
                ###compressed_stream.seek(0)
                compressed_stream = StringIO.StringIO(compressed_data)
                gzipper = gzip.GzipFile(fileobj=compressed_stream)
                content = gzipper.read()
            else:
                content = response.read()

            #logger.debug( self.cookiejar )
            logger.debug( "    Currently have %d cookies\n" % len(self.cookiejar) )

            headers = response.info()

            response.close()
        return content #, headers

    def get(self, url, *args, **kwargs):
        return self._request(url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        kwargs.update({'method':'POST'})
        return self._request(url, *args, **kwargs)

    def head(self, url, *args, **kwargs):
        kwargs.update({'method':'HEAD'})
        return self._request(url, *args, **kwargs)

    def exists(self, url, *args, **kwargs):
        kwargs.update({'method':'HEAD'})
        return self._request(url, *args, **kwargs)
