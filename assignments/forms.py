from django import forms
from .models import AssignmentOrder, AssignmentFiles, ProjectOrder, ProjectFiles

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = AssignmentOrder
        fields = (
            'title',
            'academic_level', 
            'subject_area',
            'additional_information',
            'period',
        )

class AssignmentFilesForm(forms.ModelForm):
    class Meta:
        model = AssignmentFiles
        fields = ('file',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectOrder
        fields = (
            'title',
            'academic_level', 
            'subject_area',
            'additional_information',
            'period'
        )

class ProjectFilesForm(forms.ModelForm):
    class Meta:
        model = ProjectFiles
        fields = ('file',)