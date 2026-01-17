from django.shortcuts import render
from .ml import match_resume_to_job

def upload_resume(request):
    if request.method == 'POST':
        resume_text = request.POST.get('resume_text')
        job_desc = request.POST.get('job_desc')

        score = match_resume_to_job(resume_text, job_desc)

        return render(request, 'result.html', {'score': score})

    return render(request, 'upload.html')
