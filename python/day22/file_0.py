import urllib.request as req

#Читать
link = 'https://www.google.com'

akipress = req.urlopen(link)
akipress_text = akipress.read()

print(akipress_text)

file = open('sample.txt', 'w')
# Записать на файл sample.txt
file.write(str(akipress_text))
