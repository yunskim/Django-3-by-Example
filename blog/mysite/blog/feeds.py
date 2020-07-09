from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):

    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)

    '''
    When the URL resolver is being initialised, 
    it imports your URL configuration, which in turn imports your views. 
    So at the time your view is imported and success_url is set, 
    the resolver is only halfway through its initialisation. 
    Calling reverse() at this point would not work 
    since the resolver doesn't have all the information yet to reverse the view name.
    '''
