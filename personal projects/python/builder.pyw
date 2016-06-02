import pyqrcode
import png
from PIL import Image
import os, os.path
import time
import io
import csv
import tkinter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32com.client as comclt


def main():
  date = time.strftime("%Y-%m-%d")
  albumName = None
  albumNameString = None

  try: numFiles = len([name for name in os.listdir('./' + date +'/prints/')])
  except FileNotFoundError:
    root = tkinter.Tk()
    root.withdraw()
    d = Dialog(root)

    root.wait_window(d.top)
    albumName = d.albumName
    albumNameString = d.albumNameString
    os.mkdir('./'+date)
    os.mkdir('./' + date + '/prints')
    numFiles = 0
  
  computer_number = 0

  code = pyqrcode.create(str(str(numFiles) + "," + date + "," + str(computer_number) + ","))
  
  code.png('code.png',scale=5)
  qrcode = Image.open('code.png','r')
  background = Image.new('RGBA',(1240,1844),(0,0,0,0))
  offset = (0,1659)
  background.paste(qrcode,offset)
  background.save('C:\Program Files\BreezeSys\DSLR Remote Pro\PhotoboothImages\MOJO 800x600\overlay.png')
  CSV_Parse(numFiles,date,computer_number, albumName,albumNameString)


  


def CSV_Parse(numFiles,date,computer, albumName,albumNameString):
  isNew = False
  csvFileName = None
  while True:
    newNum = len([name for name in os.listdir('./' + date + '/prints/')])
    
    if newNum > numFiles:
      break;
    else:
      time.sleep(10)

  files = sorted([f for f in os.listdir('./'+date + '/prints/')])
  
  #write to file using numFiles as key, and the filename as the value
  #files[-1] is value
  try:
    csvfile = open(str(computer) + date + ".csv", 'a')
    if os.path.getsize(str(computer) + date + ".csv") == 0: isNew = True
  
  except FileNotFoundError:
    csvfile = open(str(computer) + date + ".csv", 'w')
    isNew = True

      
  csvFileName = str(computer) + date + ".csv"
  
    
  writer = csv.writer(csvfile, delimiter=',')
  
  if(isNew):
    writer.writerow(albumName)
  
  writer.writerow([numFiles] + [files[-1]])
  filenameString = files[-1]

  csvfile.close()
  if(isNew):
    WebUploadNewAlbum(albumNameString,filenameString)
  else:
    WebUploadOldAlbum(csvFileName,filenameString)

  WebUploadCSV(csvFileName)
  os.remove('C:\Program Files\BreezeSys\DSLR Remote Pro\PhotoboothImages\MOJO 800x600\overlay.png')


def WebUploadNewAlbum(albumNameString,filenameString):
  albumNameHyphenReplace = (albumNameString.replace(",","").replace("-"," ") +
                            " "+ time.strftime("%m").lstrip("0") + "/" +
                            time.strftime("%d").lstrip("0") + "/" +
                            time.strftime("%Y"))

  
  browser = webdriver.Firefox()
  browser.get("http://members.webs.com/MembersB/editAppPage.jsp?app=photos&pageID=278815598#photos/")


  username = browser.find_element_by_name('j_username')
  password = browser.find_element_by_name('j_password')

  username.send_keys('cfausn@gmail.com')
  password.send_keys('*****')

  password.send_keys(Keys.RETURN)


  iframe = browser.find_elements_by_tag_name('iframe')
  browser.switch_to_frame(iframe[1])

  elm = browser.find_element_by_xpath(".//*[@id='webs-bin-null']/div/div/h3/div/div[1]/span[1]/a")
  elm.click()

  elm = browser.find_element_by_xpath(".//*[@id='title']")
  elm.send_keys(albumNameHyphenReplace)
  iframe = browser.find_elements_by_tag_name('iframe')
  browser.switch_to_frame(iframe[0])
  browser.find_element_by_xpath("html/body/div[1]/label").click()

  time.sleep(2)
  wsh = comclt.Dispatch("WScript.Shell")
  
  wsh.SendKeys("C:\\DSlrRemote\\" + time.strftime("%Y-%m-%d") + "\\prints\\" + filenameString)
  time.sleep(2)
  wsh.SendKeys("~") #enter key

  browser.switch_to_default_content()
  iframe = browser.find_elements_by_tag_name('iframe')
  browser.switch_to_frame(iframe[1])
  browser.find_element_by_xpath(".//*[@id='addForm']/div[3]/input").click()

  browser.switch_to_default_content()
  iframe = browser.find_elements_by_tag_name('iframe')
  browser.switch_to_frame(iframe[1])
  browser.find_element_by_xpath(".//*[@id='photoForm']/div[5]/input").click()
  browser.quit()


def WebUploadCSV(csvFileName):
  browser = webdriver.Firefox()
  browser.get("http://members.webs.com/sites/99628513/dashboard/settings/fileManager")

  username = browser.find_element_by_name('j_username')
  password = browser.find_element_by_name('j_password')

  username.send_keys('cfausn@gmail.com')
  password.send_keys('*****')

  password.send_keys(Keys.RETURN)

  

  browser.find_element_by_xpath(".//*[@id='tabs']/div[2]/div/div/div[3]/div[1]/div[3]/div[1]/div/div/img").click()

  #Delete old file if there is one
  if csvFileName in browser.page_source:
    oldElm = None
    lst = browser.find_elements_by_xpath(".//*[@id='tabs']/div[2]/div/div/div[3]")
    for rowElm in lst:
      for row in rowElm.find_elements_by_xpath(".//*"):
        if 'Delete File' in row.get_attribute("title"): oldElm = row
        elif '02016-05-26.csv' in row.get_attribute("title"): break
		      
    browser.execute_script("$(arguments[0]).click();",oldElm)
    lst = browser.find_elements_by_xpath(".//*[@id='tabs']/div[2]/div/div/div[3]")
    
    for rowElm in lst:
      for row in rowElm.find_elements_by_xpath(".//*"):
          if 'confirm' in row.get_attribute("class"):
            browser.execute_script("$(arguments[0]).click();",row)
            break

          
  browser.find_element_by_xpath(".//*[@id='tabs']/div[2]/div/div/header/div/div/input").click()

  time.sleep(2)
  wsh = comclt.Dispatch("WScript.Shell")
  
  wsh.SendKeys("C:\\DSlrRemote\\" + "0" + time.strftime("%Y-%m-%d") )
  time.sleep(2)
  wsh.SendKeys("~") #enter key
  browser.quit()

def WebUploadOldAlbum(csvFileName, filenameString):
  browser = webdriver.Firefox()
  browser.get("http://members.webs.com/MembersB/editAppPage.jsp?app=photos&pageID=278815598#photos/")


  username = browser.find_element_by_name('j_username')
  password = browser.find_element_by_name('j_password')

  username.send_keys('cfausn@gmail.com')
  password.send_keys('*****')

  password.send_keys(Keys.RETURN)


  iframe = browser.find_elements_by_tag_name('iframe')
  browser.switch_to_frame(iframe[1])

  elm = browser.find_element_by_xpath(".//*[@id='webs-bin-null']/div/div/h3/div/div[1]/span[1]/a")
  elm.click()

  browser.find_element_by_xpath(".//*[@id='cui_select_id']/div/a").click()

  elementNeeded = None

  file = open(csvFileName, 'r')
  albName = (file.readline().replace(",","").replace("-"," ") +" "
             + time.strftime("%m").lstrip("0") + "/" + time.strftime("%d").lstrip("0")
             + "/" +time.strftime("%Y"))
  
  file.close()


  lst = browser.find_element_by_xpath(".//*[@id='cui_select_id']/ul")
  
  for child in lst.find_elements_by_xpath(".//*"):
    if "..." in child.text:
      if child.text.replace("...","") in "Test Album 5/26/2016":
        child.click()
        break
    elif child.text in "Test Album 5/26/2016":
      child.click()
      break


  browser.find_element_by_xpath(".//*[@id='existing1']").click()
  
  iframe = browser.find_elements_by_tag_name('iframe')
  browser.switch_to_frame(iframe[0])
  browser.find_element_by_xpath("html/body/div[1]/label").click()

  time.sleep(2)
  wsh = comclt.Dispatch("WScript.Shell")
  
  wsh.SendKeys("C:\\DSlrRemote\\" + time.strftime("%Y-%m-%d") + "\\prints\\" + filenameString)
  time.sleep(2)
  wsh.SendKeys("~") #enter key

  browser.switch_to_default_content()
  iframe = browser.find_elements_by_tag_name('iframe')
  browser.switch_to_frame(iframe[1])
  browser.find_element_by_xpath(".//*[@id='addForm']/div[3]/input").click()

  browser.switch_to_default_content()
  iframe = browser.find_elements_by_tag_name('iframe')
  browser.switch_to_frame(iframe[1])
  browser.find_element_by_xpath(".//*[@id='photoForm']/div[5]/input").click()
  browser.quit()
  
     

class Dialog: 
  def __init__(self, parent):
    top = self.top = tkinter.Toplevel(parent)

    tkinter.Label(top, text="Name Album")

    self.e = tkinter.Entry(top)
    self.e.pack(padx=5)
    self.albumName = ""
    self.albumNameString = ""

    b = tkinter.Button(top, text="OK", command=self.ok)
    b.pack(pady=5)

  def ok(self):
    albumName = self.e.get().strip()
    albumNameString = albumName

    self.albumName = albumName.replace(" ","-")
    self.top.destroy()





if __name__ == "__main__":
  main()
