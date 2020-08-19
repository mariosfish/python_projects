import requests
import logging
from datetime import datetime

dt = datetime.now().strftime('%m-%d-%Y %I:%M')
name=f'sites_logs {dt}.log'
LOG_FORMAT = "%(levelname)s %(asctime)s: %(message)s"
logging.basicConfig(filename=name, level=logging.INFO, format=LOG_FORMAT, datefmt='%m/%d/%Y %I:%M:%S', filemode='w')

def check_site(url):
        
        try:
            request = requests.head(url,timeout=5)
            if request.ok:
                logging.info(f'Site: {url} has response {request.status_code}. It seems to be OK.')
        except requests.exceptions.InvalidSchema as err:
            logging.error("Bad schema, expecting http:// or https:// : %s" % (err,))
        except requests.exceptions.InvalidURL as err:
            logging.error("Invalid URL '%s': %s" % (url, err))
        except requests.exceptions.ConnectionError as err:
            logging.error("Couldn't establish connection to '%s': %s" % (url, err))      
        except requests.exceptions.RequestException as err:
            logging.error(msg="Unknown error connecting to '%s': %s" % (url, err))
        # except requests.exceptions.HTTPError as err:
        #     logging.critical("Unexpected status code '%d' accessing URL: %s" % (request.status_code, url))



sites = ['https://army.gr/','https://smx.army.gr/', 'https://san.army.gr/', 'https://setha.army.gr/', 'https://aooa.army.gr/', 'https://dis.army.gr/', 'https://spsx.army.gr/',
'https://katataxi.army.gr/', 'https://ekems.army.gr/', 'https://smy.army.gr/', 'https://mts.army.gr/', 'https://sath.army.gr/', 'https://sthad.army.gr/',
'https://spb.army.gr/', 'https://steamx.army.gr/', 'https://nrdc.army.gr/', 'https://spz.army.gr/', 'https://sey.army.gr/', 'https://mpsotc.army.gr/',
'https://seap.army.gr/', 'https://sse.army.gr/', 'https://asdys.army.gr/', 'https://ssas.army.gr/', 'https://sxo.army.gr/', 'https://laed.army.gr/',
'https://fww.army.gr/', 'https://ethnofilaki.army.gr/', 'https://asye.army.gr/', 'https://sse190.army.gr/', 'https://frourarxeioathinon.army.gr/',
'https://steatx.army.gr/', 'https://401gsn.army.gr/', 'https://404gsn.army.gr/', 'https://414snen.army.gr/', 'https://alumnisetha.army.gr/',
'https://alumniadispo.army.gr/', 'https://alumnispsx.army.gr/', 'https://alumnisan.army.gr/', 'https://alumnismy.army.gr/', 'https://forensics.army.gr/',
'https://emathisi.army.gr/', 'https://esetha.army.gr/', 'https://eadispo.army.gr/', 'https://espsx.army.gr/', 'https://wargames.army.gr/',
'https://elearning-spb.army.gr/', 'https://elearning-des.army.gr/', 'https://elearning-sas.army.gr/', 'https://elearning-sdb.army.gr/', 'https://elearning-sem.army.gr/',
'https://elearning-sey.army.gr/', 'https://elearning-smx.army.gr/', 'https://elearning-spz.army.gr/', 'https://elearning-sth.army.gr/',
'https://elearning-syp.army.gr/','https://elearning-tx.army.gr/','https://elearning-smy.army.gr/','https://elearning-diged.army.gr/','https://elearning-sxo.army.gr/']

print(len(sites))
print("Start checking...")
for site in sites:
    print("Checking",site)
    check_site(site)
print("Finished!")



    
