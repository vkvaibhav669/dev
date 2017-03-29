from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
my_url
uClient = uReq(my_url)
#a connection is set up btwn pae and pc

page_html = uClient.read()
uClient.close()
#to close the page when the reading and all is done
last_soup = soup(page_html , "html.parser")
#stored as a html.parser file
#grabs each product
container = last_soup.findAll("div" , {"class" :"item-container"})




 


#extrats the html parts with a directde way
contain = container[0]
#used for looping purpose it will traverse till the lenghth of the container is not satisfied 
for contain in container :
	brand =  contain.div.div.a.img["title"]
	name = contain.findAll("a",{"class":"item-title"})
	product_name = name[0].text
	shippin = contain.findAll("li",{"class":"price-ship"})	
#title part is inside the img of the html and so we need the interpreter to be more specific what we actually want
 #used strip to remove all the whitespace and all other
 #use of dot operater to access the inner parts in any code language
	shiping = shippin[0].text.strip()
	print("brand :"+brand)
	print("product name :"	+product_name)
	print("shiping :"+shiping)
	
