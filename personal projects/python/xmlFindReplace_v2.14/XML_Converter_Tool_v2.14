#!/usr/bin/env python
"""
    XML_Converter_Tool_v2.13.py

    Converts custom time in xml files to hex time

    ***WARNING***

    As of now there is no way to catch illegal entries, make sure the files you choose are not already converted
    and that they are in the correct format.

    CHANGE LOG
    v2.14 : Fixed an issue with the Ensemble not accepting hours, converted to minutes
    v2.13 : Updated to include situations where instead of 'end=', there is 'dur='. 
    v2.12 : Optimized a bit, fixed an issue where a file might have problems replacing the 'end="' numbers
    v2.11 : Had issues when xml files only showed seconds, this version fixes that
    
"""

from xml.dom.minidom import parseString, Document
from xml.dom import minidom 
import HTMLParser
import Tkinter,tkFileDialog
from Tkinter import *
import tkMessageBox
import datetime
import time
import os.path



def headerRemover(files):

    """
        Custom Header
        
        <tt xmlns="http://www.w3.org/2006/10/ttaf1"  xmlns:tts="http://www.w3.org/2006/04/ttaf1#styling" xml:lang="en">
      <body>
           <div xml:lang="en" style="1">
    """
    h = HTMLParser.HTMLParser() #used for the importing of textNodes later on
    dirc = []
    dirc = files[0].split('/')
    runningString = ''
    for elm in dirc:
        if elm == dirc[-1]:
            break
        elif elm != '':
            runningString += '/' + elm

    os.chdir(runningString)
    lengthBegin = len(files)
    x = 0

    while x < lengthBegin:

        fileName = files[x]
        
    
        #Open the document to be changed
        xmldoc = minidom.parse(fileName)
        doc_root = xmldoc.documentElement

        
        #Set up the new document with the custom header
        doc = Document()
        tt = doc.createElement('tt xmlns="http://www.w3.org/2006/10/ttaf1"  xmlns:tts="http://www.w3.org/2006/04/ttaf1#styling" xml:lang="en"')
        doc.appendChild(tt)

        #finish setting up the custom header
        body = doc.createElement('body')
        tt.appendChild(body)
       
        div = doc.createElement('div xml:lang="en" style="1"')
        body.appendChild(div)

    

        #sentinal values, consider optimization later
    
        y = 0
        z = 0.00
    
        length = len(doc_root.getElementsByTagName("p")) #gets the number of the <p> values in the root document


        while y < length:
        
            tag = doc_root.getElementsByTagName("p")[y].toxml()
            
            z = z + 0.01
            convertBegin = 0
            beginNum = 10
            endNum = 0
            colonPadding = ":"
            BEGIN = 10
            lst = []
            
                
            while True:
                
                #Replace time in the "begin" area
                newLst = []
                newLst = tag.split('"')
            

                if ':' in newLst[1] and newLst[2] == ' dur=':
                    beginReplace = tag
                    break
                
                elif tag[beginNum] != 's':
                    beginNum += 1
                else:
                         
                    if tag[BEGIN:beginNum] == "0": #had issues with one of the docs with "0", added to catch errors
                        beginReplace = tag[:BEGIN] + "00:00:00.000" + tag[(beginNum +1):]
                        break
                    convertBegin = float(tag[BEGIN:beginNum])
                    time = datetime.timedelta(seconds=convertBegin)
                    
                    
                    stringTime = str(time)
                    if stringTime[0] != "0":
                        hrsConvert = int(stringTime[0]) * 60
                        hrsConvert += int(stringTime[2:4])
                        tempTime = stringTime[4:]
                        
                        stringTime = "0:" + str(hrsConvert) + tempTime

                   
                    if not "." in tag[BEGIN:beginNum]:
                        
                        beginReplace = tag[:BEGIN] + ("00:0" + stringTime + ".000") + tag[(beginNum+1):]
                        break
                        
                    elif (convertBegin % 2) == 0 and tag[BEGIN:beginNum] != "0":
                        beginReplace = tag[:BEGIN] + (stringTime[:1] + stringTime[:11]) + ".000" + tag[(beginNum +1):]
                        break
                    
                    beginReplace = tag[:BEGIN] + (stringTime[:1] + stringTime[:11]) + tag[(beginNum +1):]
                    break

            while True:

                if ':' in newLst[1] and newLst[2] == ' dur=':
                    #convertBegin = float(newLst[1])
                    time = datetime.datetime.strptime(newLst[1],'%H:%M:%S.%f')
                    addTime = datetime.datetime.strptime(newLst[3],'%H:%M:%S.%f')
                    addThis = float(addTime.strftime('%S.%f'))

                    time = time + datetime.timedelta(seconds=addThis)
                    

                    stringTime = str(time)
                    if stringTime[0] != "0":
                        hrsConvert = int(stringTime[0]) * 60
                        hrsConvert += int(stringTime[2:4])
                        tempTime = stringTime[4:]
                        
                        stringTime = "0:" + str(hrsConvert) + tempTime

                    endReplace = beginReplace[:21] + '0" end="' + stringTime[11:23] + beginReplace[39:]
                    break
                else:
                    lst = beginReplace.split('end="')
                #Replace time in the "end" area
                if lst[1][endNum] != 's':
                    endNum += 1
                else:
                                            
                    if float(lst[1][:endNum]) == 0: #had issues with one of the docs with "0", added to catch errors
                        endReplace = lst[0] + "00:00:00.000" + lst[1][1:]
                        break
                    
                    convertEnd = float(lst[1][:endNum])
                    time = datetime.timedelta(seconds=convertEnd)
                    stringTime = str(time)
                    if stringTime[0] != "0":
                        hrsConvert = int(stringTime[0]) * 60
                        hrsConvert += int(stringTime[2:4])
                        tempTime = stringTime[4:]
                        
                        stringTime = "0:" + str(hrsConvert) + tempTime


                    if not "." in stringTime:
                        endReplace = lst[0] + 'end="' + ("00:0" + stringTime + ".000") + lst[1][(endNum+1):]
                        break
                    
                    if (convertEnd % 2) == 0 and beginReplace[29:endNum] != "0":
                        endReplace = lst[0] + 'end="' +  (stringTime[:1] + stringTime[:11])+ ".000" + lst[1][(endNum +1):]
                        break
                    
                    endReplace = lst[0] + 'end="' + (stringTime[:1] + stringTime[:11]) + lst[1][(endNum +1):]
                    break
    
            replaceData = h.unescape(endReplace)
            addData = doc.createTextNode(replaceData)
            div.appendChild(addData)
            y +=1
            
        tempList = []
        
        tempList = fileName.split('/')
        newpath = (str(os.getcwd()) + '/ConvertedFiles/')
        
        if not os.path.exists(newpath): os.makedirs(newpath)
        
        newFileName = str(newpath + "C_" + tempList[-1])
        file_handle = open(newFileName, 'w')
        #file_handle = open("%s%s_C.xml"%str(os.getcwd) %fileName,"w")
        file_handle.write(h.unescape(doc.toprettyxml(encoding='UTF-8'))) #It's important to use h.unescape here or else the document will have issues.
        file_handle.close()
        x +=  1
        
    showComplete()
    
    
    
def GUI():
    global root
    root = Tk()
    #f = Frame(root, height = 25, width = 200)
    root.title("XML Converter")
    #f.pack_propagate(0)
    #f.pack()
    
    #make my screen dimensions work
    w = 375 #The value of the width
    h = 175 #The value of the height of the window

    # get screen width and height
    ws = root.winfo_screenwidth()#This value is the width of the screen
    hs = root.winfo_screenheight()#This is the height of the screen

    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    #This is responsible for setting the dimensions of the screen and where it is
    #placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    w = Label(root, text="XML Converting Tool v2.14: Raw Caption Conversion",
                    font = "Verdana 13 bold").pack()

    
    i = Label(root, text="Used for converting original caption ",
                    font = "Verdana 11").pack()
    
    i2 = Label(root, text="files to a format ensemble can use.",
                    font = "Verdana 11").pack()
    
    b = Button(root, text="Exit", width=25, command=lambda:exitProgram())
    b2 = Button(root, text="Open Files", width=25, command=lambda:openDialog())
    b2.pack()
    b.pack()
    
    warning = Label(root, text="WARNING: Do not select already-converted",
                    font = "Verdana 8").pack()
    
    warning2 = Label(root, text="files or the program will crash! Working on a fix.",
                    font = "Verdana 8").pack()
    mainloop()
    

def exitProgram():
    print "Press cmd + W to exit the window!"
    quit()

def openDialog():
    files = tkFileDialog.askopenfilenames(parent=root,title='Choose files')
    finishedDialog(files)

def finishedDialog(files):
    if len(files) > 0:
        headerRemover(files)
    else:
        pass

def showComplete():
    tkMessageBox.showinfo("Done Converting", "Finished!")
    
def main():
    GUI()

#Call main()   
main()
