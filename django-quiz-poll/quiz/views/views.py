from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.models import User
from ..models import Category, Topic
from ..forms import AddCategoryForm, AddQuestionForm, \
    AddTopicForm, AddAnswerForm


class CategoryListView(ListView):
    model = Category
    template_name = 'quiz/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


@login_required
def delete_quizes(request):
    user = User.objects.get(id=request.user.id)
    quizes = user.user_quiz_topics.all
    return render(request, 'quiz/delete_quizes.html', {'quizes': quizes})


@login_required
def user_quizes(request):
    user = User.objects.get(id=request.user.id)
    quizes = user.user_quiz_topics.all
    return render(request, 'quiz/user_quizes.html', {'quizes': quizes})


@login_required
def quiz_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    return render(request, 'quiz/quiz_detail.html', {'topic': topic})


def topic_list(request, category_id):
    category = Category.objects.get(id=category_id)

    category.get_count = category.get_count + 1
    category.save()

    topics = category.topics.all()
    return render(request, 'quiz/topics.html',
                  {'category': category, 'topics': topics})


def answer(request, category_id, topic_id):
    topic = Topic.objects.get(id=topic_id)
    questions = topic.questions.all()
    points = 0
    name = ""

    if request.method == "POST":
        for question in questions:
            for answer in question.answers.all():
                name = 'answer-{}'.format(answer.id)
                if request.POST.get(name, "miss") == 'True':
                    points = points + 1

                if (request.POST.get(name, "miss") == 'True') or (
                        request.POST.get(name, 'miss') == 'False'):
                    question.amount = question.amount + 1
                    answer.picked = answer.picked + 1

                answer.save()
            question.save()
        else:
            return HttpResponseRedirect(
                reverse("quiz:results", args=[category_id, topic_id, points]))
    else:
        topic.get_count = topic.get_count + 1
        topic.save()

    return render(request, 'quiz/answer.html',
                  {'topic': topic, 'questions': questions})


def results(request, category_id, topic_id, points):
    category = get_object_or_404(Category, id=category_id)
    topic = get_object_or_404(Topic, id=topic_id)

    return render(request, 'quiz/results.html',
                  {'points': points, 'category': category, 'topic': topic})


@login_required
def add_category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("quiz:categories"))
    else:
        form = AddCategoryForm()

    return render(request, 'quiz/add_category.html', {'form': form})


@login_required
def add_topic(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = AddTopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.category = category
            new_topic.user = request.user
            new_topic.save()
            return HttpResponseRedirect(
                reverse(("quiz:add_question_and_answers"),
                        args=[category_id, new_topic.id]))
    else:
        form = AddTopicForm()

    return render(request, 'quiz/add_topic.html',
                  {'category': category, 'form': form})


@login_required
def add_question_and_answers(request, category_id, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == "POST":
        form_question = AddQuestionForm(request.POST)
        forms_answer = [AddAnswerForm(
            request.POST, prefix="{}".format(num)) for num in range(4)]
        if form_question.is_valid():
            new_question = form_question.save(commit=False)
            new_question.topic = topic
            new_question.save()
            for form_answer in forms_answer:
                if form_answer.is_valid():
                    new_answer = form_answer.save(commit=False)
                    new_answer.question = new_question
                    new_answer.save()
            else:
                return HttpResponseRedirect(
                    reverse(("quiz:add_question_and_answers"),
                            args=[category_id, topic_id]))
    else:
        form_question = AddQuestionForm()
        forms_answer = [AddAnswerForm(prefix="{}".format(num))
                        for num in range(4)]

    return render(request, 'quiz/add_question_and_answers.html',
                  {'topic': topic, 'form_question': form_question,
                   'forms_answer': forms_answer})
