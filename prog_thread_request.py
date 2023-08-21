import threading
import urllib.request
import time

start = time.time()

urls = ["http://google.com", "http://apple.com", "http://facebook.com", "http://instagram.com"]

def abrir_site(url):
    analise_site = urllib.request.Request(url)
    subir_site = urllib.request.urlopen(analise_site)
    visualizar_site = subir_site.read()
    print("%s' carregar em %ss" % (url, (time.time() - start)))

threads = [threading.Thread(target=abrir_site, args=(url,)) for url in urls]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Elapsed time: %s" % (time.time() - start))