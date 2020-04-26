from django import forms
from quiz.models import Category


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': ''}

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name", None)

        if name:
            all_object = Category.objects.all()
            for object in all_object:
                if name == object.name:
                    self.add_error('name', 'Category {} already exists...'.format(name))
            
        return self.cleaned_data