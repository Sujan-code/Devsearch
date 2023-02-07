from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer,ProfileSerializer
from projects.models import Project
from users.models import Profile
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
#from rest_framework import viewsets

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/developers'},
        {'GET': '/api/developer/id'},
        {'GET': '/api/Projects'},
        {'GET': '/api/project/id'},
        {'POST': '/api/developers'},
        {'PUT': '/api/developer/id'},
        {'DELETE': '/api/developer/id'},
        {'POST': '/api/projects'},
        {'PUT': '/api/project/id'},
        {'DELETE': '/api/project/id'}

   ]
    return Response(routes)

class ProfileLC(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','email']
    ordering_fields=['name']
    pagination_class= PageNumberPagination

class ProfileRUD(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','email']
    ordering_fields=['name']
    pagination_class= PageNumberPagination



class ProjectLC(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields= ['title','owner']
    pagination_class= PageNumberPagination

class ProjectRUD(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','email']
    ordering_fields=['name']
    pagination_class= PageNumberPagination
    

# @api_view(['POST'])
# def createprofile(request):
#  if request.method == 'POST':
#     serializer = ProfileSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data,status=status.HTTP_201_CREATED)
    

  

# @api_view(['GET'])
# def getProfile(request, pk):
#     post = Profile.objects.get(id=pk)
#     serializer = ProfileSerializer(post, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def createproject(request):
#  if request.method == 'POST':
#     serializer = ProjectSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data,status=status.HTTP_201_CREATED)
    

  

# @api_view(['GET'])
# def getProject(request, pk):
#     post = Project.objects.get(id=pk)
#     serializer = ProjectSerializer(post, many=False)
#     return Response(serializer.data)



# @api_view(['PUT'])
# def updateProfile(request,pk):
#     post = Profile.objects.get(id=pk)
#     serializer = ProfileSerializer(instance=post,data=request.data, partial=True)
#     if serializer.is_valid():
#        serializer.save()
#     return Response(serializer.data)
    
# @api_view(['PUT'])
# def updateProject(request,pk):
#     post = Project.objects.get(id=pk)
#     serializer = ProjectSerializer(instance=post,data=request.data, partial=True)
#     if serializer.is_valid():
#        serializer.save()
#     return Response(serializer.data)    
    
        


#class ProfileModeViewset(viewsets.ModelViewSet):
    #queryset = Profile.objects.all()
    #serializer_class = ProfileSerializer

#class ProjectModeViewset(viewsets.ModelViewSet):  
   # queryset = Project.objects.all()
    #serializer_class = ProjectSerializer
    
   

