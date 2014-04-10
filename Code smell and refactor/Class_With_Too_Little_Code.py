# This is the class with too little code
# We should either take it out of the class if it has only one method
# Or refactor it to make a meaningful class with some functions

class LoginPageView(self):
	def view(request):
		user = login(request.username, request.password)
		if user is None:
			return HttpResponse("<h3>Invalid Login<h3>")
		else:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))