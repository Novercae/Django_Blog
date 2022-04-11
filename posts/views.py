from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Count, Q, Case, When
from comments.forms import CommentForm
from comments.models import Comment
from django.contrib import messages


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related( 'category_post')
        qs = qs.order_by('-id').filter(published_post=True)
        qs = qs.annotate(
            num_comments=Count(
                Case(
                When(comment__published_comment=True, then=1),
                )
            )
        )
        return qs


class PostSearch(PostIndex):
    template_name = 'posts/post_search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        term = self.request.GET.get('term', None)

        qs = qs.filter(
                Q(title_post__icontains=term) |
                Q(content_post__icontains=term) |
                Q(category_post__name_cat__icontains=term) |
                Q(author_post__first_name__icontains=term) |
                Q(author_post__username__icontains=term) |
                Q(excerpt_post__icontains=term)
                )
        return qs
             

class PostCategory(PostIndex):
    template_name = 'posts/post_category.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        category = self.kwargs.get('category', None)
        
        if not category:
            return qs

        qs = qs.filter(category_post__name_cat__iexact=category)
        return qs

class PostDetail(UpdateView):
    template_name = 'posts/post_detail.html'
    model = Post
    form_class = CommentForm
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comment = Comment.objects.filter(published_comment=True, post_comment=post.id)
        context['comment'] = comment
        return context

    def form_valid(self, form):
        post = self.get_object()
        comment = Comment(**form.cleaned_data)
        comment.post_comment = post
        
        if self.request.user.is_authenticated:
            comment.user_comment = self.request.user

        comment.save()
        messages.success(self.request, 'Comment added successfully.')
        return redirect('post_detail', pk=post.id)
