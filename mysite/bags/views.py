from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

from .models import Bags, Category
from .forms import BagsForm, UserRegisterForm, UserLoginForm, ContactForm
from .utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Реєстрація пройшла успішно')
            return redirect('home')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = UserRegisterForm()

    return render(request, 'bags/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Помилка авторизації')
    else:
        form = UserLoginForm()
    return render(request, 'bags/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('user_login')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],
                      form.cleaned_data['content'],
                      'from',
                      ['to'],
                      fail_silently=False
                      )
            if mail:
                messages.success(request, 'Листа надіслано')
                return redirect('contact_us')
            else:
                messages.error(request, 'Листа НЕ надіслано')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = ContactForm()
    return render(request, 'bags/mailtest.html', {'form': form})



def pagitest(request):
    objects = ['Kyrylo', 'Vasylyna', 'Vladyslava', 'Kyrylo2', 'Vasylyna2', 'Vladyslava2', 'Kyrylo3', 'Vasylyna3',
               'Vladyslava3']
    paginator = Paginator(objects, 3)
    page_num = request.GET.get('page', 1)  # 1 це параметр за замовчуваннямб якщо немає в запиті пейдж(/page=...)
    page_objects = paginator.get_page(page_num)
    return render(request, 'bags/pagitest.html', {'page_obj': page_objects})


class HomeBags(MyMixin, ListView):
    model = Bags
    template_name = 'bags/home_bags_list.html'  # якщо не вказати створить дефолтний шаблон
    context_object_name = 'bags'  # це просто назва для обджектліст
    # extra_context = {'title': 'LIMA LIMA'} #краще використовувати лише для статичних штук, тайтл підходить
    mixin_prop = 'hi Ukraine'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):  # objectlist можна видлити
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('lima lima')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return Bags.objects.filter(is_published=True).select_related(
            'category')  # !!! лише з галочкою статус публікації(where в sql)


class BagsByCategory(MyMixin, ListView):
    model = Bags
    template_name = 'bags/home_bags_list.html'
    context_object_name = 'bags'
    allow_empty = False

    def get_queryset(self):
        return Bags.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context


class ViewBag(DetailView):
    model = Bags
    # pk_url_kwarg = 'bags_id'
    # template_name = 'bags/bags_detail.html'
    context_object_name = 'bags_item'


class CreateBag(LoginRequiredMixin, CreateView):
    form_class = BagsForm
    template_name = 'bags/add_bag.html'
    raise_exception = True
    # замість редірект він дивиться в мейк абсолютюрл або:
    # success_url = reverse_lazy('home')
    # login_url = '/admin/'
    # raise_exception = True щоб якщо хтось захоче додати сумочку -прмилка доступу 403


# def index(request):
#     bags = Bags.objects.all()  # order_by('-added_at') не потрібен тому що у models.Bags.Meta.ordering є
#     context = {
#         'bags': bags,
#         'title': 'Асортимент сумочек'
#
#     }
#     return render(request, template_name='bags/index.html', context=context)


# def get_category(request, category_id):
#     bags = Bags.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'bags/category.html', {'bags': bags, 'category': category})

#
# def view_bag(request, bags_id):
#     # bags_item = Bags.objects.get(pk=bags_id)
#     bags_item = get_object_or_404(Bags, pk=bags_id)
#     return render(request, "bags/view_bag.html", {'bags_item': bags_item})


# def add_bag(request):
#     if request.method == 'POST':
#         form = BagsForm(request.POST)
#         if form.is_valid():
#             #bag=Bags.objects.create(**form.cleaned_data) не повяз з мод
#             #title = form.cleaned_data[title]... кожен окремо
#             bag = form.save()
#             return redirect(bag)
#     else:
#         form = BagsForm()
#
#     return render(request, 'bags/add_bag.html', {'form': form})
