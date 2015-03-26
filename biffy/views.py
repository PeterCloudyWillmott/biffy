from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

# Renders work area, hands over list of b1if servers
def userlogin(request):
	context = {'message':'','error':False}
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            return redirect('/')
	        else:
	            context.message = 'No Login for you! Inactive User'
	    else:
	            context.message = 'No Login for you! Incorrect Login/Password'

	return render(request, 'biffy/login.html',context)

def userlogout(request):
    logout(request)
    return redirect('/accounts/login/')