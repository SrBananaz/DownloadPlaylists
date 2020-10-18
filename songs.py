from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pathlib import Path
import os

"""  -- Modificar directorio de descarga(desabilitado, por ahora) y corregir erros de navegador menores. --"""


options = webdriver.ChromeOptions() 
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
"""prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory": 
                        r"ruta xd",
             "directory_upgrade": True}
options.add_experimental_option("prefs", prefs)""" 


""" -- Buscar directorio de descargas y archivo mas reciente en esta misma carpeta. -- """


path_D = str(Path.home() / "Downloads")
os.chdir(path_D)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]


""" -- Pedir la url de la playlist y extraer los links de la playlist.  -- """


driver = webdriver.Chrome("C:/Users/nejen/Downloads/idk/chromedriver.exe", chrome_options=options)
driver.get("https://guihkx.github.io/ulist/")
url_playlist = driver.find_element_by_id("youtube-url")
url_playlist.send_keys(input("URL: "))
url_playlist.send_keys(u'\ue007')
path, dirs, files = next(os.walk(path_D))
file_count_original = len(files)
sleep(10) #A mimir 
driver.find_element_by_id("btn-download").click()
while True:
	path, dirs, files = next(os.walk(path_D))
	file_count_modi = len(files)
	if file_count_original<file_count_modi: #Verificar si el txt se descargó. 
		break


""" -- Descargar las canciones.  -- """


with open(path_D+"\\"+newest) as fp: #Buscar el archivo en el directorio de descargas.
   for cnt, line in enumerate(fp):
   	   seconds = 0
   	   path, dirs, files = next(os.walk(path_D))
   	   file_count_original = len(files)
   	   driver.get("https://ytmp3.cc/en13/") #Ir a la pagina de descargar.
   	   while True:
   	       try:
   	           driver.find_element_by_tag_name('input').send_keys(line) #Introducir la url
   	           sleep(5) # A mimir 
   	           break
   	       except:
   	           pass
   	           

   	   while seconds <26:
   	       sleep(1)  # A mimir 
   	       seconds += 1 
   	       print(seconds)
   	       try:
   	       	   driver.find_element_by_link_text("Download").click() #Descargar la canción
   	       	   break
   	       except:
   	       		try:
   	       			error = driver.find_element_by_xpath("//*[@id='error']/p[2]/a[1]")
   	       			error.click()
   	       			sleep(3) # A mimir 
   	       			form = driver.find_element_by_tag_name('input')
   	       			form.send_keys(line)
   	       			btn = driver.find_element_by_link_text("Download")
   	       			btn.click()
   	       		except:
   	       			pass

   	   seconds = 0
   	   while seconds <26:
   	   	   sleep(1) # A mimir
   	   	   seconds +=1
   	   	   print(f"seconds descarga: {seconds}")
   	   	   path, dirs, files = next(os.walk(path_D))
   	   	   file_count_modi = len(files)
   	   	   if file_count_modi>file_count_original: #Verificar si se descargó.
   	   	   	break

   	   try: #Cerrar ventana emergente, en caso de que haya una.
   	   	   sleep(2) # A mimir 
   	   	   driver.switch_to.window(driver.window_handles[1])
   	   	   driver.close() 
   	   	   driver.switch_to.window(driver.window_handles[0]) 
   	   except:
   	   	pass

   	   		
   	   		

   	   		   	       	   