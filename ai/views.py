from django.shortcuts import render, get_object_or_404, redirect
from .new import KEY, ENDPOINT
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GeneratedImage, Trial
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://chat-gpt4.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = KEY

def chack_if_user_has_trials(request):
    user_trials = Trial.objects.filter(user=request.user)
    if user_trials:
        pass
    else:
        trial = Trial.objects.create(user=request.user)
        trial.save()

# Create your views here.
@login_required
def chat(request):
    context = {
        'title': 'Our Intelligent Chatbot',

    }
    return render(request, 'ai/chat.html', context)

@login_required
def desc_to_image(request):
    chack_if_user_has_trials(request)
    image_url = None
    description = None
    can_generate_image = 0
    genarated_images = GeneratedImage.objects.filter(user=request.user, is_active=True)
    user_trials = Trial.objects.filter(user=request.user).first()
    if user_trials:
        if user_trials.number < 1:
            messages.warning(request, 'You have no trials left. Please buy any product from VSTech Limited to get 20 more trials.')
            can_generate_image = 0
        else:
            can_generate_image = 1
            if request.method == 'POST':
                description = request.POST.get('description')
                # check if user has any trials left
                if description:
                    response = openai.Image.create(
                        prompt=description,
                        size='1024x1024',
                        n=1,
                    )

                    if response.get('data') and response['data'][0].get('url'):
                        image_url = response['data'][0]['url']

                        generated_image = GeneratedImage.objects.create(
                            user=request.user,
                            description=description,
                            image_url=image_url
                        )
                        generated_image.save()
                        # update user's trial count
                        user_trials.count -= 1
                        user_trials.save()

                        messages.success(request, 'Image generated successfully!')
                    else:
                        messages.warning(request, 'An error occurred while generating the image. Please try again.')
                else:
                    messages.warning(request, 'Please provide a description.')
    context = {
        'title': 'Generate Image',
        'category': 'AI',
        'image_url': image_url,
        'content': description,
        'can_generate_image': can_generate_image,
        'generated_images': genarated_images,
    }
    return render(request, 'ai/desc_to_image.html', context)

@login_required
def delete_generated_image(request, id):
    image = get_object_or_404(GeneratedImage, id=id, user=request.user)
    image.is_active = False
    image.save()
    messages.success(request, 'Image deleted successfully.')
    return redirect('ai:desc_to_image')
