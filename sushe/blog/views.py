from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag
import markdown
import re
# 美化markdown设置锚点的值
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

# 分页API
from pure_pagination.mixins import PaginationMixin

# from users.models import User

# 通用视图类,ListView为获取模型列表， DetailView为获取模型的一条记录数据
from django.views.generic import ListView, DetailView

from django.db.models import Q

# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

# ListView通用类视图功能：获取数据库中某个模型列表数据
class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 4


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     # 阅读量 +1
#     post.increase_views()
#
#     md = markdown.Markdown(extensions=[
#                                       'markdown.extensions.extra',  # 基础扩展
#                                       'markdown.extensions.codehilite',  # 语法高亮
#                                       # 'markdown.extensions.toc',  # 自动生成目录
#                                        TocExtension(slugify=slugify),
#                                   ])
#     post.body = md.convert(post.body)
#
#     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
#     post.toc = m.group(1) if m is not None else ''
#
#     return render(request, 'blog/detail.html', context={'post': post})

def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            # 记得在顶部引入 TocExtension 和 slugify
            TocExtension(slugify=slugify),
        ])
        post.body = md.convert(post.body)

        m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
        post._toc = m.group(1) if m is not None else ''

        return post


class ArchiveView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(created_time__year=year, created_time__month=month)


# def category(request, pk):
#     # 记得在开始部分导入 Category 类
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

class CategoryView(IndexView):
    # get_queryset方法默认是获取指定模型的全部列表数据，现在覆写为获取指定id的文章
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


# def tag(request, pk):
#     # 记得在开始部分导入 Tag 类
#     t = get_object_or_404(Tag, pk=pk)
#     post_list = Post.objects.filter(tags=t).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

class TagView(IndexView):
    def get_queryset(self):
        t = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView,self).get_queryset().filter(tags=t)

def about(request):
    return render(request, 'blog/about.html')

def context(request):
    return render(request, 'blog/context.html')


from django.contrib import messages
def search(request):
    q = request.GET.get('q')

    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'post_list': post_list})

