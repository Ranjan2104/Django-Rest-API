from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializers
from .models import Todo
@api_view(['GET'])
def getApi(request):
    get_post = Todo.objects.all()
    filterData = TodoSerializers(get_post, many=True)
    return Response({
        'status': 'success',
        'status_code': 200,
        'data': filterData.data,
    })

@api_view(['POST'])
def postApi(request):
    data = request.data
    req_data = TodoSerializers(data=data)
    if req_data.is_valid():
        req_data.save()
        return Response({
            'status': True,
            'status_code': 201,
            'message': "Data Added Successfully!",
        })
    else:
        return Response({
            'status': False,
            'status_code': 400,
            'message': req_data.errors,
        })

@api_view(['POST'])
def deleteApi(request):
    param_value = request.GET.get('id', '')
    getData = Todo.objects.get(id=param_value)
    getData.delete()
    return Response({
        'status': 'success', 
        'status_code': 200, 
        'messgae': 'Data Deleted Successfully'
    })
