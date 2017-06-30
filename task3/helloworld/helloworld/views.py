#from django.shortcuts import render_to_response

#def index(request):
    #return render_to_response('siteTutorial.html')

from django.http import HttpResponse
from django.template import Context, loader


#def css(request):
    #filename = request.path.strip("/siteStyle.css")
    #data = open(filename, "rb").read()
#    return HttpsResponse(data, mimetype="text/css")



def index(request):
    template = loader.get_template("siteTutorial.html")
    return HttpResponse(template.render())
