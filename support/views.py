import random

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Prompt, Resource, JournalEntry
from .forms import JournalEntryForm


def _session_key(request):
    if not request.session.session_key:
        request.session.save()
    return request.session.session_key


def home(request):
    prompt = None
    prompts = list(Prompt.objects.all())
    if prompts:
        prompt = random.choice(prompts)
    return render(request, "support/home.html", {"prompt": prompt})


def prompt_list(request):
    stage = request.GET.get("stage")
    prompts = Prompt.objects.all()
    if stage:
        prompts = prompts.filter(stage=stage)
    return render(request, "support/prompt_list.html", {
        "prompts": prompts,
        "stages": Prompt.STAGE_CHOICES,
        "active_stage": stage,
    })


def prompt_detail(request, pk):
    prompt = get_object_or_404(Prompt, pk=pk)
    key = _session_key(request)

    if request.method == "POST":
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.prompt = prompt
            entry.session_key = key
            entry.save()
            messages.success(request, "Your reflection has been saved.")
            return redirect("prompt_detail", pk=pk)
    else:
        form = JournalEntryForm()

    entries = JournalEntry.objects.filter(prompt=prompt, session_key=key)
    return render(request, "support/prompt_detail.html", {
        "prompt": prompt,
        "form": form,
        "entries": entries,
    })


def resource_list(request):
    resources = Resource.objects.all()
    grouped = {}
    for r in resources:
        grouped.setdefault(r.get_kind_display(), []).append(r)
    return render(request, "support/resource_list.html", {"grouped": grouped})


def journal(request):
    key = _session_key(request)
    entries = JournalEntry.objects.filter(session_key=key)
    return render(request, "support/journal.html", {"entries": entries})
