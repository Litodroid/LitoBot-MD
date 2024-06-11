#!/usr/bin/env python
import csv #line:18
import datetime #line:19
import errno #line:20
import math #line:21
import os #line:22
import platform #line:23
import re #line:24
import signal #line:25
import socket #line:26
import sys #line:27
import threading #line:28
import timeit #line:29
import xml .parsers .expat #line:30
try :#line:32
    import gzip #line:33
    GZIP_BASE =gzip .GzipFile #line:34
except ImportError :#line:35
    gzip =None #line:36
    GZIP_BASE =object #line:37
__version__ ='2.1.4b1'#line:39
class FakeShutdownEvent (object ):#line:42
    ""#line:45
    @staticmethod #line:47
    def isSet ():#line:48
        "Dummy method to always return false" ""#line:49
        return False #line:50
    is_set =isSet #line:52
DEBUG =False #line:56
_OO000OO0O0000O0OO =object ()#line:57
PY25PLUS =sys .version_info [:2 ]>=(2 ,5 )#line:58
PY26PLUS =sys .version_info [:2 ]>=(2 ,6 )#line:59
PY32PLUS =sys .version_info [:2 ]>=(3 ,2 )#line:60
PY310PLUS =sys .version_info [:2 ]>=(3 ,10 )#line:61
try :#line:64
    import json #line:65
except ImportError :#line:66
    try :#line:67
        import simplejson as json #line:68
    except ImportError :#line:69
        json =None #line:70
try :#line:72
    import xml .etree .ElementTree as ET #line:73
    try :#line:74
        from xml .etree .ElementTree import _Element as ET_Element #line:75
    except ImportError :#line:76
        pass #line:77
except ImportError :#line:78
    from xml .dom import minidom as DOM #line:79
    from xml .parsers .expat import ExpatError #line:80
    ET =None #line:81
try :#line:83
    from urllib2 import (urlopen ,Request ,HTTPError ,URLError ,AbstractHTTPHandler ,ProxyHandler ,HTTPDefaultErrorHandler ,HTTPRedirectHandler ,HTTPErrorProcessor ,OpenerDirector )#line:87
except ImportError :#line:88
    from urllib .request import (urlopen ,Request ,HTTPError ,URLError ,AbstractHTTPHandler ,ProxyHandler ,HTTPDefaultErrorHandler ,HTTPRedirectHandler ,HTTPErrorProcessor ,OpenerDirector )#line:92
try :#line:94
    from httplib import HTTPConnection ,BadStatusLine #line:95
except ImportError :#line:96
    from http .client import HTTPConnection ,BadStatusLine #line:97
try :#line:99
    from httplib import HTTPSConnection #line:100
except ImportError :#line:101
    try :#line:102
        from http .client import HTTPSConnection #line:103
    except ImportError :#line:104
        HTTPSConnection =None #line:105
try :#line:107
    from httplib import FakeSocket #line:108
except ImportError :#line:109
    FakeSocket =None #line:110
try :#line:112
    from Queue import Queue #line:113
except ImportError :#line:114
    from queue import Queue #line:115
try :#line:117
    from urlparse import urlparse #line:118
except ImportError :#line:119
    from urllib .parse import urlparse #line:120
try :#line:122
    from urlparse import parse_qs #line:123
except ImportError :#line:124
    try :#line:125
        from urllib .parse import parse_qs #line:126
    except ImportError :#line:127
        from cgi import parse_qs #line:128
try :#line:130
    from hashlib import md5 #line:131
except ImportError :#line:132
    from md5 import md5 #line:133
try :#line:135
    from argparse import ArgumentParser as ArgParser #line:136
    from argparse import SUPPRESS as ARG_SUPPRESS #line:137
    PARSER_TYPE_INT =int #line:138
    PARSER_TYPE_STR =str #line:139
    PARSER_TYPE_FLOAT =float #line:140
except ImportError :#line:141
    from optparse import OptionParser as ArgParser #line:142
    from optparse import SUPPRESS_HELP as ARG_SUPPRESS #line:143
    PARSER_TYPE_INT ='int'#line:144
    PARSER_TYPE_STR ='string'#line:145
    PARSER_TYPE_FLOAT ='float'#line:146
try :#line:148
    from cStringIO import StringIO #line:149
    BytesIO =None #line:150
except ImportError :#line:151
    try :#line:152
        from StringIO import StringIO #line:153
        BytesIO =None #line:154
    except ImportError :#line:155
        from io import StringIO ,BytesIO #line:156
try :#line:158
    import __builtin__ #line:159
except ImportError :#line:160
    import builtins #line:161
    from io import TextIOWrapper ,FileIO #line:162
    class _O00OO0O000OOOO0OO (TextIOWrapper ):#line:164
        ""#line:167
        def __init__ (O00000OO0O000OOO0 ,O00OO0OOOOO0OOOO0 ,**O000OOOO0OO00O00O ):#line:168
            O00OO00OO0O0000OO =FileIO (O00OO0OOOOO0OOOO0 .fileno (),'w')#line:169
            super (_O00OO0O000OOOO0OO ,O00000OO0O000OOO0 ).__init__ (O00OO00OO0O0000OO ,encoding ='utf8',errors ='strict')#line:174
        def write (O0O0OOO00OO0000OO ,OOO00O00OOOOOOO00 ):#line:176
            super (_O00OO0O000OOOO0OO ,O0O0OOO00OO0000OO ).write (OOO00O00OOOOOOO00 )#line:177
            O0O0OOO00OO0000OO .flush ()#line:178
    _O00O0OOOO00OOOO00 =getattr (builtins ,'print')#line:180
    try :#line:181
        _O0O00O0OOOOO0O00O =_O00OO0O000OOOO0OO (sys .stdout )#line:182
        _O0O000OOOOOOO00O0 =_O00OO0O000OOOO0OO (sys .stderr )#line:183
    except OSError :#line:184
        _O0O00O0OOOOO0O00O =sys .stdout #line:187
        _O0O000OOOOOOO00O0 =sys .stderr #line:188
    def to_utf8 (O0OO0O0O0OOOO00O0 ):#line:190
        ""#line:191
        return O0OO0O0O0OOOO00O0 #line:192
    def print_ (*O00OO0O0O00O000OO ,**O0O0O00OO0O00O00O ):#line:194
        ""#line:195
        if O0O0O00OO0O00O00O .get ('file')==sys .stderr :#line:196
            O0O0O00OO0O00O00O ['file']=_O0O000OOOOOOO00O0 #line:197
        else :#line:198
            O0O0O00OO0O00O00O ['file']=O0O0O00OO0O00O00O .get ('file',_O0O00O0OOOOO0O00O )#line:199
        _O00O0OOOO00OOOO00 (*O00OO0O0O00O000OO ,**O0O0O00OO0O00O00O )#line:200
else :#line:201
    del __builtin__ #line:202
    def to_utf8 (O00OO00O000OOOO00 ):#line:204
        ""#line:205
        try :#line:206
            return O00OO00O000OOOO00 .encode ('utf8','strict')#line:207
        except AttributeError :#line:208
            return O00OO00O000OOOO00 #line:209
    def print_ (*OO0O00OO0OOOOOO0O ,**O0000OOOOO0OOOO0O ):#line:211
        ""#line:217
        OO0O00O00O00O00OO =O0000OOOOO0OOOO0O .pop ("file",sys .stdout )#line:218
        if OO0O00O00O00O00OO is None :#line:219
            return #line:220
        def O00OOOOOO0O0000OO (O00OO000O0O0O00OO ):#line:222
            if not isinstance (O00OO000O0O0O00OO ,basestring ):#line:223
                O00OO000O0O0O00OO =str (O00OO000O0O0O00OO )#line:224
            OO000O0000O0O000O ='utf8'#line:226
            if (isinstance (OO0O00O00O00O00OO ,file )and isinstance (O00OO000O0O0O00OO ,unicode )and OO000O0000O0O000O is not None ):#line:229
                OO00000O0000O0000 =getattr (OO0O00O00O00O00OO ,"errors",None )#line:230
                if OO00000O0000O0000 is None :#line:231
                    OO00000O0000O0000 ="strict"#line:232
                O00OO000O0O0O00OO =O00OO000O0O0O00OO .encode (OO000O0000O0O000O ,OO00000O0000O0000 )#line:233
            OO0O00O00O00O00OO .write (O00OO000O0O0O00OO )#line:234
            OO0O00O00O00O00OO .flush ()#line:235
        O0OOOOOOOO00OOO0O =False #line:236
        OO00O0000000OOO0O =O0000OOOOO0OOOO0O .pop ("sep",None )#line:237
        if OO00O0000000OOO0O is not None :#line:238
            if isinstance (OO00O0000000OOO0O ,unicode ):#line:239
                O0OOOOOOOO00OOO0O =True #line:240
            elif not isinstance (OO00O0000000OOO0O ,str ):#line:241
                raise TypeError ("sep must be None or a string")#line:242
        OOOO0OOOO00O0O00O =O0000OOOOO0OOOO0O .pop ("end",None )#line:243
        if OOOO0OOOO00O0O00O is not None :#line:244
            if isinstance (OOOO0OOOO00O0O00O ,unicode ):#line:245
                O0OOOOOOOO00OOO0O =True #line:246
            elif not isinstance (OOOO0OOOO00O0O00O ,str ):#line:247
                raise TypeError ("end must be None or a string")#line:248
        if O0000OOOOO0OOOO0O :#line:249
            raise TypeError ("invalid keyword arguments to print()")#line:250
        if not O0OOOOOOOO00OOO0O :#line:251
            for O0OO0O000OOOO000O in OO0O00OO0OOOOOO0O :#line:252
                if isinstance (O0OO0O000OOOO000O ,unicode ):#line:253
                    O0OOOOOOOO00OOO0O =True #line:254
                    break #line:255
        if O0OOOOOOOO00OOO0O :#line:256
            O000OOOO00OOO0000 =unicode ("\n")#line:257
            O0OO0O0OOO00000O0 =unicode (" ")#line:258
        else :#line:259
            O000OOOO00OOO0000 ="\n"#line:260
            O0OO0O0OOO00000O0 =" "#line:261
        if OO00O0000000OOO0O is None :#line:262
            OO00O0000000OOO0O =O0OO0O0OOO00000O0 #line:263
        if OOOO0OOOO00O0O00O is None :#line:264
            OOOO0OOOO00O0O00O =O000OOOO00OOO0000 #line:265
        for O0OO0O00000O000OO ,O0OO0O000OOOO000O in enumerate (OO0O00OO0OOOOOO0O ):#line:266
            if O0OO0O00000O000OO :#line:267
                O00OOOOOO0O0000OO (OO00O0000000OOO0O )#line:268
            O00OOOOOO0O0000OO (O0OO0O000OOOO000O )#line:269
        O00OOOOOO0O0000OO (OOOO0OOOO00O0O00O )#line:270
try :#line:273
    import ssl #line:274
    try :#line:275
        CERT_ERROR =(ssl .CertificateError ,)#line:276
    except AttributeError :#line:277
        CERT_ERROR =tuple ()#line:278
    HTTP_ERRORS =((HTTPError ,URLError ,socket .error ,ssl .SSLError ,BadStatusLine )+CERT_ERROR )#line:283
except ImportError :#line:284
    ssl =None #line:285
    HTTP_ERRORS =(HTTPError ,URLError ,socket .error ,BadStatusLine )#line:286
if PY32PLUS :#line:288
    etree_iter =ET .Element .iter #line:289
elif PY25PLUS :#line:290
    etree_iter =ET_Element .getiterator #line:291
if PY26PLUS :#line:293
    thread_is_alive =threading .Thread .is_alive #line:294
else :#line:295
    thread_is_alive =threading .Thread .isAlive #line:296
def event_is_set (OOO00OO00O0O0O000 ):#line:299
    try :#line:300
        return OOO00OO00O0O0O000 .is_set ()#line:301
    except AttributeError :#line:302
        return OOO00OO00O0O0O000 .isSet ()#line:303
class SpeedtestException (Exception ):#line:306
    ""#line:307
class SpeedtestCLIError (SpeedtestException ):#line:310
    ""#line:311
class SpeedtestHTTPError (SpeedtestException ):#line:314
    ""#line:315
class SpeedtestConfigError (SpeedtestException ):#line:318
    ""#line:319
class SpeedtestServersError (SpeedtestException ):#line:322
    ""#line:323
class ConfigRetrievalError (SpeedtestHTTPError ):#line:326
    ""#line:327
class ServersRetrievalError (SpeedtestHTTPError ):#line:330
    ""#line:331
class InvalidServerIDType (SpeedtestException ):#line:334
    ""#line:335
class NoMatchedServers (SpeedtestException ):#line:338
    ""#line:339
class SpeedtestMiniConnectFailure (SpeedtestException ):#line:342
    ""#line:343
class InvalidSpeedtestMiniServer (SpeedtestException ):#line:346
    ""#line:349
class ShareResultsConnectFailure (SpeedtestException ):#line:352
    ""#line:353
class ShareResultsSubmitFailure (SpeedtestException ):#line:356
    ""#line:359
class SpeedtestUploadTimeout (SpeedtestException ):#line:362
    ""#line:365
class SpeedtestBestServerFailure (SpeedtestException ):#line:368
    ""#line:369
class SpeedtestMissingBestServer (SpeedtestException ):#line:372
    ""#line:373
def create_connection (O0O00OO0000O0OOO0 ,timeout =_OO000OO0O0000O0OO ,source_address =None ):#line:377
    ""#line:390
    O00000OO00OOO00O0 ,OO00OOOOO00O0O00O =O0O00OO0000O0OOO0 #line:392
    O0O0O000OOOO000OO =None #line:393
    for O0OO0OO0O0OO0OOO0 in socket .getaddrinfo (O00000OO00OOO00O0 ,OO00OOOOO00O0O00O ,0 ,socket .SOCK_STREAM ):#line:394
        OO00O0OOOO00OO000 ,OO0O00O000OOOO0OO ,OO0OOO0OO000O0O00 ,OO0OOO00OO0OOO000 ,OO00OO0O0OOOO0O00 =O0OO0OO0O0OO0OOO0 #line:395
        OO00OOOOOOO000000 =None #line:396
        try :#line:397
            OO00OOOOOOO000000 =socket .socket (OO00O0OOOO00OO000 ,OO0O00O000OOOO0OO ,OO0OOO0OO000O0O00 )#line:398
            if timeout is not _OO000OO0O0000O0OO :#line:399
                OO00OOOOOOO000000 .settimeout (float (timeout ))#line:400
            if source_address :#line:401
                OO00OOOOOOO000000 .bind (source_address )#line:402
            OO00OOOOOOO000000 .connect (OO00OO0O0OOOO0O00 )#line:403
            return OO00OOOOOOO000000 #line:404
        except socket .error :#line:406
            O0O0O000OOOO000OO =get_exception ()#line:407
            if OO00OOOOOOO000000 is not None :#line:408
                OO00OOOOOOO000000 .close ()#line:409
    if O0O0O000OOOO000OO is not None :#line:411
        raise O0O0O000OOOO000OO #line:412
    else :#line:413
        raise socket .error ("getaddrinfo returns an empty list")#line:414
class SpeedtestHTTPConnection (HTTPConnection ):#line:417
    ""#line:420
    def __init__ (OO0000OO00OO0OOO0 ,*OO0OO0000O0O0000O ,**O00OO00O0O0OOOOO0 ):#line:421
        OO00O00OO00O0OOOO =O00OO00O0O0OOOOO0 .pop ('source_address',None )#line:422
        OO000O00OO0OOO0OO =O00OO00O0O0OOOOO0 .pop ('timeout',10 )#line:423
        OO0000OO00OO0OOO0 ._tunnel_host =None #line:425
        HTTPConnection .__init__ (OO0000OO00OO0OOO0 ,*OO0OO0000O0O0000O ,**O00OO00O0O0OOOOO0 )#line:427
        OO0000OO00OO0OOO0 .source_address =OO00O00OO00O0OOOO #line:429
        OO0000OO00OO0OOO0 .timeout =OO000O00OO0OOO0OO #line:430
    def connect (OOO0OOOO00OOOOO00 ):#line:432
        ""#line:433
        try :#line:434
            OOO0OOOO00OOOOO00 .sock =socket .create_connection ((OOO0OOOO00OOOOO00 .host ,OOO0OOOO00OOOOO00 .port ),OOO0OOOO00OOOOO00 .timeout ,OOO0OOOO00OOOOO00 .source_address )#line:439
        except (AttributeError ,TypeError ):#line:440
            OOO0OOOO00OOOOO00 .sock =create_connection ((OOO0OOOO00OOOOO00 .host ,OOO0OOOO00OOOOO00 .port ),OOO0OOOO00OOOOO00 .timeout ,OOO0OOOO00OOOOO00 .source_address )#line:445
        if OOO0OOOO00OOOOO00 ._tunnel_host :#line:447
            OOO0OOOO00OOOOO00 ._tunnel ()#line:448
if HTTPSConnection :#line:451
    class SpeedtestHTTPSConnection (HTTPSConnection ):#line:452
        ""#line:455
        default_port =443 #line:456
        def __init__ (O0OO0OOO0O0000OOO ,*OOOO0000OOOOO0O0O ,**OO0O0O000OOOO0OOO ):#line:458
            O0000000OO0OO0000 =OO0O0O000OOOO0OOO .pop ('source_address',None )#line:459
            O0O00OO000O00000O =OO0O0O000OOOO0OOO .pop ('timeout',10 )#line:460
            O0OO0OOO0O0000OOO ._tunnel_host =None #line:462
            HTTPSConnection .__init__ (O0OO0OOO0O0000OOO ,*OOOO0000OOOOO0O0O ,**OO0O0O000OOOO0OOO )#line:464
            O0OO0OOO0O0000OOO .timeout =O0O00OO000O00000O #line:466
            O0OO0OOO0O0000OOO .source_address =O0000000OO0OO0000 #line:467
        def connect (O0000O0O000O00OOO ):#line:469
            ""#line:470
            try :#line:471
                O0000O0O000O00OOO .sock =socket .create_connection ((O0000O0O000O00OOO .host ,O0000O0O000O00OOO .port ),O0000O0O000O00OOO .timeout ,O0000O0O000O00OOO .source_address )#line:476
            except (AttributeError ,TypeError ):#line:477
                O0000O0O000O00OOO .sock =create_connection ((O0000O0O000O00OOO .host ,O0000O0O000O00OOO .port ),O0000O0O000O00OOO .timeout ,O0000O0O000O00OOO .source_address )#line:482
            if O0000O0O000O00OOO ._tunnel_host :#line:484
                O0000O0O000O00OOO ._tunnel ()#line:485
            if ssl :#line:487
                try :#line:488
                    O0OOOO0O000000O00 ={}#line:489
                    if hasattr (ssl ,'SSLContext'):#line:490
                        if O0000O0O000O00OOO ._tunnel_host :#line:491
                            O0OOOO0O000000O00 ['server_hostname']=O0000O0O000O00OOO ._tunnel_host #line:492
                        else :#line:493
                            O0OOOO0O000000O00 ['server_hostname']=O0000O0O000O00OOO .host #line:494
                    O0000O0O000O00OOO .sock =O0000O0O000O00OOO ._context .wrap_socket (O0000O0O000O00OOO .sock ,**O0OOOO0O000000O00 )#line:495
                except AttributeError :#line:496
                    O0000O0O000O00OOO .sock =ssl .wrap_socket (O0000O0O000O00OOO .sock )#line:497
                    try :#line:498
                        O0000O0O000O00OOO .sock .server_hostname =O0000O0O000O00OOO .host #line:499
                    except AttributeError :#line:500
                        pass #line:501
            elif FakeSocket :#line:502
                try :#line:504
                    O0000O0O000O00OOO .sock =FakeSocket (O0000O0O000O00OOO .sock ,socket .ssl (O0000O0O000O00OOO .sock ))#line:505
                except AttributeError :#line:506
                    raise SpeedtestException ('This version of Python does not support HTTPS/SSL ' 'functionality')#line:510
            else :#line:511
                raise SpeedtestException ('This version of Python does not support HTTPS/SSL ' 'functionality')#line:515
def _OO0O0OO0O000O0O00 (O000O000O0OO0O00O ,O0OO0O0OO0OOO0OOO ,O00O0OO000O00000O ,context =None ):#line:518
    ""#line:524
    def OO000OOOOOO0OO000 (OOOO000OO0O00OOO0 ,**OO0O00O0O0OOO0O0O ):#line:525
        OO0O00O0O0OOO0O0O .update ({'source_address':O0OO0O0OO0OOO0OOO ,'timeout':O00O0OO000O00000O })#line:529
        if context :#line:530
            OO0O00O0O0OOO0O0O ['context']=context #line:531
        return O000O000O0OO0O00O (OOOO000OO0O00OOO0 ,**OO0O00O0O0OOO0O0O )#line:532
    return OO000OOOOOO0OO000 #line:533
class SpeedtestHTTPHandler (AbstractHTTPHandler ):#line:536
    ""#line:539
    def __init__ (OO0O000OO0OOO00O0 ,debuglevel =0 ,source_address =None ,timeout =10 ):#line:540
        AbstractHTTPHandler .__init__ (OO0O000OO0OOO00O0 ,debuglevel )#line:541
        OO0O000OO0OOO00O0 .source_address =source_address #line:542
        OO0O000OO0OOO00O0 .timeout =timeout #line:543
    def http_open (OOOO00O0O0000OOO0 ,O0OO0O0O0OO000000 ):#line:545
        return OOOO00O0O0000OOO0 .do_open (_OO0O0OO0O000O0O00 (SpeedtestHTTPConnection ,OOOO00O0O0000OOO0 .source_address ,OOOO00O0O0000OOO0 .timeout ),O0OO0O0O0OO000000 )#line:553
    http_request =AbstractHTTPHandler .do_request_ #line:555
class SpeedtestHTTPSHandler (AbstractHTTPHandler ):#line:558
    ""#line:561
    def __init__ (O0O000OOO000O0OOO ,debuglevel =0 ,context =None ,source_address =None ,timeout =10 ):#line:563
        AbstractHTTPHandler .__init__ (O0O000OOO000O0OOO ,debuglevel )#line:564
        O0O000OOO000O0OOO ._context =context #line:565
        O0O000OOO000O0OOO .source_address =source_address #line:566
        O0O000OOO000O0OOO .timeout =timeout #line:567
    def https_open (OOO0OO00OO0OO0OO0 ,O0O00OOOOOO00O00O ):#line:569
        return OOO0OO00OO0OO0OO0 .do_open (_OO0O0OO0O000O0O00 (SpeedtestHTTPSConnection ,OOO0OO00OO0OO0OO0 .source_address ,OOO0OO00OO0OO0OO0 .timeout ,context =OOO0OO00OO0OO0OO0 ._context ,),O0O00OOOOOO00O00O )#line:578
    https_request =AbstractHTTPHandler .do_request_ #line:580
def build_opener (source_address =None ,timeout =10 ):#line:583
    ""#line:588
    printer ('Timeout set to %d'%timeout ,debug =True )#line:590
    if source_address :#line:592
        O0O00OO0OOOOO0000 =(source_address ,0 )#line:593
        printer ('Binding to source address: %r'%(O0O00OO0OOOOO0000 ,),debug =True )#line:595
    else :#line:596
        O0O00OO0OOOOO0000 =None #line:597
    O00O0O00O0OO0OOOO =[ProxyHandler (),SpeedtestHTTPHandler (source_address =O0O00OO0OOOOO0000 ,timeout =timeout ),SpeedtestHTTPSHandler (source_address =O0O00OO0OOOOO0000 ,timeout =timeout ),HTTPDefaultErrorHandler (),HTTPRedirectHandler (),HTTPErrorProcessor ()]#line:608
    OO00O0OOOOOO0OOOO =OpenerDirector ()#line:610
    OO00O0OOOOOO0OOOO .addheaders =[('User-agent',build_user_agent ())]#line:611
    for OOO00O00OOOO00OOO in O00O0O00O0OO0OOOO :#line:613
        OO00O0OOOOOO0OOOO .add_handler (OOO00O00OOOO00OOO )#line:614
    return OO00O0OOOOOO0OOOO #line:616
class GzipDecodedResponse (GZIP_BASE ):#line:619
    ""#line:625
    def __init__ (OOOO0OO00OO0O0O0O ,OO0O0OO00OO0OOOOO ):#line:626
        if not gzip :#line:629
            raise SpeedtestHTTPError ('HTTP response body is gzip encoded, ' 'but gzip support is not available')#line:631
        O000O0O0O0OOO0O0O =BytesIO or StringIO #line:632
        OOOO0OO00OO0O0O0O .io =O000O0O0O0OOO0O0O ()#line:633
        while 1 :#line:634
            O0000OO00O00O000O =OO0O0OO00OO0OOOOO .read (1024 )#line:635
            if len (O0000OO00O00O000O )==0 :#line:636
                break #line:637
            OOOO0OO00OO0O0O0O .io .write (O0000OO00O00O000O )#line:638
        OOOO0OO00OO0O0O0O .io .seek (0 )#line:639
        gzip .GzipFile .__init__ (OOOO0OO00OO0O0O0O ,mode ='rb',fileobj =OOOO0OO00OO0O0O0O .io )#line:640
    def close (O00O0000000000000 ):#line:642
        try :#line:643
            gzip .GzipFile .close (O00O0000000000000 )#line:644
        finally :#line:645
            O00O0000000000000 .io .close ()#line:646
def get_exception ():#line:649
    ""#line:652
    return sys .exc_info ()[1 ]#line:653
def distance (O0O0O0OO0OO0O0000 ,O0000000OOOOOO0O0 ):#line:656
    ""#line:657
    OO00OO0OOO0O0OOO0 ,O000O0O0OO0O00000 =O0O0O0OO0OO0O0000 #line:659
    OO0O0O0OOOOO000OO ,O00O0OOOO00O0O0OO =O0000000OOOOOO0O0 #line:660
    OO0OO000000OO0OOO =6371 #line:661
    O0OO0O0OOOO0OOO00 =math .radians (OO0O0O0OOOOO000OO -OO00OO0OOO0O0OOO0 )#line:663
    O000OO00OO00OOO0O =math .radians (O00O0OOOO00O0O0OO -O000O0O0OO0O00000 )#line:664
    OOO0O0000000OOO00 =(math .sin (O0OO0O0OOOO0OOO00 /2 )*math .sin (O0OO0O0OOOO0OOO00 /2 )+math .cos (math .radians (OO00OO0OOO0O0OOO0 ))*math .cos (math .radians (OO0O0O0OOOOO000OO ))*math .sin (O000OO00OO00OOO0O /2 )*math .sin (O000OO00OO00OOO0O /2 ))#line:668
    OO000O000OOOOO0O0 =2 *math .atan2 (math .sqrt (OOO0O0000000OOO00 ),math .sqrt (1 -OOO0O0000000OOO00 ))#line:669
    O0OO0OOO0OOO00OOO =OO0OO000000OO0OOO *OO000O000OOOOO0O0 #line:670
    return O0OO0OOO0OOO00OOO #line:672
def build_user_agent ():#line:675
    ""#line:676
    OOO0OO000OOO00OO0 =('Mozilla/5.0','(%s; U; %s; en-us)'%(platform .platform (),platform .architecture ()[0 ]),'Python/%s'%platform .python_version (),'(KHTML, like Gecko)','speedtest-cli/%s'%__version__ )#line:685
    O0O0OO000OO0OO0OO =' '.join (OOO0OO000OOO00OO0 )#line:686
    printer ('User-Agent: %s'%O0O0OO000OO0OO0OO ,debug =True )#line:687
    return O0O0OO000OO0OO0OO #line:688
def build_request (O0O00OO0O0O000O0O ,data =None ,headers =None ,bump ='0',secure =False ):#line:691
    ""#line:696
    if not headers :#line:698
        headers ={}#line:699
    if O0O00OO0O0O000O0O [0 ]==':':#line:701
        OOO0OO000OO00O00O =('http','https')[bool (secure )]#line:702
        OO0OO0O000OO0000O ='%s%s'%(OOO0OO000OO00O00O ,O0O00OO0O0O000O0O )#line:703
    else :#line:704
        OO0OO0O000OO0000O =O0O00OO0O0O000O0O #line:705
    if '?'in O0O00OO0O0O000O0O :#line:707
        OO00OO00OO0O0O0O0 ='&'#line:708
    else :#line:709
        OO00OO00OO0O0O0O0 ='?'#line:710
    OOOOOOOO0O00O0O00 ='%s%sx=%s.%s'%(OO0OO0O000OO0000O ,OO00OO00OO0O0O0O0 ,int (timeit .time .time ()*1000 ),bump )#line:715
    headers .update ({'Cache-Control':'no-cache',})#line:719
    printer ('%s %s'%(('GET','POST')[bool (data )],OOOOOOOO0O00O0O00 ),debug =True )#line:722
    return Request (OOOOOOOO0O00O0O00 ,data =data ,headers =headers )#line:724
def catch_request (OOOO0O0O00O0OO0O0 ,opener =None ):#line:727
    ""#line:731
    if opener :#line:733
        _OOO000OO00000O0O0 =opener .open #line:734
    else :#line:735
        _OOO000OO00000O0O0 =urlopen #line:736
    try :#line:738
        O0OO000O00O0OOO00 =_OOO000OO00000O0O0 (OOOO0O0O00O0OO0O0 )#line:739
        if OOOO0O0O00O0OO0O0 .get_full_url ()!=O0OO000O00O0OOO00 .geturl ():#line:740
            printer ('Redirected to %s'%O0OO000O00O0OOO00 .geturl (),debug =True )#line:741
        return O0OO000O00O0OOO00 ,False #line:742
    except HTTP_ERRORS :#line:743
        O0O0O00OOO0O0O0OO =get_exception ()#line:744
        return None ,O0O0O00OOO0O0O0OO #line:745
def get_response_stream (OO00000O00O0OOOO0 ):#line:748
    ""#line:752
    try :#line:754
        O00O00000OO000O00 =OO00000O00O0OOOO0 .headers .getheader #line:755
    except AttributeError :#line:756
        O00O00000OO000O00 =OO00000O00O0OOOO0 .getheader #line:757
    if O00O00000OO000O00 ('content-encoding')=='gzip':#line:759
        return GzipDecodedResponse (OO00000O00O0OOOO0 )#line:760
    return OO00000O00O0OOOO0 #line:762
def get_attributes_by_tag_name (O0OO000O00O0O00OO ,O0OOOOO0O0OOO0OOO ):#line:765
    ""#line:771
    OO000OOO0OOO00OOO =O0OO000O00O0O00OO .getElementsByTagName (O0OOOOO0O0OOO0OOO )[0 ]#line:772
    return dict (list (OO000OOO0OOO00OOO .attributes .items ()))#line:773
def print_dots (OOO0O0O0OO000O00O ):#line:776
    ""#line:779
    def O0OO000OO0000O0OO (OO000OOO0O0O0O0O0 ,O00000OO000OO0O0O ,start =False ,end =False ):#line:780
        if event_is_set (OOO0O0O0OO000O00O ):#line:781
            return #line:782
        sys .stdout .write ('.')#line:784
        if OO000OOO0O0O0O0O0 +1 ==O00000OO000OO0O0O and end is True :#line:785
            sys .stdout .write ('\n')#line:786
        sys .stdout .flush ()#line:787
    return O0OO000OO0000O0OO #line:788
def do_nothing (*OOO00000OO0O00O00 ,**OO0OOO000O0OO000O ):#line:791
    pass #line:792
class HTTPDownloader (threading .Thread ):#line:795
    ""#line:796
    def __init__ (OO0OO0OOOO000OOOO ,O00O000O0O000O000 ,O00OOO0O000000O0O ,OO000OOOOOO0O00O0 ,OO0O0OOOOOOOOOOO0 ,opener =None ,shutdown_event =None ):#line:799
        threading .Thread .__init__ (OO0OO0OOOO000OOOO )#line:800
        OO0OO0OOOO000OOOO .request =O00OOO0O000000O0O #line:801
        OO0OO0OOOO000OOOO .result =[0 ]#line:802
        OO0OO0OOOO000OOOO .starttime =OO000OOOOOO0O00O0 #line:803
        OO0OO0OOOO000OOOO .timeout =OO0O0OOOOOOOOOOO0 #line:804
        OO0OO0OOOO000OOOO .i =O00O000O0O000O000 #line:805
        if opener :#line:806
            OO0OO0OOOO000OOOO ._opener =opener .open #line:807
        else :#line:808
            OO0OO0OOOO000OOOO ._opener =urlopen #line:809
        if shutdown_event :#line:811
            OO0OO0OOOO000OOOO ._shutdown_event =shutdown_event #line:812
        else :#line:813
            OO0OO0OOOO000OOOO ._shutdown_event =FakeShutdownEvent ()#line:814
    def run (O0O0OOO00O00OO0O0 ):#line:816
        try :#line:817
            if (timeit .default_timer ()-O0O0OOO00O00OO0O0 .starttime )<=O0O0OOO00O00OO0O0 .timeout :#line:818
                O0O0OO0OOO0OOOOOO =O0O0OOO00O00OO0O0 ._opener (O0O0OOO00O00OO0O0 .request )#line:819
                while (not event_is_set (O0O0OOO00O00OO0O0 ._shutdown_event )and (timeit .default_timer ()-O0O0OOO00O00OO0O0 .starttime )<=O0O0OOO00O00OO0O0 .timeout ):#line:822
                    O0O0OOO00O00OO0O0 .result .append (len (O0O0OO0OOO0OOOOOO .read (10240 )))#line:823
                    if O0O0OOO00O00OO0O0 .result [-1 ]==0 :#line:824
                        break #line:825
                O0O0OO0OOO0OOOOOO .close ()#line:826
        except IOError :#line:827
            pass #line:828
        except HTTP_ERRORS :#line:829
            pass #line:830
class HTTPUploaderData (object ):#line:833
    ""#line:836
    def __init__ (O0O00O0O000OO00O0 ,OO00OO00OOO00OOO0 ,O0OOOO0OOO0OOOO00 ,O0OOOOOO0O00O0OOO ,shutdown_event =None ):#line:838
        O0O00O0O000OO00O0 .length =OO00OO00OOO00OOO0 #line:839
        O0O00O0O000OO00O0 .start =O0OOOO0OOO0OOOO00 #line:840
        O0O00O0O000OO00O0 .timeout =O0OOOOOO0O00O0OOO #line:841
        if shutdown_event :#line:843
            O0O00O0O000OO00O0 ._shutdown_event =shutdown_event #line:844
        else :#line:845
            O0O00O0O000OO00O0 ._shutdown_event =FakeShutdownEvent ()#line:846
        O0O00O0O000OO00O0 ._data =None #line:848
        O0O00O0O000OO00O0 .total =[0 ]#line:850
    def pre_allocate (O00O00OO0O000O0O0 ):#line:852
        OO00O0O0OO0O00000 ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'#line:853
        OO0OOOOO0OO0O0O0O =int (round (int (O00O00OO0O000O0O0 .length )/36.0 ))#line:854
        O0O00OO0O0O00O000 =BytesIO or StringIO #line:855
        try :#line:856
            O00O00OO0O000O0O0 ._data =O0O00OO0O0O00O000 (('content1=%s'%(OO00O0O0OO0O00000 *OO0OOOOO0OO0O0O0O )[0 :int (O00O00OO0O000O0O0 .length )-9 ]).encode ())#line:861
        except MemoryError :#line:862
            raise SpeedtestCLIError ('Insufficient memory to pre-allocate upload data. Please ' 'use --no-pre-allocate')#line:866
    @property #line:868
    def data (OOO0OO0OOO000O00O ):#line:869
        if not OOO0OO0OOO000O00O ._data :#line:870
            OOO0OO0OOO000O00O .pre_allocate ()#line:871
        return OOO0OO0OOO000O00O ._data #line:872
    def read (OOOO00O0000OOOO00 ,n =10240 ):#line:874
        if ((timeit .default_timer ()-OOOO00O0000OOOO00 .start )<=OOOO00O0000OOOO00 .timeout and not event_is_set (OOOO00O0000OOOO00 ._shutdown_event )):#line:876
            O0000OO0OO0OO0O00 =OOOO00O0000OOOO00 .data .read (n )#line:877
            OOOO00O0000OOOO00 .total .append (len (O0000OO0OO0OO0O00 ))#line:878
            return O0000OO0OO0OO0O00 #line:879
        else :#line:880
            raise SpeedtestUploadTimeout ()#line:881
    def __len__ (OOOO000O00O0O000O ):#line:883
        return OOOO000O00O0O000O .length #line:884
class HTTPUploader (threading .Thread ):#line:887
    ""#line:888
    def __init__ (OO00O0000OO00OO00 ,OO0OO0O0O0OO0OOO0 ,OOO000OO00OOO0O00 ,OO00O00OOOOOO0OO0 ,OOOOOO00OOO00OOOO ,O0OOOO000O0O0000O ,opener =None ,shutdown_event =None ):#line:891
        threading .Thread .__init__ (OO00O0000OO00OO00 )#line:892
        OO00O0000OO00OO00 .request =OOO000OO00OOO0O00 #line:893
        OO00O0000OO00OO00 .request .data .start =OO00O0000OO00OO00 .starttime =OO00O00OOOOOO0OO0 #line:894
        OO00O0000OO00OO00 .size =OOOOOO00OOO00OOOO #line:895
        OO00O0000OO00OO00 .result =0 #line:896
        OO00O0000OO00OO00 .timeout =O0OOOO000O0O0000O #line:897
        OO00O0000OO00OO00 .i =OO0OO0O0O0OO0OOO0 #line:898
        if opener :#line:900
            OO00O0000OO00OO00 ._opener =opener .open #line:901
        else :#line:902
            OO00O0000OO00OO00 ._opener =urlopen #line:903
        if shutdown_event :#line:905
            OO00O0000OO00OO00 ._shutdown_event =shutdown_event #line:906
        else :#line:907
            OO00O0000OO00OO00 ._shutdown_event =FakeShutdownEvent ()#line:908
    def run (O0OOOO00OO0O0OO0O ):#line:910
        OOOO0OOO0O00O00O0 =O0OOOO00OO0O0OO0O .request #line:911
        try :#line:912
            if ((timeit .default_timer ()-O0OOOO00OO0O0OO0O .starttime )<=O0OOOO00OO0O0OO0O .timeout and not event_is_set (O0OOOO00OO0O0OO0O ._shutdown_event )):#line:914
                try :#line:915
                    OOOO00OO0O0OO0O00 =O0OOOO00OO0O0OO0O ._opener (OOOO0OOO0O00O00O0 )#line:916
                except TypeError :#line:917
                    OOOO0OOO0O00O00O0 =build_request (O0OOOO00OO0O0OO0O .request .get_full_url (),data =OOOO0OOO0O00O00O0 .data .read (O0OOOO00OO0O0OO0O .size ))#line:922
                    OOOO00OO0O0OO0O00 =O0OOOO00OO0O0OO0O ._opener (OOOO0OOO0O00O00O0 )#line:923
                OOOO00OO0O0OO0O00 .read (11 )#line:924
                OOOO00OO0O0OO0O00 .close ()#line:925
                O0OOOO00OO0O0OO0O .result =sum (O0OOOO00OO0O0OO0O .request .data .total )#line:926
            else :#line:927
                O0OOOO00OO0O0OO0O .result =0 #line:928
        except (IOError ,SpeedtestUploadTimeout ):#line:929
            O0OOOO00OO0O0OO0O .result =sum (O0OOOO00OO0O0OO0O .request .data .total )#line:930
        except HTTP_ERRORS :#line:931
            O0OOOO00OO0O0OO0O .result =0 #line:932
class SpeedtestResults (object ):#line:935
    ""#line:946
    def __init__ (O00000O0O0OO0O0OO ,download =0 ,upload =0 ,ping =0 ,server =None ,client =None ,opener =None ,secure =False ):#line:949
        O00000O0O0OO0O0OO .download =download #line:950
        O00000O0O0OO0O0OO .upload =upload #line:951
        O00000O0O0OO0O0OO .ping =ping #line:952
        if server is None :#line:953
            O00000O0O0OO0O0OO .server ={}#line:954
        else :#line:955
            O00000O0O0OO0O0OO .server =server #line:956
        O00000O0O0OO0O0OO .client =client or {}#line:957
        O00000O0O0OO0O0OO ._share =None #line:959
        O00000O0O0OO0O0OO .timestamp ='%sZ'%datetime .datetime .utcnow ().isoformat ()#line:960
        O00000O0O0OO0O0OO .bytes_received =0 #line:961
        O00000O0O0OO0O0OO .bytes_sent =0 #line:962
        if opener :#line:964
            O00000O0O0OO0O0OO ._opener =opener #line:965
        else :#line:966
            O00000O0O0OO0O0OO ._opener =build_opener ()#line:967
        O00000O0O0OO0O0OO ._secure =secure #line:969
    def __repr__ (O0O00O0O0O0000000 ):#line:971
        return repr (O0O00O0O0O0000000 .dict ())#line:972
    def share (O00OO0OOOOOOO0O0O ):#line:974
        ""#line:977
        if O00OO0OOOOOOO0O0O ._share :#line:979
            return O00OO0OOOOOOO0O0O ._share #line:980
        OOO00O0OOOOO00O0O =int (round (O00OO0OOOOOOO0O0O .download /1000.0 ,0 ))#line:982
        O00OOO0O00O0OOOOO =int (round (O00OO0OOOOOOO0O0O .ping ,0 ))#line:983
        OOOOO00O0O00O000O =int (round (O00OO0OOOOOOO0O0O .upload /1000.0 ,0 ))#line:984
        O00OOO00OOOOO0000 =['recommendedserverid=%s'%O00OO0OOOOOOO0O0O .server ['id'],'ping=%s'%O00OOO0O00O0OOOOO ,'screenresolution=','promo=','download=%s'%OOO00O0OOOOO00O0O ,'screendpi=','upload=%s'%OOOOO00O0O00O000O ,'testmethod=http','hash=%s'%md5 (('%s-%s-%s-%s'%(O00OOO0O00O0OOOOO ,OOOOO00O0O00O000O ,OOO00O0OOOOO00O0O ,'297aae72')).encode ()).hexdigest (),'touchscreen=none','startmode=pingselect','accuracy=1','bytesreceived=%s'%O00OO0OOOOOOO0O0O .bytes_received ,'bytessent=%s'%O00OO0OOOOOOO0O0O .bytes_sent ,'serverid=%s'%O00OO0OOOOOOO0O0O .server ['id'],]#line:1007
        O0O0OOOO00O00OOOO ={'Referer':'http://c.speedtest.net/flash/speedtest.swf'}#line:1009
        OO0OOOO00O00O00O0 =build_request ('://www.speedtest.net/api/api.php',data ='&'.join (O00OOO00OOOOO0000 ).encode (),headers =O0O0OOOO00O00OOOO ,secure =O00OO0OOOOOOO0O0O ._secure )#line:1012
        O0OO0OOO0OOO0OOO0 ,O00OO0OOOO0O00OO0 =catch_request (OO0OOOO00O00O00O0 ,opener =O00OO0OOOOOOO0O0O ._opener )#line:1013
        if O00OO0OOOO0O00OO0 :#line:1014
            raise ShareResultsConnectFailure (O00OO0OOOO0O00OO0 )#line:1015
        O00000OOO00O00OOO =O0OO0OOO0OOO0OOO0 .read ()#line:1017
        OO000OO0O00OOO00O =O0OO0OOO0OOO0OOO0 .code #line:1018
        O0OO0OOO0OOO0OOO0 .close ()#line:1019
        if int (OO000OO0O00OOO00O )!=200 :#line:1021
            raise ShareResultsSubmitFailure ('Could not submit results to ' 'speedtest.net')#line:1023
        OO00O0O0OO000OO00 =parse_qs (O00000OOO00O00OOO .decode ())#line:1025
        OOOO0OOOOOOOOO0OO =OO00O0O0OO000OO00 .get ('resultid')#line:1026
        if not OOOO0OOOOOOOOO0OO or len (OOOO0OOOOOOOOO0OO )!=1 :#line:1027
            raise ShareResultsSubmitFailure ('Could not submit results to ' 'speedtest.net')#line:1029
        O00OO0OOOOOOO0O0O ._share ='http://www.speedtest.net/result/%s.png'%OOOO0OOOOOOOOO0OO [0 ]#line:1031
        return O00OO0OOOOOOO0O0O ._share #line:1033
    def dict (O0OOOOOOO0O000O0O ):#line:1035
        ""#line:1036
        return {'download':O0OOOOOOO0O000O0O .download ,'upload':O0OOOOOOO0O000O0O .upload ,'ping':O0OOOOOOO0O000O0O .ping ,'server':O0OOOOOOO0O000O0O .server ,'timestamp':O0OOOOOOO0O000O0O .timestamp ,'bytes_sent':O0OOOOOOO0O000O0O .bytes_sent ,'bytes_received':O0OOOOOOO0O000O0O .bytes_received ,'share':O0OOOOOOO0O000O0O ._share ,'client':O0OOOOOOO0O000O0O .client ,}#line:1048
    @staticmethod #line:1050
    def csv_header (delimiter =','):#line:1051
        ""#line:1052
        OO0OOOOOO000OOO00 =['Server ID','Sponsor','Server Name','Timestamp','Distance','Ping','Download','Upload','Share','IP Address']#line:1055
        OOO0OO00O000O000O =StringIO ()#line:1056
        OO000O0OOOOO0O0OO =csv .writer (OOO0OO00O000O000O ,delimiter =delimiter ,lineterminator ='')#line:1057
        OO000O0OOOOO0O0OO .writerow ([to_utf8 (O00O0OOOOO00O0OOO )for O00O0OOOOO00O0OOO in OO0OOOOOO000OOO00 ])#line:1058
        return OOO0OO00O000O000O .getvalue ()#line:1059
    def csv (O000O00OOOOOO00OO ,delimiter =','):#line:1061
        ""#line:1062
        O0000OOO0O000O0O0 =O000O00OOOOOO00OO .dict ()#line:1064
        O0OO000OO0O0O0OOO =StringIO ()#line:1065
        O0O0000000O00O000 =csv .writer (O0OO000OO0O0O0OOO ,delimiter =delimiter ,lineterminator ='')#line:1066
        OOO0OO0O0000OOOO0 =[O0000OOO0O000O0O0 ['server']['id'],O0000OOO0O000O0O0 ['server']['sponsor'],O0000OOO0O000O0O0 ['server']['name'],O0000OOO0O000O0O0 ['timestamp'],O0000OOO0O000O0O0 ['server']['d'],O0000OOO0O000O0O0 ['ping'],O0000OOO0O000O0O0 ['download'],O0000OOO0O000O0O0 ['upload'],O000O00OOOOOO00OO ._share or '',O000O00OOOOOO00OO .client ['ip']]#line:1070
        O0O0000000O00O000 .writerow ([to_utf8 (O0000O0OOOOO00O0O )for O0000O0OOOOO00O0O in OOO0OO0O0000OOOO0 ])#line:1071
        return O0OO000OO0O0O0OOO .getvalue ()#line:1072
    def json (O0000OO000OOOOOO0 ,pretty =False ):#line:1074
        ""#line:1075
        O0O00000OOO0O000O ={}#line:1077
        if pretty :#line:1078
            O0O00000OOO0O000O .update ({'indent':4 ,'sort_keys':True })#line:1082
        return json .dumps (O0000OO000OOOOOO0 .dict (),**O0O00000OOO0O000O )#line:1083
class Speedtest (object ):#line:1086
    ""#line:1087
    def __init__ (OO000000OOOO0O000 ,config =None ,source_address =None ,timeout =10 ,secure =False ,shutdown_event =None ):#line:1090
        OO000000OOOO0O000 .config ={}#line:1091
        OO000000OOOO0O000 ._source_address =source_address #line:1093
        OO000000OOOO0O000 ._timeout =timeout #line:1094
        OO000000OOOO0O000 ._opener =build_opener (source_address ,timeout )#line:1095
        OO000000OOOO0O000 ._secure =secure #line:1097
        if shutdown_event :#line:1099
            OO000000OOOO0O000 ._shutdown_event =shutdown_event #line:1100
        else :#line:1101
            OO000000OOOO0O000 ._shutdown_event =FakeShutdownEvent ()#line:1102
        OO000000OOOO0O000 .get_config ()#line:1104
        if config is not None :#line:1105
            OO000000OOOO0O000 .config .update (config )#line:1106
        OO000000OOOO0O000 .servers ={}#line:1108
        OO000000OOOO0O000 .closest =[]#line:1109
        OO000000OOOO0O000 ._best ={}#line:1110
        OO000000OOOO0O000 .results =SpeedtestResults (client =OO000000OOOO0O000 .config ['client'],opener =OO000000OOOO0O000 ._opener ,secure =secure ,)#line:1116
    @property #line:1118
    def best (O00O0O00O00000OO0 ):#line:1119
        if not O00O0O00O00000OO0 ._best :#line:1120
            O00O0O00O00000OO0 .get_best_server ()#line:1121
        return O00O0O00O00000OO0 ._best #line:1122
    def get_config (O00O0000OOO00000O ):#line:1124
        ""#line:1127
        OO00OO0O0OO00OO0O ={}#line:1129
        if gzip :#line:1130
            OO00OO0O0OO00OO0O ['Accept-Encoding']='gzip'#line:1131
        O0OOO000O00000OO0 =build_request ('://www.speedtest.net/speedtest-config.php',headers =OO00OO0O0OO00OO0O ,secure =O00O0000OOO00000O ._secure )#line:1133
        O0O0OO00OOO0O00O0 ,O00OOOO0OO000O00O =catch_request (O0OOO000O00000OO0 ,opener =O00O0000OOO00000O ._opener )#line:1134
        if O00OOOO0OO000O00O :#line:1135
            raise ConfigRetrievalError (O00OOOO0OO000O00O )#line:1136
        OO000000O0OOO0O0O =[]#line:1137
        O00OOOO00O000000O =get_response_stream (O0O0OO00OOO0O00O0 )#line:1139
        while 1 :#line:1141
            try :#line:1142
                OO000000O0OOO0O0O .append (O00OOOO00O000000O .read (1024 ))#line:1143
            except (OSError ,EOFError ):#line:1144
                raise ConfigRetrievalError (get_exception ())#line:1145
            if len (OO000000O0OOO0O0O [-1 ])==0 :#line:1146
                break #line:1147
        O00OOOO00O000000O .close ()#line:1148
        O0O0OO00OOO0O00O0 .close ()#line:1149
        if int (O0O0OO00OOO0O00O0 .code )!=200 :#line:1151
            return None #line:1152
        O0OOO0OO00OO000O0 =''.encode ().join (OO000000O0OOO0O0O )#line:1154
        printer ('Config XML:\n%s'%O0OOO0OO00OO000O0 ,debug =True )#line:1156
        try :#line:1158
            try :#line:1159
                OOOOO0OO00OOO0000 =ET .fromstring (O0OOO0OO00OO000O0 )#line:1160
            except ET .ParseError :#line:1161
                O00OOOO0OO000O00O =get_exception ()#line:1162
                raise SpeedtestConfigError ('Malformed speedtest.net configuration: %s'%O00OOOO0OO000O00O )#line:1165
            OOO000OO000OO000O =OOOOO0OO00OOO0000 .find ('server-config').attrib #line:1166
            O0O00O0OOO0O000O0 =OOOOO0OO00OOO0000 .find ('download').attrib #line:1167
            OOOO0OO0O000OO000 =OOOOO0OO00OOO0000 .find ('upload').attrib #line:1168
            OOOO00OOOO0OO0O00 =OOOOO0OO00OOO0000 .find ('client').attrib #line:1170
        except AttributeError :#line:1172
            try :#line:1173
                OOOOO0OO00OOO0000 =DOM .parseString (O0OOO0OO00OO000O0 )#line:1174
            except ExpatError :#line:1175
                O00OOOO0OO000O00O =get_exception ()#line:1176
                raise SpeedtestConfigError ('Malformed speedtest.net configuration: %s'%O00OOOO0OO000O00O )#line:1179
            OOO000OO000OO000O =get_attributes_by_tag_name (OOOOO0OO00OOO0000 ,'server-config')#line:1180
            O0O00O0OOO0O000O0 =get_attributes_by_tag_name (OOOOO0OO00OOO0000 ,'download')#line:1181
            OOOO0OO0O000OO000 =get_attributes_by_tag_name (OOOOO0OO00OOO0000 ,'upload')#line:1182
            OOOO00OOOO0OO0O00 =get_attributes_by_tag_name (OOOOO0OO00OOO0000 ,'client')#line:1184
        OOOO0OOO00O0OO0O0 =[int (O0OOO00OO000O0OOO )for O0OOO00OO000O0OOO in OOO000OO000OO000O ['ignoreids'].split (',')if O0OOO00OO000O0OOO ]#line:1188
        OO000O0O0OOOOOOOO =int (OOOO0OO0O000OO000 ['ratio'])#line:1190
        O0OOO000O000O0OO0 =int (OOOO0OO0O000OO000 ['maxchunkcount'])#line:1191
        O000O0O0O00OO00O0 =[32768 ,65536 ,131072 ,262144 ,524288 ,1048576 ,7340032 ]#line:1192
        O00OO0OOO00O00OO0 ={'upload':O000O0O0O00OO00O0 [OO000O0O0OOOOOOOO -1 :],'download':[350 ,500 ,750 ,1000 ,1500 ,2000 ,2500 ,3000 ,3500 ,4000 ]}#line:1197
        OOOO0OOO00O000000 =len (O00OO0OOO00O00OO0 ['upload'])#line:1199
        OOOOO0OOO0O00OOO0 =int (math .ceil (O0OOO000O000O0OO0 /OOOO0OOO00O000000 ))#line:1201
        OOO0O0OO00OOO00OO ={'upload':OOOOO0OOO0O00OOO0 ,'download':int (O0O00O0OOO0O000O0 ['threadsperurl'])}#line:1206
        O0OOO0000O00OO0OO ={'upload':int (OOOO0OO0O000OO000 ['threads']),'download':int (OOO000OO000OO000O ['threadcount'])*2 }#line:1211
        O00OOO00OO0O0O000 ={'upload':int (OOOO0OO0O000OO000 ['testlength']),'download':int (O0O00O0OOO0O000O0 ['testlength'])}#line:1216
        O00O0000OOO00000O .config .update ({'client':OOOO00OOOO0OO0O00 ,'ignore_servers':OOOO0OOO00O0OO0O0 ,'sizes':O00OO0OOO00O00OO0 ,'counts':OOO0O0OO00OOO00OO ,'threads':O0OOO0000O00OO0OO ,'length':O00OOO00OO0O0O000 ,'upload_max':OOOOO0OOO0O00OOO0 *OOOO0OOO00O000000 })#line:1226
        try :#line:1228
            O00O0000OOO00000O .lat_lon =(float (OOOO00OOOO0OO0O00 ['lat']),float (OOOO00OOOO0OO0O00 ['lon']))#line:1229
        except ValueError :#line:1230
            raise SpeedtestConfigError ('Unknown location: lat=%r lon=%r'%(OOOO00OOOO0OO0O00 .get ('lat'),OOOO00OOOO0OO0O00 .get ('lon')))#line:1234
        printer ('Config:\n%r'%O00O0000OOO00000O .config ,debug =True )#line:1236
        return O00O0000OOO00000O .config #line:1238
    def get_servers (OOO0O0OOOOO0000O0 ,servers =None ,exclude =None ):#line:1240
        ""#line:1243
        if servers is None :#line:1244
            servers =[]#line:1245
        if exclude is None :#line:1247
            exclude =[]#line:1248
        OOO0O0OOOOO0000O0 .servers .clear ()#line:1250
        for OO000O00O00O00OO0 in (servers ,exclude ):#line:1252
            for OO00O0OO0OO0OO000 ,O0O0O0000O0OOO0OO in enumerate (OO000O00O00O00OO0 ):#line:1253
                try :#line:1254
                    OO000O00O00O00OO0 [OO00O0OO0OO0OO000 ]=int (O0O0O0000O0OOO0OO )#line:1255
                except ValueError :#line:1256
                    raise InvalidServerIDType ('%s is an invalid server type, must be int'%O0O0O0000O0OOO0OO )#line:1259
        OO000000OO0O00O00 =['://www.speedtest.net/speedtest-servers-static.php','http://c.speedtest.net/speedtest-servers-static.php','://www.speedtest.net/speedtest-servers.php','http://c.speedtest.net/speedtest-servers.php',]#line:1266
        O0O0O0O0OO0OOO0O0 ={}#line:1268
        if gzip :#line:1269
            O0O0O0O0OO0OOO0O0 ['Accept-Encoding']='gzip'#line:1270
        O00OO0OO000O000OO =[]#line:1272
        for O00O0OOOO0O0OOOO0 in OO000000OO0O00O00 :#line:1273
            try :#line:1274
                O0OOO00000000OO00 =build_request ('%s?threads=%s'%(O00O0OOOO0O0OOOO0 ,OOO0O0OOOOO0000O0 .config ['threads']['download']),headers =O0O0O0O0OO0OOO0O0 ,secure =OOO0O0OOOOO0000O0 ._secure )#line:1280
                O00000OOOO0OO000O ,O00O00O00OO0O00O0 =catch_request (O0OOO00000000OO00 ,opener =OOO0O0OOOOO0000O0 ._opener )#line:1281
                if O00O00O00OO0O00O0 :#line:1282
                    O00OO0OO000O000OO .append ('%s'%O00O00O00OO0O00O0 )#line:1283
                    raise ServersRetrievalError ()#line:1284
                OOOOOO000O00OO0O0 =get_response_stream (O00000OOOO0OO000O )#line:1286
                OO000O0OOOO000O0O =[]#line:1288
                while 1 :#line:1289
                    try :#line:1290
                        OO000O0OOOO000O0O .append (OOOOOO000O00OO0O0 .read (1024 ))#line:1291
                    except (OSError ,EOFError ):#line:1292
                        raise ServersRetrievalError (get_exception ())#line:1293
                    if len (OO000O0OOOO000O0O [-1 ])==0 :#line:1294
                        break #line:1295
                OOOOOO000O00OO0O0 .close ()#line:1297
                O00000OOOO0OO000O .close ()#line:1298
                if int (O00000OOOO0OO000O .code )!=200 :#line:1300
                    raise ServersRetrievalError ()#line:1301
                OOOO0OO0OO0OOOO00 =''.encode ().join (OO000O0OOOO000O0O )#line:1303
                printer ('Servers XML:\n%s'%OOOO0OO0OO0OOOO00 ,debug =True )#line:1305
                try :#line:1307
                    try :#line:1308
                        try :#line:1309
                            OO00OO00OOO0OO0O0 =ET .fromstring (OOOO0OO0OO0OOOO00 )#line:1310
                        except ET .ParseError :#line:1311
                            O00O00O00OO0O00O0 =get_exception ()#line:1312
                            raise SpeedtestServersError ('Malformed speedtest.net server list: %s'%O00O00O00OO0O00O0 )#line:1315
                        O000OO0O0OO0OO0O0 =etree_iter (OO00OO00OOO0OO0O0 ,'server')#line:1316
                    except AttributeError :#line:1317
                        try :#line:1318
                            OO00OO00OOO0OO0O0 =DOM .parseString (OOOO0OO0OO0OOOO00 )#line:1319
                        except ExpatError :#line:1320
                            O00O00O00OO0O00O0 =get_exception ()#line:1321
                            raise SpeedtestServersError ('Malformed speedtest.net server list: %s'%O00O00O00OO0O00O0 )#line:1324
                        O000OO0O0OO0OO0O0 =OO00OO00OOO0OO0O0 .getElementsByTagName ('server')#line:1325
                except (SyntaxError ,xml .parsers .expat .ExpatError ):#line:1326
                    raise ServersRetrievalError ()#line:1327
                for O0OOO00O00O00OOOO in O000OO0O0OO0OO0O0 :#line:1329
                    try :#line:1330
                        OO000O0O0OO00OO00 =O0OOO00O00O00OOOO .attrib #line:1331
                    except AttributeError :#line:1332
                        OO000O0O0OO00OO00 =dict (list (O0OOO00O00O00OOOO .attributes .items ()))#line:1333
                    if servers and int (OO000O0O0OO00OO00 .get ('id'))not in servers :#line:1335
                        continue #line:1336
                    if (int (OO000O0O0OO00OO00 .get ('id'))in OOO0O0OOOOO0000O0 .config ['ignore_servers']or int (OO000O0O0OO00OO00 .get ('id'))in exclude ):#line:1339
                        continue #line:1340
                    try :#line:1342
                        O00O0000O0OO0OOO0 =distance (OOO0O0OOOOO0000O0 .lat_lon ,(float (OO000O0O0OO00OO00 .get ('lat')),float (OO000O0O0OO00OO00 .get ('lon'))))#line:1345
                    except Exception :#line:1346
                        continue #line:1347
                    OO000O0O0OO00OO00 ['d']=O00O0000O0OO0OOO0 #line:1349
                    try :#line:1351
                        OOO0O0OOOOO0000O0 .servers [O00O0000O0OO0OOO0 ].append (OO000O0O0OO00OO00 )#line:1352
                    except KeyError :#line:1353
                        OOO0O0OOOOO0000O0 .servers [O00O0000O0OO0OOO0 ]=[OO000O0O0OO00OO00 ]#line:1354
                break #line:1356
            except ServersRetrievalError :#line:1358
                continue #line:1359
        if (servers or exclude )and not OOO0O0OOOOO0000O0 .servers :#line:1361
            raise NoMatchedServers ()#line:1362
        return OOO0O0OOOOO0000O0 .servers #line:1364
    def set_mini_server (O0OO0000O0O0O0OO0 ,O0OO0O00OO000O0O0 ):#line:1366
        ""#line:1369
        OOO0OOOO000OO0OOO =urlparse (O0OO0O00OO000O0O0 )#line:1371
        OO0O0O00O000000OO ,O0O000000000OOO00 =os .path .splitext (OOO0OOOO000OO0OOO [2 ])#line:1373
        if O0O000000000OOO00 :#line:1374
            O00OO00OO00O0OOOO =os .path .dirname (O0OO0O00OO000O0O0 )#line:1375
        else :#line:1376
            O00OO00OO00O0OOOO =O0OO0O00OO000O0O0 #line:1377
        O000OOO00O00O0O0O =build_request (O00OO00OO00O0OOOO )#line:1379
        O00OOOOO0OO0O0OOO ,OO00000OOO000O00O =catch_request (O000OOO00O00O0O0O ,opener =O0OO0000O0O0O0OO0 ._opener )#line:1380
        if OO00000OOO000O00O :#line:1381
            raise SpeedtestMiniConnectFailure ('Failed to connect to %s'%O0OO0O00OO000O0O0 )#line:1383
        else :#line:1384
            OO0O0O0OO0O0O0000 =O00OOOOO0OO0O0OOO .read ()#line:1385
            O00OOOOO0OO0O0OOO .close ()#line:1386
        O0000OOO00OO0O000 =re .findall ('upload_?[Ee]xtension: "([^"]+)"',OO0O0O0OO0O0O0000 .decode ())#line:1389
        if not O0000OOO00OO0O000 :#line:1390
            for O0O000000000OOO00 in ['php','asp','aspx','jsp']:#line:1391
                try :#line:1392
                    OO000O000O0OOO00O =O0OO0000O0O0O0OO0 ._opener .open ('%s/speedtest/upload.%s'%(O00OO00OO00O0OOOO ,O0O000000000OOO00 ))#line:1395
                except Exception :#line:1396
                    pass #line:1397
                else :#line:1398
                    OOOOO0O0O0OO0O00O =OO000O000O0OOO00O .read ().strip ().decode ()#line:1399
                    if (OO000O000O0OOO00O .code ==200 and len (OOOOO0O0O0OO0O00O .splitlines ())==1 and re .match ('size=[0-9]',OOOOO0O0O0OO0O00O )):#line:1402
                        O0000OOO00OO0O000 =[O0O000000000OOO00 ]#line:1403
                        break #line:1404
        if not OOO0OOOO000OO0OOO or not O0000OOO00OO0O000 :#line:1405
            raise InvalidSpeedtestMiniServer ('Invalid Speedtest Mini Server: ' '%s'%O0OO0O00OO000O0O0 )#line:1407
        O0OO0000O0O0O0OO0 .servers =[{'sponsor':'Speedtest Mini','name':OOO0OOOO000OO0OOO [1 ],'d':0 ,'url':'%s/speedtest/upload.%s'%(O00OO00OO00O0OOOO .rstrip ('/'),O0000OOO00OO0O000 [0 ]),'latency':0 ,'id':0 }]#line:1416
        return O0OO0000O0O0O0OO0 .servers #line:1418
    def get_closest_servers (OO0OOO0O000O0OO0O ,limit =5 ):#line:1420
        ""#line:1423
        if not OO0OOO0O000O0OO0O .servers :#line:1425
            OO0OOO0O000O0OO0O .get_servers ()#line:1426
        for O000000OOO0OO0OOO in sorted (OO0OOO0O000O0OO0O .servers .keys ()):#line:1428
            for O0OOOOOOO0O0OO0O0 in OO0OOO0O000O0OO0O .servers [O000000OOO0OO0OOO ]:#line:1429
                OO0OOO0O000O0OO0O .closest .append (O0OOOOOOO0O0OO0O0 )#line:1430
                if len (OO0OOO0O000O0OO0O .closest )==limit :#line:1431
                    break #line:1432
            else :#line:1433
                continue #line:1434
            break #line:1435
        printer ('Closest Servers:\n%r'%OO0OOO0O000O0OO0O .closest ,debug =True )#line:1437
        return OO0OOO0O000O0OO0O .closest #line:1438
    def get_best_server (O000O00O000O0OOO0 ,servers =None ):#line:1440
        ""#line:1443
        if not servers :#line:1445
            if not O000O00O000O0OOO0 .closest :#line:1446
                servers =O000O00O000O0OOO0 .get_closest_servers ()#line:1447
            servers =O000O00O000O0OOO0 .closest #line:1448
        if O000O00O000O0OOO0 ._source_address :#line:1450
            OOOOO00OOOOO00OO0 =(O000O00O000O0OOO0 ._source_address ,0 )#line:1451
        else :#line:1452
            OOOOO00OOOOO00OO0 =None #line:1453
        O0O0O00OOOOO0O0OO =build_user_agent ()#line:1455
        OOOOO00OO00OOOO00 ={}#line:1457
        for OO0OOO0OOOO0OOOO0 in servers :#line:1458
            O000OOO00O0O0O0O0 =[]#line:1459
            O0000OOO00O000OO0 =os .path .dirname (OO0OOO0OOOO0OOOO0 ['url'])#line:1460
            O0OOO00OOO0OO0O0O =int (timeit .time .time ()*1000 )#line:1461
            OOO0O00O0OOO00OO0 ='%s/latency.txt?x=%s'%(O0000OOO00O000OO0 ,O0OOO00OOO0OO0O0O )#line:1462
            for O00000OOOOO00O0OO in range (0 ,3 ):#line:1463
                OO0000O0O000OOO0O ='%s.%s'%(OOO0O00O0OOO00OO0 ,O00000OOOOO00O0OO )#line:1464
                printer ('%s %s'%('GET',OO0000O0O000OOO0O ),debug =True )#line:1466
                O0000O00OOO0O000O =urlparse (OOO0O00O0OOO00OO0 )#line:1467
                try :#line:1468
                    if O0000O00OOO0O000O [0 ]=='https':#line:1469
                        OOO0OOO000O0O0000 =SpeedtestHTTPSConnection (O0000O00OOO0O000O [1 ],source_address =OOOOO00OOOOO00OO0 )#line:1473
                    else :#line:1474
                        OOO0OOO000O0O0000 =SpeedtestHTTPConnection (O0000O00OOO0O000O [1 ],source_address =OOOOO00OOOOO00OO0 )#line:1478
                    O000O000O00OOOOO0 ={'User-Agent':O0O0O00OOOOO0O0OO }#line:1479
                    O0000OOOO0OOO0OOO ='%s?%s'%(O0000O00OOO0O000O [2 ],O0000O00OOO0O000O [4 ])#line:1480
                    O0OO000OOO0OOO0O0 =timeit .default_timer ()#line:1481
                    OOO0OOO000O0O0000 .request ("GET",O0000OOOO0OOO0OOO ,headers =O000O000O00OOOOO0 )#line:1482
                    OO00000O0O0000O0O =OOO0OOO000O0O0000 .getresponse ()#line:1483
                    OOOOOO0OO0O00OOOO =(timeit .default_timer ()-O0OO000OOO0OOO0O0 )#line:1484
                except HTTP_ERRORS :#line:1485
                    O00O0O0000O0OO00O =get_exception ()#line:1486
                    printer ('ERROR: %r'%O00O0O0000O0OO00O ,debug =True )#line:1487
                    O000OOO00O0O0O0O0 .append (3600 )#line:1488
                    continue #line:1489
                OO0O00OOO0OO0OO0O =OO00000O0O0000O0O .read (9 )#line:1491
                if int (OO00000O0O0000O0O .status )==200 and OO0O00OOO0OO0OO0O =='test=test'.encode ():#line:1492
                    O000OOO00O0O0O0O0 .append (OOOOOO0OO0O00OOOO )#line:1493
                else :#line:1494
                    O000OOO00O0O0O0O0 .append (3600 )#line:1495
                OOO0OOO000O0O0000 .close ()#line:1496
            O0O00O00OO000000O =round ((sum (O000OOO00O0O0O0O0 )/6 )*1000.0 ,3 )#line:1498
            OOOOO00OO00OOOO00 [O0O00O00OO000000O ]=OO0OOO0OOOO0OOOO0 #line:1499
        try :#line:1501
            OO0OO0OO0OO00O000 =sorted (OOOOO00OO00OOOO00 .keys ())[0 ]#line:1502
        except IndexError :#line:1503
            raise SpeedtestBestServerFailure ('Unable to connect to servers to ' 'test latency.')#line:1505
        OOOOOOO0000O0OOOO =OOOOO00OO00OOOO00 [OO0OO0OO0OO00O000 ]#line:1506
        OOOOOOO0000O0OOOO ['latency']=OO0OO0OO0OO00O000 #line:1507
        O000O00O000O0OOO0 .results .ping =OO0OO0OO0OO00O000 #line:1509
        O000O00O000O0OOO0 .results .server =OOOOOOO0000O0OOOO #line:1510
        O000O00O000O0OOO0 ._best .update (OOOOOOO0000O0OOOO )#line:1512
        printer ('Best Server:\n%r'%OOOOOOO0000O0OOOO ,debug =True )#line:1513
        return OOOOOOO0000O0OOOO #line:1514
    def download (O000O00OOOOOOOO00 ,callback =do_nothing ,threads =None ):#line:1516
        ""#line:1521
        OOO000000000O00OO =[]#line:1523
        for O00OO000O00000OOO in O000O00OOOOOOOO00 .config ['sizes']['download']:#line:1524
            for _O0OO0OO000000OO0O in range (0 ,O000O00OOOOOOOO00 .config ['counts']['download']):#line:1525
                OOO000000000O00OO .append ('%s/random%sx%s.jpg'%(os .path .dirname (O000O00OOOOOOOO00 .best ['url']),O00OO000O00000OOO ,O00OO000O00000OOO ))#line:1527
        O0O0O000O0OOO00O0 =len (OOO000000000O00OO )#line:1529
        O000O0OOO0O0O00O0 =[]#line:1530
        for OO00OO000OOO0OO0O ,OOOO0000O0OO0000O in enumerate (OOO000000000O00OO ):#line:1531
            O000O0OOO0O0O00O0 .append (build_request (OOOO0000O0OO0000O ,bump =OO00OO000OOO0OO0O ,secure =O000O00OOOOOOOO00 ._secure ))#line:1534
        O00OO0OO0O0O00OOO =threads or O000O00OOOOOOOO00 .config ['threads']['download']#line:1536
        OO0OO00O0OOOOOOOO ={'threads':0 }#line:1537
        def O0OOO0OO00O00000O (OOOO00000000OO00O ,O0000OOOOOOO00O0O ,OOOO00OOOOOO00O00 ):#line:1539
            for O0OO0O0O000OO0O0O ,OOO0OOOOOO0000OO0 in enumerate (O0000OOOOOOO00O0O ):#line:1540
                OOO00OO000OOOOOOO =HTTPDownloader (O0OO0O0O000OO0O0O ,OOO0OOOOOO0000OO0 ,OOOOOO0O0000OO000 ,O000O00OOOOOOOO00 .config ['length']['download'],opener =O000O00OOOOOOOO00 ._opener ,shutdown_event =O000O00OOOOOOOO00 ._shutdown_event )#line:1548
                while OO0OO00O0OOOOOOOO ['threads']>=O00OO0OO0O0O00OOO :#line:1549
                    timeit .time .sleep (0.001 )#line:1550
                OOO00OO000OOOOOOO .start ()#line:1551
                OOOO00000000OO00O .put (OOO00OO000OOOOOOO ,True )#line:1552
                OO0OO00O0OOOOOOOO ['threads']+=1 #line:1553
                callback (O0OO0O0O000OO0O0O ,OOOO00OOOOOO00O00 ,start =True )#line:1554
        O0OOO0OO000O0OO00 =[]#line:1556
        def OO00000000OOOOO00 (O00OOOOO0O0O000O0 ,O0O0O0OOOOOOO0OOO ):#line:1558
            _OOO0000OOO0O00OOO =thread_is_alive #line:1559
            while len (O0OOO0OO000O0OO00 )<O0O0O0OOOOOOO0OOO :#line:1560
                O000O00O0O0OOOO00 =O00OOOOO0O0O000O0 .get (True )#line:1561
                while _OOO0000OOO0O00OOO (O000O00O0O0OOOO00 ):#line:1562
                    O000O00O0O0OOOO00 .join (timeout =0.001 )#line:1563
                OO0OO00O0OOOOOOOO ['threads']-=1 #line:1564
                O0OOO0OO000O0OO00 .append (sum (O000O00O0O0OOOO00 .result ))#line:1565
                callback (O000O00O0O0OOOO00 .i ,O0O0O0OOOOOOO0OOO ,end =True )#line:1566
        O00OOOO00OO0OOO00 =Queue (O00OO0OO0O0O00OOO )#line:1568
        OO0000O00O0OOOOO0 =threading .Thread (target =O0OOO0OO00O00000O ,args =(O00OOOO00OO0OOO00 ,O000O0OOO0O0O00O0 ,O0O0O000O0OOO00O0 ))#line:1570
        OO0O0OO0000O0000O =threading .Thread (target =OO00000000OOOOO00 ,args =(O00OOOO00OO0OOO00 ,O0O0O000O0OOO00O0 ))#line:1572
        OOOOOO0O0000OO000 =timeit .default_timer ()#line:1573
        OO0000O00O0OOOOO0 .start ()#line:1574
        OO0O0OO0000O0000O .start ()#line:1575
        _O0OO0OO0000OOO000 =thread_is_alive #line:1576
        while _O0OO0OO0000OOO000 (OO0000O00O0OOOOO0 ):#line:1577
            OO0000O00O0OOOOO0 .join (timeout =0.001 )#line:1578
        while _O0OO0OO0000OOO000 (OO0O0OO0000O0000O ):#line:1579
            OO0O0OO0000O0000O .join (timeout =0.001 )#line:1580
        O0O0OOO0000OO00O0 =timeit .default_timer ()#line:1582
        O000O00OOOOOOOO00 .results .bytes_received =sum (O0OOO0OO000O0OO00 )#line:1583
        O000O00OOOOOOOO00 .results .download =((O000O00OOOOOOOO00 .results .bytes_received /(O0O0OOO0000OO00O0 -OOOOOO0O0000OO000 ))*8.0 )#line:1586
        if O000O00OOOOOOOO00 .results .download >100000 :#line:1587
            O000O00OOOOOOOO00 .config ['threads']['upload']=8 #line:1588
        return O000O00OOOOOOOO00 .results .download #line:1589
    def upload (O0OO0000OOO000OOO ,callback =do_nothing ,pre_allocate =True ,threads =None ):#line:1591
        ""#line:1596
        OOO0O0O00OO0OO000 =[]#line:1598
        for O0O0OOOO0OOO0O000 in O0OO0000OOO000OOO .config ['sizes']['upload']:#line:1600
            for _O00OO0OOO0OO00O00 in range (0 ,O0OO0000OOO000OOO .config ['counts']['upload']):#line:1601
                OOO0O0O00OO0OO000 .append (O0O0OOOO0OOO0O000 )#line:1602
        OO0O0OOOO000OO00O =O0OO0000OOO000OOO .config ['upload_max']#line:1605
        OOOOOOOOO0O0O0OO0 =[]#line:1607
        for O0OO0O00O00OO0O00 ,O0O0OOOO0OOO0O000 in enumerate (OOO0O0O00OO0OO000 ):#line:1608
            OO0O0O0000O0OO00O =HTTPUploaderData (O0O0OOOO0OOO0O000 ,0 ,O0OO0000OOO000OOO .config ['length']['upload'],shutdown_event =O0OO0000OOO000OOO ._shutdown_event )#line:1616
            if pre_allocate :#line:1617
                OO0O0O0000O0OO00O .pre_allocate ()#line:1618
            O0O0OO0OOO0O000O0 ={'Content-length':O0O0OOOO0OOO0O000 }#line:1620
            OOOOOOOOO0O0O0OO0 .append ((build_request (O0OO0000OOO000OOO .best ['url'],OO0O0O0000O0OO00O ,secure =O0OO0000OOO000OOO ._secure ,headers =O0O0OO0OOO0O000O0 ),O0O0OOOO0OOO0O000 ))#line:1627
        O000O00O0000OO00O =threads or O0OO0000OOO000OOO .config ['threads']['upload']#line:1629
        O0OOO00O000OO0OO0 ={'threads':0 }#line:1630
        def O0O0O00O00O0O0OO0 (O0O00OO0OO0OOO00O ,O0OOO00O0OO0OO0O0 ,O0OO00O0OO0OO0OO0 ):#line:1632
            for OO00000OOO00O0OOO ,O0OO00OOO0000O0OO in enumerate (O0OOO00O0OO0OO0O0 [:O0OO00O0OO0OO0OO0 ]):#line:1633
                OOOO0OOOO0000O0O0 =HTTPUploader (OO00000OOO00O0OOO ,O0OO00OOO0000O0OO [0 ],OO00000OO000OO0O0 ,O0OO00OOO0000O0OO [1 ],O0OO0000OOO000OOO .config ['length']['upload'],opener =O0OO0000OOO000OOO ._opener ,shutdown_event =O0OO0000OOO000OOO ._shutdown_event )#line:1642
                while O0OOO00O000OO0OO0 ['threads']>=O000O00O0000OO00O :#line:1643
                    timeit .time .sleep (0.001 )#line:1644
                OOOO0OOOO0000O0O0 .start ()#line:1645
                O0O00OO0OO0OOO00O .put (OOOO0OOOO0000O0O0 ,True )#line:1646
                O0OOO00O000OO0OO0 ['threads']+=1 #line:1647
                callback (OO00000OOO00O0OOO ,O0OO00O0OO0OO0OO0 ,start =True )#line:1648
        O0OO000OO000O00O0 =[]#line:1650
        def O00OO0OO0O0000OO0 (OOO0OOO000O0OO000 ,O000O000OO000000O ):#line:1652
            _OOOO000OOO000000O =thread_is_alive #line:1653
            while len (O0OO000OO000O00O0 )<O000O000OO000000O :#line:1654
                O0O00O0OO0OO0OOO0 =OOO0OOO000O0OO000 .get (True )#line:1655
                while _OOOO000OOO000000O (O0O00O0OO0OO0OOO0 ):#line:1656
                    O0O00O0OO0OO0OOO0 .join (timeout =0.001 )#line:1657
                O0OOO00O000OO0OO0 ['threads']-=1 #line:1658
                O0OO000OO000O00O0 .append (O0O00O0OO0OO0OOO0 .result )#line:1659
                callback (O0O00O0OO0OO0OOO0 .i ,O000O000OO000000O ,end =True )#line:1660
        O0OOO0O00O00OO000 =Queue (threads or O0OO0000OOO000OOO .config ['threads']['upload'])#line:1662
        O00O0OOO00OO00O00 =threading .Thread (target =O0O0O00O00O0O0OO0 ,args =(O0OOO0O00O00OO000 ,OOOOOOOOO0O0O0OO0 ,OO0O0OOOO000OO00O ))#line:1664
        O0OO0OOO0OOO0O0OO =threading .Thread (target =O00OO0OO0O0000OO0 ,args =(O0OOO0O00O00OO000 ,OO0O0OOOO000OO00O ))#line:1666
        OO00000OO000OO0O0 =timeit .default_timer ()#line:1667
        O00O0OOO00OO00O00 .start ()#line:1668
        O0OO0OOO0OOO0O0OO .start ()#line:1669
        _O0O0O0OO00O0OO00O =thread_is_alive #line:1670
        while _O0O0O0OO00O0OO00O (O00O0OOO00OO00O00 ):#line:1671
            O00O0OOO00OO00O00 .join (timeout =0.1 )#line:1672
        while _O0O0O0OO00O0OO00O (O0OO0OOO0OOO0O0OO ):#line:1673
            O0OO0OOO0OOO0O0OO .join (timeout =0.1 )#line:1674
        OOOO00OOO0O0O0OOO =timeit .default_timer ()#line:1676
        O0OO0000OOO000OOO .results .bytes_sent =sum (O0OO000OO000O00O0 )#line:1677
        O0OO0000OOO000OOO .results .upload =((O0OO0000OOO000OOO .results .bytes_sent /(OOOO00OOO0O0O0OOO -OO00000OO000OO0O0 ))*8.0 )#line:1680
        return O0OO0000OOO000OOO .results .upload #line:1681
def ctrl_c (OO0000O0OO0OOOO00 ):#line:1684
    ""#line:1687
    def O00O00000OOOOO000 (O0OO00OOO00O000O0 ,OOO0OOO0OOOOOO0O0 ):#line:1688
        OO0000O0OO0OOOO00 .set ()#line:1689
        printer ('\nCancelling...',error =True )#line:1690
        sys .exit (0 )#line:1691
    return O00O00000OOOOO000 #line:1692
def version ():#line:1695
    ""#line:1696
    printer ('speedtest-cli %s'%__version__ )#line:1698
    printer ('Python %s'%sys .version .replace ('\n',''))#line:1699
    sys .exit (0 )#line:1700
def csv_header (delimiter =','):#line:1703
    ""#line:1704
    printer (SpeedtestResults .csv_header (delimiter =delimiter ))#line:1706
    sys .exit (0 )#line:1707
def parse_args ():#line:1710
    ""#line:1711
    OOOO0OO0O0OO0OO00 =('Command line interface for testing internet bandwidth using ' 'speedtest.net.\n' '------------------------------------------------------------' '--------------\n' 'https://github.com/sivel/speedtest-cli')#line:1717
    OO0OOOOOO0000O000 =ArgParser (description =OOOO0OO0O0OO0OO00 )#line:1719
    try :#line:1722
        OO0OOOOOO0000O000 .add_argument =OO0OOOOOO0000O000 .add_option #line:1723
    except AttributeError :#line:1724
        pass #line:1725
    OO0OOOOOO0000O000 .add_argument ('--no-download',dest ='download',default =True ,action ='store_const',const =False ,help ='Do not perform download test')#line:1728
    OO0OOOOOO0000O000 .add_argument ('--no-upload',dest ='upload',default =True ,action ='store_const',const =False ,help ='Do not perform upload test')#line:1731
    OO0OOOOOO0000O000 .add_argument ('--single',default =False ,action ='store_true',help ='Only use a single connection instead of ' 'multiple. This simulates a typical file ' 'transfer.')#line:1735
    OO0OOOOOO0000O000 .add_argument ('--bytes',dest ='units',action ='store_const',const =('byte',8 ),default =('bit',1 ),help ='Display values in bytes instead of bits. Does ' 'not affect the image generated by --share, nor ' 'output from --json or --csv')#line:1740
    OO0OOOOOO0000O000 .add_argument ('--share',action ='store_true',help ='Generate and provide a URL to the speedtest.net ' 'share results image, not displayed with --csv')#line:1743
    OO0OOOOOO0000O000 .add_argument ('--simple',action ='store_true',default =False ,help ='Suppress verbose output, only show basic ' 'information')#line:1746
    OO0OOOOOO0000O000 .add_argument ('--csv',action ='store_true',default =False ,help ='Suppress verbose output, only show basic ' 'information in CSV format. Speeds listed in ' 'bit/s and not affected by --bytes')#line:1750
    OO0OOOOOO0000O000 .add_argument ('--csv-delimiter',default =',',type =PARSER_TYPE_STR ,help ='Single character delimiter to use in CSV ' 'output. Default ","')#line:1753
    OO0OOOOOO0000O000 .add_argument ('--csv-header',action ='store_true',default =False ,help ='Print CSV headers')#line:1755
    OO0OOOOOO0000O000 .add_argument ('--json',action ='store_true',default =False ,help ='Suppress verbose output, only show basic ' 'information in JSON format. Speeds listed in ' 'bit/s and not affected by --bytes')#line:1759
    OO0OOOOOO0000O000 .add_argument ('--list',action ='store_true',help ='Display a list of speedtest.net servers ' 'sorted by distance')#line:1762
    OO0OOOOOO0000O000 .add_argument ('--server',type =PARSER_TYPE_INT ,action ='append',help ='Specify a server ID to test against. Can be ' 'supplied multiple times')#line:1765
    OO0OOOOOO0000O000 .add_argument ('--exclude',type =PARSER_TYPE_INT ,action ='append',help ='Exclude a server from selection. Can be ' 'supplied multiple times')#line:1768
    OO0OOOOOO0000O000 .add_argument ('--mini',help ='URL of the Speedtest Mini server')#line:1769
    OO0OOOOOO0000O000 .add_argument ('--source',help ='Source IP address to bind to')#line:1770
    OO0OOOOOO0000O000 .add_argument ('--timeout',default =10 ,type =PARSER_TYPE_FLOAT ,help ='HTTP timeout in seconds. Default 10')#line:1772
    OO0OOOOOO0000O000 .add_argument ('--secure',action ='store_true',help ='Use HTTPS instead of HTTP when communicating ' 'with speedtest.net operated servers')#line:1775
    OO0OOOOOO0000O000 .add_argument ('--no-pre-allocate',dest ='pre_allocate',action ='store_const',default =True ,const =False ,help ='Do not pre allocate upload data. Pre allocation ' 'is enabled by default to improve upload ' 'performance. To support systems with ' 'insufficient memory, use this option to avoid a ' 'MemoryError')#line:1782
    OO0OOOOOO0000O000 .add_argument ('--version',action ='store_true',help ='Show the version number and exit')#line:1784
    OO0OOOOOO0000O000 .add_argument ('--debug',action ='store_true',help =ARG_SUPPRESS ,default =ARG_SUPPRESS )#line:1786
    O0OOOO0OOO0000OO0 =OO0OOOOOO0000O000 .parse_args ()#line:1788
    if isinstance (O0OOOO0OOO0000OO0 ,tuple ):#line:1789
        OOOO00OO0O0OO0OOO =O0OOOO0OOO0000OO0 [0 ]#line:1790
    else :#line:1791
        OOOO00OO0O0OO0OOO =O0OOOO0OOO0000OO0 #line:1792
    return OOOO00OO0O0OO0OOO #line:1793
def validate_optional_args (OO000000O0O0OOO00 ):#line:1796
    ""#line:1802
    O0O0OOOO0O0000O00 ={'json':('json/simplejson python module',json ),'secure':('SSL support',HTTPSConnection ),}#line:1806
    for OO000O0OOOOOOOOO0 ,O0000OO0OO0O0O000 in O0O0OOOO0O0000O00 .items ():#line:1808
        if getattr (OO000000O0O0OOO00 ,OO000O0OOOOOOOOO0 ,False )and O0000OO0OO0O0O000 [1 ]is None :#line:1809
            raise SystemExit ('%s is not installed. --%s is ' 'unavailable'%(O0000OO0OO0O0O000 [0 ],OO000O0OOOOOOOOO0 ))#line:1811
def printer (O0OO0O00OO0OO0000 ,quiet =False ,debug =False ,error =False ,**O0000O0O0O000O0O0 ):#line:1814
    ""#line:1815
    if debug and not DEBUG :#line:1817
        return #line:1818
    if debug :#line:1820
        if sys .stdout .isatty ():#line:1821
            OO0OOOO0O0O0OOOOO ='\033[1;30mDEBUG: %s\033[0m'%O0OO0O00OO0OO0000 #line:1822
        else :#line:1823
            OO0OOOO0O0O0OOOOO ='DEBUG: %s'%O0OO0O00OO0OO0000 #line:1824
    else :#line:1825
        OO0OOOO0O0O0OOOOO =O0OO0O00OO0OO0000 #line:1826
    if error :#line:1828
        O0000O0O0O000O0O0 ['file']=sys .stderr #line:1829
    if not quiet :#line:1831
        print_ (OO0OOOO0O0O0OOOOO ,**O0000O0O0O000O0O0 )#line:1832
def shell ():#line:1835
    ""#line:1836
    global DEBUG #line:1838
    OOO000000O0OO00OO =threading .Event ()#line:1839
    signal .signal (signal .SIGINT ,ctrl_c (OOO000000O0OO00OO ))#line:1841
    OOO0OOOO000O0OO00 =parse_args ()#line:1843
    if OOO0OOOO000O0OO00 .version :#line:1846
        version ()#line:1847
    if not OOO0OOOO000O0OO00 .download and not OOO0OOOO000O0OO00 .upload :#line:1849
        raise SpeedtestCLIError ('Cannot supply both --no-download and ' '--no-upload')#line:1851
    if len (OOO0OOOO000O0OO00 .csv_delimiter )!=1 :#line:1853
        raise SpeedtestCLIError ('--csv-delimiter must be a single character')#line:1854
    if OOO0OOOO000O0OO00 .csv_header :#line:1856
        csv_header (OOO0OOOO000O0OO00 .csv_delimiter )#line:1857
    validate_optional_args (OOO0OOOO000O0OO00 )#line:1859
    O000O0OOOO0000O00 =getattr (OOO0OOOO000O0OO00 ,'debug',False )#line:1861
    if O000O0OOOO0000O00 =='SUPPRESSHELP':#line:1862
        O000O0OOOO0000O00 =False #line:1863
    if O000O0OOOO0000O00 :#line:1864
        DEBUG =True #line:1865
    if OOO0OOOO000O0OO00 .simple or OOO0OOOO000O0OO00 .csv or OOO0OOOO000O0OO00 .json :#line:1867
        O000O0OOOO000OO0O =True #line:1868
    else :#line:1869
        O000O0OOOO000OO0O =False #line:1870
    if OOO0OOOO000O0OO00 .csv or OOO0OOOO000O0OO00 .json :#line:1872
        O0000OOOO0O0OO0O0 =True #line:1873
    else :#line:1874
        O0000OOOO0O0OO0O0 =False #line:1875
    if O000O0OOOO000OO0O or O000O0OOOO0000O00 :#line:1878
        O0OO0O000OO0OO0OO =do_nothing #line:1879
    else :#line:1880
        O0OO0O000OO0OO0OO =print_dots (OOO000000O0OO00OO )#line:1881
    printer ('',O000O0OOOO000OO0O )#line:1883
    try :#line:1884
        OOOO0000OOOOOO00O =Speedtest (source_address =OOO0OOOO000O0OO00 .source ,timeout =OOO0OOOO000O0OO00 .timeout ,secure =OOO0OOOO000O0OO00 .secure )#line:1889
    except (ConfigRetrievalError ,)+HTTP_ERRORS :#line:1890
        printer ('Cannot retrieve speedtest configuration',error =True )#line:1891
        raise SpeedtestCLIError (get_exception ())#line:1892
    if OOO0OOOO000O0OO00 .list :#line:1894
        try :#line:1895
            OOOO0000OOOOOO00O .get_servers ()#line:1896
        except (ServersRetrievalError ,)+HTTP_ERRORS :#line:1897
            printer ('Cannot retrieve speedtest server list',error =True )#line:1898
            raise SpeedtestCLIError (get_exception ())#line:1899
        for _OO0O0OO000OOOOOOO ,OOO000O00OO000OOO in sorted (OOOO0000OOOOOO00O .servers .items ()):#line:1901
            for OO000000O0O0O000O in OOO000O00OO000OOO :#line:1902
                O00000O0O00O00O00 =('%(id)5s) %(sponsor)s (%(name)s, %(country)s) ' '[%(d)0.2f km]'%OO000000O0O0O000O )#line:1904
                try :#line:1905
                    printer (O00000O0O00O00O00 )#line:1906
                except IOError :#line:1907
                    O000OO0O00OOO00OO =get_exception ()#line:1908
                    if O000OO0O00OOO00OO .errno !=errno .EPIPE :#line:1909
                        raise #line:1910
        sys .exit (0 )#line:1911
    printer ('*🔭 Testing From %(isp)s...*\n'%OOOO0000OOOOOO00O .config ['client'],O000O0OOOO000OO0O )#line:1914
    if not OOO0OOOO000O0OO00 .mini :#line:1916
        printer ('📑 Retrieving speedtest.net server list...',O000O0OOOO000OO0O )#line:1917
        try :#line:1918
            OOOO0000OOOOOO00O .get_servers (servers =OOO0OOOO000O0OO00 .server ,exclude =OOO0OOOO000O0OO00 .exclude )#line:1919
        except NoMatchedServers :#line:1920
            raise SpeedtestCLIError ('No matched servers: %s'%', '.join ('%s'%OOO0O00OO0OOO000O for OOO0O00OO0OOO000O in OOO0OOOO000O0OO00 .server ))#line:1924
        except (ServersRetrievalError ,)+HTTP_ERRORS :#line:1925
            printer ('Cannot retrieve speedtest server list',error =True )#line:1926
            raise SpeedtestCLIError (get_exception ())#line:1927
        except InvalidServerIDType :#line:1928
            raise SpeedtestCLIError ('%s is an invalid server type, must ' 'be an int'%', '.join ('%s'%OOOOO00O0O00OOO0O for OOOOO00O0O00OOO0O in OOO0OOOO000O0OO00 .server ))#line:1932
        if OOO0OOOO000O0OO00 .server and len (OOO0OOOO000O0OO00 .server )==1 :#line:1934
            printer ('📰 Retrieving information for the selected server...',O000O0OOOO000OO0O )#line:1935
        else :#line:1936
            printer ('🔎 Selección del mejor servidor basado en ping...',O000O0OOOO000OO0O )#line:1937
        OOOO0000OOOOOO00O .get_best_server ()#line:1938
    elif OOO0OOOO000O0OO00 .mini :#line:1939
        OOOO0000OOOOOO00O .get_best_server (OOOO0000OOOOOO00O .set_mini_server (OOO0OOOO000O0OO00 .mini ))#line:1940
    O00O00OOOO00OOO00 =OOOO0000OOOOOO00O .results #line:1942
    printer ('\n...................................................................................\n🏬 *Hosted By :* %(sponsor)s\n🌎 *Ubicación :* %(name)s [%(d)0.2f km] ' '\n🟢 *Ping :* %(latency)s ms'%O00O00OOOO00OOO00 .server ,O000O0OOOO000OO0O )#line:1945
    if OOO0OOOO000O0OO00 .download :#line:1947
        printer ('',O000O0OOOO000OO0O ,end =('','\n')[bool (O000O0OOOO0000O00 )])#line:1949
        OOOO0000OOOOOO00O .download (callback =O0OO0O000OO0OO0OO ,threads =(None ,1 )[OOO0OOOO000O0OO00 .single ])#line:1953
        printer ('*📫 Descarga:* %0.2f M%s/s'%((O00O00OOOO00OOO00 .download /1000.0 /1000.0 )/OOO0OOOO000O0OO00 .units [1 ],OOO0OOOO000O0OO00 .units [0 ]),O000O0OOOO000OO0O )#line:1957
    else :#line:1958
        printer ('Skipping download test',O000O0OOOO000OO0O )#line:1959
    if OOO0OOOO000O0OO00 .upload :#line:1961
        OOOO0000OOOOOO00O .upload ()#line:1962
        printer ('*🚀 Subida:* %0.2f M%s/s'%((O00O00OOOO00OOO00 .upload /1000.0 /1000.0 )/OOO0OOOO000O0OO00 .units [1 ],OOO0OOOO000O0OO00 .units [0 ]),O000O0OOOO000OO0O )#line:1966
        printer ("\n...................................................................................\n▶︎ POWERED BY *OOKLA*\n▶︎ Script By *FG98*")#line:1967
    else :#line:1968
        printer ('Skipping upload test',O000O0OOOO000OO0O )#line:1969
    printer ('Results:\n%r'%O00O00OOOO00OOO00 .dict (),debug =True )#line:1971
    if not OOO0OOOO000O0OO00 .simple and OOO0OOOO000O0OO00 .share :#line:1973
        O00O00OOOO00OOO00 .share ()#line:1974
    if OOO0OOOO000O0OO00 .simple :#line:1976
        printer ('Ping: %s ms\nDownload: %0.2f M%s/s\nUpload: %0.2f M%s/s'%(O00O00OOOO00OOO00 .ping ,(O00O00OOOO00OOO00 .download /1000.0 /1000.0 )/OOO0OOOO000O0OO00 .units [1 ],OOO0OOOO000O0OO00 .units [0 ],(O00O00OOOO00OOO00 .upload /1000.0 /1000.0 )/OOO0OOOO000O0OO00 .units [1 ],OOO0OOOO000O0OO00 .units [0 ]))#line:1982
    elif OOO0OOOO000O0OO00 .csv :#line:1983
        printer (O00O00OOOO00OOO00 .csv (delimiter =OOO0OOOO000O0OO00 .csv_delimiter ))#line:1984
    elif OOO0OOOO000O0OO00 .json :#line:1985
        printer (O00O00OOOO00OOO00 .json ())#line:1986
    if OOO0OOOO000O0OO00 .share and not O0000OOOO0O0OO0O0 :#line:1988
        printer ('▶︎Compartir resultado: %s'%O00O00OOOO00OOO00 .share ())#line:1989
def main ():#line:1992
    try :#line:1993
        shell ()#line:1994
    except KeyboardInterrupt :#line:1995
        printer ('\nCancelling...',error =True )#line:1996
    except (SpeedtestException ,SystemExit ):#line:1997
        OO00O0O0000O000O0 =get_exception ()#line:1998
        if getattr (OO00O0O0000O000O0 ,'code',1 )not in (0 ,2 ):#line:2000
            OOOO0OOO0OOO0OO00 ='%s'%OO00O0O0000O000O0 #line:2001
            if not OOOO0OOO0OOO0OO00 :#line:2002
                OOOO0OOO0OOO0OO00 ='%r'%OO00O0O0000O000O0 #line:2003
            raise SystemExit ('ERROR: %s'%OOOO0OOO0OOO0OO00 )#line:2004
if __name__ =='__main__':#line:2007
    main ()#line:2008
