# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import urllib
import urllib2
import json
import time
import base64

__addon__               = xbmcaddon.Addon()
__lang__                = __addon__.getLocalizedString

import debug

def removeMovie(self, values):
    # prevent go Kodi to suspend
    if xbmc.getGlobalIdleTime() > 120:
        xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Input.ExecuteAction", "params": { "action": "noop" }, "id": 1 }')
        
    url = self.setXBMC['RootURL'] + 'sync/movies/remove'
    
    debug.debug('[REQUEST]: ' + url)
    debug.debug('[REQUEST]: ' + str(values))
    
    data = urllib.urlencode(values, True)
    data_len = len(data)
    
    debug.debug('[REQUEST DATA SIZE]: ' + str(data_len) + ' bytes')
    
    for l in range(1, 4):
        try:
            request = urllib2.Request(url, data, headers = { 'token' : self.setXBMC['Token']})
            result = urllib2.urlopen(request)
            output = result.read()
        except Exception as Error:
            conn = False
            debug.debug('Can\'t connect to: ' + url)
            debug.debug('[REQUEST ERROR]: ' + str(Error))
            if l < 3:
                debug.debug('[REQUEST]: Wait 5 secs and retring ' + str(l))
            time.sleep(15)
        else:
            conn = True
            break;
        
    if conn != True:
        debug.notify(__lang__(32100).encode('utf-8'))
        return False
        
    debug.debug('[RESPONSE]: ' + str(output))
    
    # if no values return json
    if values == '':
        try:
            output = unicode(output, 'utf-8', errors='ignore')
            output = json.loads(output)
        except Exception as Error:
            debug.debug('[GET JSON ERROR]: ' + str(Error))
            return False
    else:
        #get errors
        if len(output) > 0 and 'ERROR:' in output:
            debug.notify(__lang__(32102).encode('utf-8'))
            return False
    
    return output


def updateHashes(self, values):
    # prevent go Kodi to suspend
    if xbmc.getGlobalIdleTime() > 120:
        xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Input.ExecuteAction", "params": { "action": "noop" }, "id": 1 }')
        
    url = self.setXBMC['RootURL'] + 'settings/updatehash'
    
    debug.debug('[REQUEST]: ' + url)
    debug.debug('[REQUEST]: ' + str(values))
    
    # try send data
    data = urllib.urlencode(values, True)
    data_len = len(data)
    
    debug.debug('[REQUEST DATA SIZE]: ' + str(data_len) + ' bytes')
    
    for l in range(1, 4):
        try:
            request = urllib2.Request(url, data, headers = { 'token' : self.setXBMC['Token']})
            result = urllib2.urlopen(request)
            output = result.read()
        except Exception as Error:
            conn = False
            debug.debug('Can\'t connect to: ' + url)
            debug.debug('[REQUEST ERROR]: ' + str(Error))
            if l < 3:
                debug.debug('[REQUEST]: Wait 5 secs and retring ' + str(l))
            time.sleep(15)
        else:
            conn = True
            break;
        
    if conn != True:
        debug.notify(__lang__(32100).encode('utf-8'))
        return False
        
    debug.debug('[RESPONSE]: ' + str(output))
    
    # if no values return json
    if values == '':
        try:
            output = unicode(output, 'utf-8', errors='ignore')
            output = json.loads(output)
        except Exception as Error:
            debug.debug('[GET JSON ERROR]: ' + str(Error))
            return False
    else:
        #get errors
        if len(output) > 0 and 'ERROR:' in output:
            debug.notify(__lang__(32102).encode('utf-8'))
            return False
    
    return output


def getHashes(self):
    # prevent go Kodi to suspend
    if xbmc.getGlobalIdleTime() > 120:
        xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Input.ExecuteAction", "params": { "action": "noop" }, "id": 1 }')
        
    url = self.setXBMC['RootURL'] + 'settings/hash'
    
    debug.debug('[REQUEST]: ' + url)
    
    # try send data
    data = urllib.urlencode('', True)
    data_len = len(data)
    
    debug.debug('[REQUEST DATA SIZE]: ' + str(data_len) + ' bytes')
   
    for l in range(1, 4):
        try:
            request = urllib2.Request(url, data, headers = { 'token' : self.setXBMC['Token']})
            result = urllib2.urlopen(request)
            output = result.read()
        except Exception as Error:
            conn = False
            debug.debug('Can\'t connect to: ' + url)
            debug.debug('[REQUEST ERROR]: ' + str(Error))
            if l < 3:
                debug.debug('[REQUEST]: Wait 5 secs and retring ' + str(l))
            time.sleep(15)
        else:
            conn = True
            break;
        
    if conn != True:
        debug.notify(__lang__(32100).encode('utf-8'))
        return False
        
    debug.debug('[RESPONSE]: ' + str(output))
    
    try:
        output = unicode(output, 'utf-8', errors='ignore')
        output = json.loads(output)
    except Exception as Error:
        debug.debug('[GET JSON ERROR]: ' + str(Error))
        return False
    
    return output



def getSettings(self):

    # prevent go Kodi to suspend
    if xbmc.getGlobalIdleTime() > 120:
        xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Input.ExecuteAction", "params": { "action": "noop" }, "id": 1 }')
        
    url = self.setXBMC['RootURL'] + 'settings'
    values = ''
    
    debug.debug('[REQUEST]: ' + url)
    
    # try send data
    data = urllib.urlencode(values, True)
    data_len = len(data)
    
    debug.debug('[REQUEST DATA SIZE]: ' + str(data_len) + ' bytes')
   
    for l in range(1, 4):
        try:
            request = urllib2.Request(url, data, headers = { 'token' : self.setXBMC['Token']})
            result = urllib2.urlopen(request)
            output = result.read()
        except Exception as Error:
            conn = False
            debug.debug('Can\'t connect to: ' + url)
            debug.debug('[REQUEST ERROR]: ' + str(Error))
            if l < 3:
                debug.debug('[REQUEST]: Wait 5 secs and retring ' + str(l))
            time.sleep(15)
        else:
            conn = True
            break;
        
    if conn != True:
        debug.notify(__lang__(32100).encode('utf-8'))
        return False
        
    debug.debug('[RESPONSE]: ' + str(output))
    
    # if no values return json
    if values == '':
        try:
            output = unicode(output, 'utf-8', errors='ignore')
            output = json.loads(output)
        except Exception as Error:
            debug.debug('[GET JSON ERROR]: ' + str(Error))
            return False
    else:
        #get errors
        if len(output) > 0 and 'ERROR:' in output:
            debug.notify(__lang__(32102).encode('utf-8'))
            return False
    
    return output


def postAddVideo(self, values=''):

  # prevent go Kodi to suspend
    if xbmc.getGlobalIdleTime() > 120:
        xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Input.ExecuteAction", "params": { "action": "noop" }, "id": 1 }')
        
    url = self.setXBMC['RootURL'] + 'sync/movies'
        
    debug.debug('[REQUEST]: ' + url)
    debug.debug('[REQUEST]: ' + str(values))
    
    # try send data
    data = urllib.urlencode(values, True)
    data_len = len(data)
    
    debug.debug('[REQUEST DATA SIZE]: ' + str(data_len) + ' bytes')
  
    for l in range(1, 4):
        try:
            request = urllib2.Request(url, data, headers = { 'token' : self.setXBMC['Token']})
            result = urllib2.urlopen(request)
            output = result.read()
        except Exception as Error:
            conn = False
            debug.debug('Can\'t connect to: ' + url)
            debug.debug('[REQUEST ERROR]: ' + str(Error))
            if l < 3:
                debug.debug('[REQUEST]: Wait 5 secs and retring ' + str(l))
            time.sleep(15)
        else:
            conn = True
            break;
        
    if conn != True:
        debug.notify(__lang__(32100).encode('utf-8'))
        return False
        
    debug.debug('[RESPONSE]: ' + str(output))
    
    # if no values return json
    if values == '':
        try:
            output = unicode(output, 'utf-8', errors='ignore')
            output = json.loads(output)
        except Exception as Error:
            debug.debug('[GET JSON ERROR]: ' + str(Error))
            return False
    else:
        #get errors
        if len(output) > 0 and 'ERROR:' in output:
            debug.notify(__lang__(32102).encode('utf-8'))
            return False
    
    return output


def getMovieHashList(self):
    
    # prevent go Kodi to suspend
    if xbmc.getGlobalIdleTime() > 120:
        xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Input.ExecuteAction", "params": { "action": "noop" }, "id": 1 }')
        
    url = self.setXBMC['RootURL'] + 'sync/movies/hashes'
    values = ''
    
    debug.debug('[REQUEST]: ' + url)
    debug.debug('[REQUEST]: ' + str(values))
    
    # try send data
    data = urllib.urlencode(values, True)
    data_len = len(data)
    
    debug.debug('[REQUEST DATA SIZE]: ' + str(data_len) + ' bytes')
    
    if data_len > self.setSITE['POST_MAX_SIZE_B']:
        debug.notify(__lang__(32116).encode('utf-8'))
        debug.debug('[REQUEST ERROR]: Data too large to send, server can takes only ' + str(self.setSITE['POST_MAX_SIZE_B']) + ' bytes')
        return False

    for l in range(1, 4):
        try:
            request = urllib2.Request(url, data, headers = { 'token' : self.setXBMC['Token']})
            result = urllib2.urlopen(request)
            output = result.read()
        except Exception as Error:
            conn = False
            debug.debug('Can\'t connect to: ' + url)
            debug.debug('[REQUEST ERROR]: ' + str(Error))
            if l < 3:
                debug.debug('[REQUEST]: Wait 5 secs and retring ' + str(l))
            time.sleep(15)
        else:
            conn = True
            break;
        
    if conn != True:
        debug.notify(__lang__(32100).encode('utf-8'))
        return False
        
    debug.debug('[RESPONSE]: ' + str(output))
    
    # if no values return json
    if values == '':
        try:
            output = unicode(output, 'utf-8', errors='ignore')
            output = json.loads(output)
        except Exception as Error:
            debug.debug('[GET JSON ERROR]: ' + str(Error))
            return False
    else:
        #get errors
        if len(output) > 0 and 'ERROR:' in output:
            debug.notify(__lang__(32102).encode('utf-8'))
            return False
    
    return output
        