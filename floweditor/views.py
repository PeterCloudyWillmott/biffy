from django.shortcuts import render
from django.http import JsonResponse
from floweditor.models import B1if
from easywebdavbiffy import *
import xmltodict
import StringIO

# Renders work area, hands over list of b1if servers
def index(request):
	b1if_servers = B1if.objects.order_by('server')

	context = {
		'b1if_servers': b1if_servers
    }
	return render(request, 'floweditor/workarea.html', context)

# Gets a list of scenarios - .vPac is the content for un-assigned flows
def getScenarios(request):
	#b1if_server = B1if.objects.get(id=request.POST['server'])
	b1if_server = B1if.objects.get(id=1)
	webdav = ewdconnect(b1if_server.server, port=b1if_server.port, username=b1if_server.user, password=b1if_server.password)
	folders = webdav.ls(b1if_server.path)
	scenarios = []
	for f in folders:
		fname = f.name.rsplit('/')[-1]
		# Folders starting with vPac. are scenarios, don't include SAP generated scenarios
		if 'vPac.' in fname and not 'vPac.sap.' in fname:
			scenarios.append(fname)
	return JsonResponse({'scenarios':scenarios,'path':b1if_server.path})

# JSON Returns a list of flows for a scenario - read from the vBIU list in the scenario vPac file
def getScenarioFlows(request):
	b1if_server = B1if.objects.get(id=request.POST['server'])
	webdav = ewdconnect(b1if_server.server, port=b1if_server.port, username=b1if_server.user, password=b1if_server.password)
	path = b1if_server.path+request.POST['scenario']+'/vPac.xml'
	virtual_file = StringIO.StringIO()
	webdav.download(path,virtual_file)
	file_contents = virtual_file.getvalue()
	flows = []
	doc = xmltodict.parse(file_contents)
	#print doc['vPac']['vBIUList']
	for vbiu in doc['vPac']['vBIUList']['vBIU']:
		flows.append(vbiu['@Id'])
	return JsonResponse({'flows':flows,'path':b1if_server.path,})

# JSON Returns a list of files for a scenario flow
def getFlowFiles(request):
	b1if_server = B1if.objects.get(id=request.POST['server'])
	webdav = ewdconnect(b1if_server.server, port=b1if_server.port, username=b1if_server.user, password=b1if_server.password)
	path = b1if_server.path+'vBIU.'+request.POST['flow']
	folders = webdav.ls(path)
	files = []
	for f in folders:
		fname = f.name.rsplit('/')[-1]
		files.append(fname)
	return JsonResponse({'files':files,'path':path})

# JSON Returns a files content
def getFlowFileContent(request):
	b1if_server = B1if.objects.get(id=request.POST['server'])
	webdav = ewdconnect(b1if_server.server, port=b1if_server.port, username=b1if_server.user, password=b1if_server.password)
	path = b1if_server.path+'vBIU.'+request.POST['flow']+'/'+request.POST['file']
	virtual_file = StringIO.StringIO()
	webdav.download(path,virtual_file)
	return JsonResponse({'file_content':virtual_file.getvalue(),'path':path})


# JSON Saves a files content - returns True/False
# Writes the new file to .floweditor.xml (pro tip, the webdav server will Base64 encode
# your file if it doesn't end in .xml or .xsl)
# Will bails if the upload fails instead of overwriting the  old file
# with a blank new file (severely painful past experience here)
# Deletes the old file and moves the new file to the old name
# Deletes old move files first
def saveFlowFileContent(request):
	b1if_server = B1if.objects.get(id=request.POST['server'])
	webdav = ewdconnect(b1if_server.server, port=b1if_server.port, username=b1if_server.user, password=b1if_server.password)
	path = b1if_server.path+'vBIU.'+request.POST['flow']+'/'+request.POST['file']
	temp_path = b1if_server.path+'vBIU.'+request.POST['flow']+'/floweditor.'+request.POST['file']
	new_file_content = request.POST['file_content']

	if webdav.exists(temp_path)==True:
		webdav.delete(temp_path)

	virtual_file = StringIO.StringIO()
	virtual_file.write(new_file_content)

	webdav.upload(virtual_file,temp_path)
	response = False
	if webdav.exists(temp_path)==True:
		webdav.delete(path)
		webdav.move(temp_path,path)
		response = True
	return JsonResponse({'success':response})