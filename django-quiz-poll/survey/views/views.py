from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from ..models import Category, Topic
from ..forms import SaveAnswerForm, AddQuestionForm, \
    AddTopicForm, AddCategoryForm


@login_required
def survey_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    return render(request, 'survey/survey_detail.html', {'topic': topic})


@login_required
def delete_survey(request):
    user = User.objects.get(id=request.user.id)
    survey = user.user_survey_topics.all
    return render(request, 'survey/delete_survey.html', {'survey': survey})


@login_required
def user_survey(request):
    user = User.objects.get(id=request.user.id)
    survey = user.user_survey_topics.all
    return render(request, 'survey/user_survey.html', {'survey': survey})


def answer(request, category_id, topic_id):
    topic = Topic.objects.get(id=topic_id)
    questions = topic.questions.all()
    if request.method == "POST":
        forms = [SaveAnswerForm(request.POST, prefix="{}".format(_.id))
                 for _ in questions]
        for num, form in enumerate(forms):
            id_num = 'id-{}'.format(num)
            name = '{}-answer'.format(int(request.POST[id_num]))
            if form.is_valid():
                instance = form.save(commit=False)
                instance.answer = request.POST[name]
                instance.question = questions.get(id=int(request.POST[id_num]))
                instance.save()
        else:
            return HttpResponseRedirect(
                reverse(("survey:topics"), args=[category_id]))
    else:
        forms = [SaveAnswerForm(prefix="{}".format(_.id)) for _ in questions]

        topic.get_count = topic.get_count + 1
        topic.save()

    zipper = zip(questions, forms)
    return render(request, 'survey/answer.html',
                  {'questions': questions, 'topic': topic, 'zipper': zipper})


@login_required
def add_topic(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = AddTopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.category = category
            new_topic.user = request.user
            new_topic.save()
            return HttpResponseRedirect(
                reverse(("survey:add_question"),
                        args=[category_id, new_topic.id]))
    else:
        form = AddTopicForm()

    return render(request, 'survey/add_topic.html',
                  {'category': category, 'form': form})


@login_required
def add_question(request, category_id, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method == "POST":
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.topic = topic
            new_question.save()
            return HttpResponseRedirect(
                reverse("survey:add_question", args=[category_id, topic_id]))
    else:
        form = AddQuestionForm()

    return render(request, 'survey/add_question.html',
                  {'topic': topic, 'form': form})


def topic_list(request, category_id):
    category = Category.objects.get(id=category_id)

    category.get_count = category.get_count + 1
    category.save()

    topics = category.topics.all()
    return render(request, 'survey/topics.html',
                  {'category': category, 'topics': topics})


def categories_list(request):
    categories = Category.objects.order_by()
    return render(request, 'survey/categories.html',
                  {'categories': categories})


@login_required
def add_category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("survey:categories"))
    else:
        form = AddCategoryForm()

    return render(request, 'survey/add_category.html', {'form': form})


def index(request):
    return render(request, 'index.html', {'none': ""})
