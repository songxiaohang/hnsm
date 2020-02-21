from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown
import re
# 美化markdown设置锚点的值
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',  # 基础扩展
                                      'markdown.extensions.codehilite',  # 语法高亮
                                      # 'markdown.extensions.toc',  # 自动生成目录
        TocExtension(slugify=slugify),
                                  ])
    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


def about(request):
    return render(request, 'blog/about.html')

def context(request):
    return render(request, 'blog/context.html')

