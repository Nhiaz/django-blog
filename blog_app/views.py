from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.decorators.http import require_POST

from .models import Post
from .forms import EmailPostForm, CommentForm
from decouple import config



class PostListView(ListView):
    """
    Альтернативное представления списка постов
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog_app/post/list.html'

def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog_app/post/list.html',
                  {
                      'posts': posts
                   }
                  )

def post_detail(request, year,month,day,post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    #Список активных комментариев к посту
    comments = post.comments.filter(active=True)
    #Форма для ввода комментария
    form = CommentForm()


    return render(request,
                  'blog_app/post/detail.html',
                  {
                      'post': post,
                      'comments': comments,
                      'form': form
                   }
                  )

def post_list(request):
    all_posts = Post.published.all()
    #Постраничная разбивка с 3 постами на странице
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # Если page_number находится вне диапазона, то
        # выдать последнюю страницу
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render(request,
                  'blog_app/post/list.html',
                  {
                      'posts': posts
                   }
                  )

def post_share(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )

    sent = False

    if request.method == 'POST':
        #Форма была переданна в обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #Поля формы успешно прошли валидацию
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = (
                f'{cd['name']} рекомендация для прочтения '
                f'{post.title}'
            )
            message = (
                f'Прочитай {post.title} здесь: {post_url}\n\n'
                f'{cd['name']} комментарий к посту:: {cd["comments"]}\n'
            )
            send_mail(
                subject,
                message,
                config('EMAIL_HOST_USER'),
                [cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(
         request,
         'blog_app/post/share.html',
         {
             'post': post,
             'form': form,
             'sent': sent
         }
     )

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    comment = None
    #Комментарий был отправлен
    form = CommentForm(data = request.POST)
    if form.is_valid():
        #Создаём объект класса Comment, но пока не сохраняем в БД
        comment = form.save(commit=False)
        #Привязываем комментарий к текущему посту
        comment.post = post
        #Сохраняем комментарий в БД
        comment.save()
    return render(
        request,
        'blog_app/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment,
        }
    )