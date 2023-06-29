from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission, DjangoModelPermissions, AllowAny
from blog.models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import filters


class PostUserWritePermission(BasePermission):
    message = 'Editing is restricted to the author only!'

    def has_object_permission(self, request, view, obj):
        # shortcut saying that the method is GET/OPTIONS/... that won't edit
        if request.method in permissions.SAFE_METHODS:
            return True

        # the editor is the author
        return obj.author == request.user
        # if obj.author == request.user:
        #     return True


# # -----------------------using ModalViewSet--------------------------
# class PostList(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     permission_classes = [AllowAny]
#     serializer_class = PostSerializer
#
#     # queryset = Post.postobjects.all()
#
#     # overwrite the queryset, customize the set
#     def get_queryset(self):
#         return Post.objects.all()
#
#     # get single post via the slug after /
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')  # capture the url parameter
#         return get_object_or_404(Post, slug=item)

# -----------------------using basic ViewSet--------------------------
# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#
#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)  # get pk from url
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


# -----------------------using generics & filter--------------------------
class PostList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


class PostListDetailFilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search
    # '$' Regex search
    search_fields = ['$title', '$excerpt', '$content']


class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def post(self, request, format=None):
    #     print(request.data)
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
