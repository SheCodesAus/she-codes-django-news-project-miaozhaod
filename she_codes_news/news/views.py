from django.views import generic
from .models import NewsStory
from django.urls import reverse_lazy
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = "news/index.html"

    def get_queryset(self):
        """Return all news stories."""
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_stories"] = NewsStory.objects.all()[:4]
        context["all_stories"] = NewsStory.objects.all()
        context["stories_by_date"] = NewsStory.objects.all().order_by("-pub_date")
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = "story"


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = "storyForm"
    template_name = "news/createStory.html"
    success_url = reverse_lazy("news:index")

    # overriding form_valid which is on generic.CreateView
    def form_valid(self, form):
        # to set author to the  user logged in
        form.instance.author = self.request.user
        # call the form_valid on generic.CreateVie
        return super().form_valid(form)

class storiesByDateView(generic.ListView):
    template_name = "news/storiesByDate.html"

    def get_queryset(self):
        """Return all news stories."""
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stories_by_date"] = NewsStory.objects.all().order_by("-pub_date")
        return context

class storiesByAuthorView(generic.ListView):
    template_name = "news/storiesByAuthor.html"

    def get_queryset(self):
        """Return all news stories."""
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        # author = self.request.GET.get("author")
        author = self.kwargs["author"] # this author refers to the P<author> defined in the url
        print("author", author)
        context = super().get_context_data(**kwargs)
        context["stories_by_author"] = NewsStory.objects.all().filter(author=author)
        return context
