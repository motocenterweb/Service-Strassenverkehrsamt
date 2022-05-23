from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Bill
from api.jwt import encode_token
from ..serializers import BillSerializer


@api_view(["GET"])
def get_all_bills(request):
    bills = Bill.objects.all()
    serializer = BillSerializer(bills, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_bill(request):
    if "accesToken" not in request.META.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.META["accessToken"])
    if not jwt.verify(payload["expireDate"]):
        return Response(status=401) 
    serializer = BillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["GET"])
def get_bill_by_id(request, id):
    try:
        bill = Bill.objects.get(pk=id)
    except Bill.DoesNotExist:
        return Response(status=404)    
    serializer = BillSerializer(bill, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_bill_by_user(request):
    if "accesToken" not in request.META.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.META["accessToken"])
    if not jwt.verify(payload["expireDate"]):
        return Response(status=401) 
    try:
        bills = Bill.objects.filter(receiver=payload["email"])    
    except Bill.DoesNotExist:
        return Response(status=404)        
    serializer = BillSerializer(bills, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_bill_by_id(request, id):
    if "accesToken" not in request.META.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.META["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
    try:
        bill = Bill.objects.get(pk=id)    
        if bill.receiver != payload["email"]:
           return Response(status=401) 
    except Bill.DoesNotExist:
        return Response(status=404)   
    bill.delete()
    return Response(status=200)