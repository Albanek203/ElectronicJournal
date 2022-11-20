from .models import *
from django.shortcuts import render, get_object_or_404, redirect


def journal_list(request):
    journals = Journal.objects.order_by('name')
    return render(request, 'mysite/journal_list.html', {'journals': journals})


def journal_detail(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    topics = Topic.objects.filter(journal=journal.id)
    student_journals = StudentJournal.objects.filter(journal=journal.id)
    print(journal.id)
    marks = Mark.objects.values()
    return render(request, 'mysite/journal_detail.html',
                  {'journal': journal, 'topics': topics, 'student_journals': student_journals, 'marks': marks})
