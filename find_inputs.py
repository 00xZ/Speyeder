#Python3.9
import requests 
from bs4 import BeautifulSoup
from lxml import html, etree
import sys, fnmatch, threading
import re, os
import random
import urllib3

urllib3.disable_warnings()
def presentation():

	print("  ░██████╗██████╗░███████╗██╗░░░██╗███████╗██████╗░███████╗██████╗░")
	print("  ██╔════╝██╔══██╗██╔════╝╚██╗░██╔╝██╔════╝██╔══██╗██╔════╝██╔══██╗")
	print("  ╚█████╗░██████╔╝█████╗░░░╚████╔╝░█████╗░░██║░░██║█████╗░░██████╔╝")
	print("  ░╚═══██╗██╔═══╝░██╔══╝░░░░╚██╔╝░░██╔══╝░░██║░░██║██╔══╝░░██╔══██╗")
	print("  ██████╔╝██║░░░░░███████╗░░░██║░░░███████╗██████╔╝███████╗██║░░██║")
	print("  ╚═════╝░╚═╝░░░░░╚══════╝░░░╚═╝░░░╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝")
	print("                                                                   ")
	print("   ~By Eyezik github/00xZ     Find Inputs                          ")

def title(url, proxy):
	url = (url)
	print(url)
	sitelists = []
	print("[+] Crawling: " +url)
	blacklist = ['*stackoverflow*', "*mikrotik*", "*plesk*", "*pinterest*", '*youtu*',  '*wikipedia*', "*apache*", '*microsoft*', '*centos*', '*google*', '*yahoo*', '*cloudflare*','*instagram*', '*facebook*' ,'*youtube*', '*twitter*','*tiktok*','*snapchat*','*gmail*','*amazon*', '*nginx*' ,'*bing*']
	try:
		headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Content-Type":"*"}
		rqt = requests.get(url, timeout=25, verify=True, headers=headers, proxies=proxy)
		soupr = BeautifulSoup(rqt.content, 'html.parser')
		
		for link in soupr.select('a[href*="?"]'):
			site = (link.get('href'))
			site = str(site)
			if any([fnmatch.fnmatch(site, filtering) for filtering in blacklist]):
				continue
			urlin = bool(url in site)#Url Is In Quiry
			print(urlin)
			if urlin == False:
				site = (url +"" +site)
				print(site + " Added ext. was - " + url)
			else: pass
			print("\n [!] Found Branch: " +site)
			if site not in sitelists:
				try:
					r = requests.get(site, timeout=25, verify=True, headers=headers, proxies=proxy)
					print("  [+] Branched: " + site + " [+]")
					#fotitle = open("output_with_title.txt", "a+") # Feel free to commit this out i just use it for logging
					#fotitle.write(site + " : " + title +  "\n")
					#fotitle.close
					#print("Appended branch: " + site)
					sitelists.append(site)
					#print("Appended ")
					fo = open("xss_output.txt", "a+")
					fo.write(site + "\n")
					fo.close
				except Exception:
					#print("Branch already scanned: " + site)
					Print(" [+] Next [+]")
					pass
			else:
				pass
	except Exception:
		#print("Error: " + site)
		pass
def whatitbe(ip, proxy):
	url = (ip)
	if proxy == '':
		pass
	else:
		proxy = {"http": "http://" +proxy}
	#print(proxy)
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) YA boy Eyezik AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Content-Type":"*"}
	#print(headers)
	try:
		#print("Debug 1 " + url)
		reqeer = requests.get(url, timeout=6, headers=headers, verify=False)
		#print(reqeer + "Debug 2")
		title(url, proxy)
	except Exception:
		#print(" [!] Site Timed Out: "+url+" [!] ")
		title(url, proxy)
		pass
def main():
	presentation()
	#fo = open("output.txt", "w")
	#fo.write("\n")
	#fo.close
	count = 0
	if str(sys.argv[1]) == "-h":
		print("Use:")
		print("    Make sure to add https://")
		print("    Single server scan: sqleye.py [Server]")
		print("    Scan with proxy: sqleye.py [Server] -p 1.2.3.4")
		print("    Scan with proxy: sqleye.py -f filename -p 1.2.3.4")
		print("    Scan ips in file use: sqleye.py -f filename")
	elif str(sys.argv[1]) == "-f":
		input_file = open(sys.argv[2])
		proxy = ('')
		try:
			if str(sys.argv[3]) == "-p":
				proxy = str(sys.argv[4])
				print("Proxy: " + proxy)
			else:
				pass
		except Exception:
			pass
		for i in input_file.readlines():
			ip = i.strip("\n")
			whatitbe(ip, proxy)
	elif len(sys.argv) > 1 :
		ip = str(sys.argv[1])
		proxy = ('')
		print("Server: " + ip)
		try:
			if str(sys.argv[2]) == "-p":
				proxy = str(sys.argv[3])
				print("Proxy: " + proxy)
			else:
				pass
		except Exception:
			pass
		whatitbe(ip, proxy)
	else:
		print("Use -h for help")
		pass
main()



