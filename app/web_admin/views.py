from django.views.generic import CreateView

from web_admin.forms import NewCreateForm


class CreateNew(CreateView):
    form_class = NewCreateForm
    template_name = 'web_admin/create_new.html'
    success_url = '/'

'''
def create_new(request):
    news = New.objects.all()
    if request.method == 'POST':
        form = NewCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NewCreateForm()
    context = {'form': form, 'news': news}
    return render(request, 'web_admin/create_new.html', context)
'''