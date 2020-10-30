import time as tm

import pandas as pd
import requests

SITE_LIST = ['bebeosis.army.gr', 'spider.army.gr', 'bbb.army.gr', 'army.gr', 'smx.army.gr', 'san.army.gr',
             'setha.army.gr', 'aooa.army.gr', 'dis.army.gr', 'spsx.army.gr',
             'katataxi.army.gr', 'ekems.army.gr', 'smy.army.gr', 'mts.army.gr', 'sath.army.gr', 'sthad.army.gr',
             'spb.army.gr', 'steamx.army.gr', 'nrdc.army.gr', 'spz.army.gr', 'sey.army.gr', 'mpsotc.army.gr',
             'seap.army.gr', 'sse.army.gr', 'asdys.army.gr', 'ssas.army.gr', 'sxo.army.gr', 'laed.army.gr',
             'fww.army.gr', 'ethnofilaki.army.gr', 'asye.army.gr', 'sse190.army.gr', 'frourarxeioathinon.army.gr',
             'steatx.army.gr', '401gsn.army.gr', '404gsn.army.gr', '414snen.army.gr', 'alumnisetha.army.gr',
             'alumniadispo.army.gr', 'alumnispsx.army.gr', 'alumnisan.army.gr', 'alumnismy.army.gr',
             'forensics.army.gr',
             'emathisi.army.gr', 'esetha.army.gr', 'eadispo.army.gr', 'espsx.army.gr', 'wargames.army.gr',
             'elearning-spb.army.gr', 'elearning-des.army.gr', 'elearning-sas.army.gr', 'elearning-sdb.army.gr',
             'elearning-sem.army.gr',
             'elearning-sey.army.gr', 'elearning-smx.army.gr', 'elearning-spz.army.gr', 'elearning-sth.army.gr',
             'elearning-syp.army.gr', 'elearning-tx.army.gr', 'elearning-smy.army.gr', 'elearning-diged.army.gr',
             'elearning-sxo.army.gr']
duration_ = []
results = []


def get_status(site_):
    try:
        response = requests.head(site_, timeout=10)
        status_code = response.status_code
        reason = response.reason
    except requests.exceptions.ReadTimeout:
        status_code = '-'
        reason = 'Read timed out'
    except requests.exceptions.ConnectionError:
        status_code = '000'
        reason = 'ConnectionError'
    return site_, status_code, reason


for url in SITE_LIST:
    start = tm.time()
    site = 'http://{}'.format(url)
    if get_status(site)[1] in [302, 303]:
        site = 'https://{}'.format(url)
    print(get_status(site))
    stop = tm.time()
    duration = stop - start
    duration_.append(duration)
    results.append(get_status(site))

df = pd.DataFrame(data=results, columns=[
                  'site', 'status_code', 'reason'], index=None)
df['time elapsed for the response'] = pd.Series(duration_)
df.to_excel('results.xlsx', index=False)
