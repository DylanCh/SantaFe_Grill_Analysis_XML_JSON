import xmltodict
import json
import webbrowser
import testXML

def run():
    xmlSource = raw_input("Export your SPSS data to XML. Press Y+return when done, press H+return for help\n")
    testXmlDoc = testXML.TEST_XML_STRING
    
    if (xmlSource.lower() is 'y') or xmlSource.lower()== 'y' :
        parse(testXmlDoc)
    elif xmlSource.lower() is 'h' or xmlSource.lower()=='h' :
        exportOptions = raw_input('Export using SPSS Add-on - 1 \nExport using SPSS and Excel - 2 \n')
        if exportOptions is '1':
            webbrowser.open('https://www.ibm.com/support/knowledgecenter/SSLVQG_7.0.0/com.spss.ddl/xml_export.htm')
        elif exportOptions is '2':
            webbrowser.open('https://support.office.com/en-us/article/Export-XML-data-0b21f51b-56d6-48f0-83d9-a89637cd4360')
    else: 
        print('Thank you for using XMLParser')
        
def parse(xmlDoc):
    # xmlDoc = raw_input('Copy the the <Table> tags and the content within, paste here and press return')
    try:
        o = xmltodict.parse(xmlDoc)
        print(o)
        exportJSON('data.json',o)
    except xmltodict.expat.ExpatError as expatErr:
        print('Parse XML failed, expat error ')
        exportJSON('data.json','{\"error\":\"'+str(expatErr)+'"\}')
    except IOError as ioErr:
        print('can\'t write to file')
        exportJSON('data.json','{\"error\":\"'+str(ioErr)+'"\}')

def exportJSON(fileName,o):
    with open(fileName, 'w') as outfile:
        try:
            json.dumps(o,outfile)
        except Exception as jsonErr:
            print('Cannot output JSON')