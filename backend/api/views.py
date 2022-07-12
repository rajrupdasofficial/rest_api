from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

""" # from django.shortcuts import render
# import json
# from django.http import JsonResponse,HttpResponse
# import logging
#from products.models import Product
# from django.forms.models import model_to_dict
# Create your views here.
# logger=logging.getLogger()
# logger.setLevel(logging.INFO)
# def api_home(request, *args,**kwargs):
    # print (request.GET) #always output an URL query parameters
    # print (request.POST) #always output an URL query parameters for post request `
    # body=request.body
    # data={}
   # try:
     #   data=json.loads(body)
   # except:
    #    pass
  #  print(data)
    # print(data.keys())
    # logger.info(data)
    # data['headers']=request.headers #header types
   # data['params']=dict(request.GET)
   # data['headers']=dict(request.headers)
   # data['content_type']=request.content_type #content type
#    return JsonResponse(data)
        # data['id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.price
        # data=model_to_dict(model_data,fields=['id','title'])
        # json_data_str=json.dumps(data)
    # return JsonResponse(data)
    # return HttpResponse(json_data_str,headers={"content-type":"application/json"})"""


"""proper DRF view
# @api_view(["GET"])
# def api_home(request,*args,**kwargs):
    # if request.method!="POST":
     #   return Response({"details":"method 'GET' is not allowed"}, status=405)
 #   instance=Product.objects.all().order_by("?").first()
  #  data={}
   # if instance:
        # data=model_to_dict(model_data,fields=['id','title','price','sale_price'])
 #       data=ProductSerializer(instance).data
#    return Response(data) """


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """ DRF api view POST method"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
