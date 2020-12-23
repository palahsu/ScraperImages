import bs4
import requests
import shutil
import os

data = input('Search Images:')
size = int(input('How Much Images: '))

while True:
    choice = input("What Search Engine do you want to use?\n    1) Google\n    2) Bing\n    > Answer(1 or 2): ")
    if choice.lower() == "1" or choice.lower() == 'GOOGLE_IMAGE':
                        GOOGLE_IMAGE  = \
                            'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
                        break
    elif choice.lower() == "2" or choice.lower() == 'BING_IMAGE':
                        BING_IMAGE = \
                          'https://bing.com/'
                        break
    else:
        print("\n Wrong input, try again", 'red')
                        #time.sleep(3)
                        #clrscr()
        continue                    

def extract(data, size):
    
    while True:
        ans = choice
        if ans == '1':
            URL_input = GOOGLE_IMAGE + 'q=' + data
            print('Fetching from url =', URL_input)
            break
        elif ans == '2':    
          URL_input = BING_IMAGE + 'q=' + data
          print('Fetching from url =', URL_input)
          
          continue
                   
    URLdata = requests.get(URL_input)
    soup = bs4.BeautifulSoup(URLdata.text, "html.parser")
    img = soup.find_all('img')
    i = 0
    print('Please wait..')
    while i < size:

        for link in img:
            try:
                images = link.get('src')
                ext = images[images.rindex('.'):]
                if ext.startswith('.png'):
                    ext = '.png'
                elif ext.startswith('.jpg'):
                    ext = '.jpg'
                elif ext.startswith('.jfif'):
                    ext = '.jfif'
                elif ext.startswith('.com'):
                    ext = '.jpg'
                elif ext.startswith('.svg'):
                    ext = '.svg'
                data = requests.get(images, stream=True)
                filename = "Downloads/"+str(i) + ext
                with open(filename, 'wb') as file:
                    shutil.copyfileobj(data.raw, file)
                i += 1
            except:
                pass
    print('\t\t\t Downloaded Successfull\t\t ')

extract(data, size)

#By palahsu
#NOTE: Some code lines have been modified.
