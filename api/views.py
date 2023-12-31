from django.shortcuts import render

# Create your views here.



from rest_framework import viewsets
from .models import Member, Membership
from .serializers import MemberSerializer, MembershipSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import Member, Membership
# from .serializers import MemberSerializer, MembershipSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer



# @api_view(['GET', 'POST'])
# def member_list(request):
#     if request.method == 'GET':
#         members = Member.objects.all()
#         serializer = MemberSerializer(members, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MemberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def member_detail(request, pk):
#     try:
#         member = Member.objects.get(pk=pk)
#     except Member.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MemberSerializer(member)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MemberSerializer(member, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         member.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

