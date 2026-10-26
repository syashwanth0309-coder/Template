import time
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .forms import EnquiryForm
from .data import CATEGORIES, SKILLS, PROJECTS, CERTIFICATIONS
@require_http_methods(["GET", "POST"])
def home(request):
    form = EnquiryForm(request.POST or None)
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            now = time.time()
            if now - request.session.get("last_enquiry", 0) < 60:
                form.add_error(None, "Please wait a minute before sending another enquiry.")
            else:
                form.save()
                request.session["last_enquiry"] = now
                messages.success(request, "Your enquiry has been saved. Thank you for getting in touch!")
                return redirect(reverse("enquiry:home") + "#enquiry")
    return render(request, "index.html", {"form":form, "categories":CATEGORIES, "skills":SKILLS, "projects":PROJECTS, "certifications":CERTIFICATIONS, "modal_data":{"projects":PROJECTS, "certifications":CERTIFICATIONS}})
