from django.shortcuts import render
from django.http import JsonResponse
from floweditor.models import B1if
#import pkg_resources
#pkg_resources.require("easywebdav==p1.2.0")
from easywebdavbiffy import *
import xmltodict

def index(request):
	b1if_servers = B1if.objects.order_by('server')
	connectstring = 'unconnected'

	if request.method == 'POST':
		connectstring = 'connected'

	context = {
		'b1if_servers': b1if_servers,
		'connectstring': connectstring,
    }
	return render(request, 'floweditor/workarea.html', context)

def getScenarios(request):
	#b1if_server = B1if.objects.get(id=request.POST['server'])
	b1if_server = B1if.objects.get(id=1)
	webdav = ewdconnect(b1if_server.server, port=b1if_server.port, username=b1if_server.user, password=b1if_server.password)
	folders = webdav.ls(b1if_server.path)
	scenarios = []
	for f in folders:
		fname = f.name.rsplit('/')[-1]
		if 'vPac.' in fname and fname != 'vPac.' and not 'vPac.sap.' in fname:
			scenarios.append(fname)
	return JsonResponse({'scenarios':scenarios,'path':b1if_server.path})

def getScenarioFiles(request):
	b1if_server = B1if.objects.get(id=request.POST['server'])
	webdav = easywebdav.connect(b1if_server.server, port=b1if_server.port, username=b1if_server.user, password=b1if_server.password)
	path = b1if_server.path+request.POST['scenario']+'/vPac.xml'
	file_contents = webdav.read(path)
	flows = []
	doc = xmltodict.parse(file_contents)
	#print doc['vPac']['vBIUList']
	for vbiu in doc['vPac']['vBIUList']['vBIU']:
		print vbiu
		flows.append(vbiu['@Id'])
	return JsonResponse({'flows':flows,'path':b1if_server.path,})

def getFlowFiles(request):
	b1if_server = B1if.objects.get(id=request.POST['server'])
	webdav = easywebdav.connect(b1if_server.server, port=b1if_server.port, username=b1if_server.user, password=b1if_server.password)
	path = b1if_server.path+'vBIU.'+request.POST['flow']
	folders = webdav.ls(path)
	files = []
	for f in folders:
		fname = f.name.rsplit('/')[-1]
		files.append(fname)
	return JsonResponse({'files':files,'path':path})

def getFlowFileContent(request):
	b1if_server = B1if.objects.get(id=request.POST['server'])
	webdav = easywebdav.connect(b1if_server.server, port=b1if_server.port, username=b1if_server.user, password=b1if_server.password)
	path = b1if_server.path+'vBIU.'+request.POST['flow']+'/'+request.POST['file']
	file_content = webdav.read(path)
	return JsonResponse({'file_content':file_content,'path':path})