from django.shortcuts import render, get_object_or_404, redirect
from .new import KEY, ENDPOINT
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GeneratedImage, Trial, ImageDescription, AreaChoice, LevelChoice, IdeaRequest, GeneratedIdeas
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
    image_urls = []
    description = None
    can_generate_image = 0
    generated_images = GeneratedImage.objects.filter(description__user=request.user, is_active=True)
    user_trials = Trial.objects.filter(user=request.user).first()
    
    if user_trials:
        if user_trials.image_trial < 1:
            messages.warning(request, 'You have no trials left. Please buy any product from VSTech Limited to get 20 more trials.')
            can_generate_image = 0
        else:
            can_generate_image = 1
            if request.method == 'POST':
                description = request.POST.get('description')
                number_of_images = request.POST.get('number_of_images')
                size = request.POST.get('size')

                # Check if user has any trials left
                if description:
                    if number_of_images and (int(number_of_images) < 1 or int(number_of_images) > 4):
                        messages.warning(request, 'Number of images must be between 1 and 4.')
                    else:
                        image_description =  ImageDescription.objects.create(description=description, user=request.user, size=size, initial_number_of_images=number_of_images)
                        image_description.save()
                        response = openai.Image.create(
                            prompt=description,
                            size=size,
                            n=int(number_of_images),
                        )

                        if response.get('data') and len(response['data']) > 0:
                            for image_data in response['data']:
                                if image_data.get('url'):
                                    image_urls.append(image_data['url'])
                                    generated_image = GeneratedImage.objects.create(
                                        description=image_description,
                                        image_url=image_data['url']
                                    )
                                    generated_image.save()

                            # Update user's trial count
                            user_trials.number -= 1
                            user_trials.save()

                            messages.success(request, 'Image(s) generated successfully!')
                        else:
                            messages.warning(request, 'An error occurred while generating the image(s). Please try again.')
                else:
                    messages.warning(request, 'Please provide a description.')

    context = {
        'title': 'Generate Image',
        'category': 'AI',
        'image_urls': image_urls,
        'content': description,
        'can_generate_image': can_generate_image,
        'generated_images': generated_images,
    }
    return render(request, 'ai/desc_to_image.html', context)


@login_required
def delete_generated_image(request, id):
    image = get_object_or_404(GeneratedImage, id=id, user=request.user)
    image.is_active = False
    image.save()
    messages.success(request, 'Image deleted successfully.')
    return redirect('ai:desc_to_image')


def regenerate_image(request, image_id):
    chack_if_user_has_trials(request)
    generated_images = GeneratedImage.objects.filter(description__user=request.user, is_active=True)
    image_urls = []
    can_generate_image = 0
    user_trials = Trial.objects.filter(user=request.user).first()
    
    if user_trials:
        if user_trials.number < 1:
            messages.warning(request, 'You have no trials left. Please buy any product from VSTech Limited to get 20 more trials.')
            can_generate_image = 0
        else:
            can_generate_image = 1

    image = get_object_or_404(GeneratedImage, id=image_id, description__user=request.user)
    image_description = image.description.description
    image_size = image.description.size

    response = openai.Image.create(
        prompt=image_description,
        size=image_size,
        n=1,
    )

    if response.get('data') and len(response['data']) > 0:
        for image_data in response['data']:
            if image_data.get('url'):
                image_urls.append(image_data['url'])
                generated_image = GeneratedImage.objects.create(
                    description=image.description,
                    image_url=image_data['url']
                )
                generated_image.save()

        messages.success(request, 'Image(s) generated successfully!')
    else:
        messages.warning(request, 'An error occurred while generating the image(s). Please try again.')

    context = {
        'title': 'Generate Image',
        'category': 'AI',
        'image_urls': image_urls,
        'content': image_description,
        'can_generate_image': can_generate_image,
        'generated_images': generated_images,
    }
    return render(request, 'ai/desc_to_image.html', context)


def get_ideas(request):
    chack_if_user_has_trials(request)
    new_generated_ideas = []
    can_get_ideas = 0
    generated_ideas = GeneratedIdeas.objects.filter(idea__user=request.user)
    user_trials = Trial.objects.filter(user=request.user).first()

    if user_trials:
        if user_trials.ideas_trial < 1:
            messages.warning(request, 'You have no trials left. Pay Ksh. 200 for Ideas.')
            can_get_ideas = 0
        else:
            can_get_ideas = 1
            if request.method == 'POST':
                area_id = request.POST.get('area')
                level_id = request.POST.get('level')
                description = request.POST.get('description')

                try:
                    area_choice = AreaChoice.objects.get(pk=area_id)
                    level_choice = LevelChoice.objects.get(pk=level_id)
                    idea_request = IdeaRequest.objects.create(
                        user=request.user,
                        area=area_choice,
                        level=level_choice,
                        description=description
                    )

                    # for idea_data in generated_ideas:
                    #     GeneratedIdeas.objects.create(
                    #         idea=idea_request,
                    #         project_title=idea_data['project_title'],
                    #         project_details=idea_data['project_details']
                    #     )

                except AreaChoice.DoesNotExist or LevelChoice.DoesNotExist:
                    messages.warning(request, 'Please select an area and a level.')

    area_choices = AreaChoice.objects.all()
    level_choices = LevelChoice.objects.all()

    context  = {
        'area_choices': area_choices, 
        'level_choices': level_choices,
        'title': 'Get Project Ideas',
        'category': 'AI',
        'new_generated_ideas': new_generated_ideas,
        'can_get_ideas': can_get_ideas,
        'generated_ideas': generated_ideas,
    }
    return render(request, 'ai/get-ideas.html', context)
