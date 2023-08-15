from django.shortcuts import render, get_object_or_404, redirect
from .new import KEY, ENDPOINT
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from assignments.views import generate_unique_code
from assignments.models import Referal
from .models import GeneratedImage, Trial, ImageDescription, AreaChoice, LevelChoice, IdeaRequest, GeneratedIdeas, Payment, IdeaPool
import openai

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
                        openai.api_type = "azure"
                        openai.api_base = "https://chat-gpt4.openai.azure.com/"
                        openai.api_version = "2023-06-01-preview"
                        openai.api_key = KEY
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
                            user_trials.image_trial -= 1
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
    image = get_object_or_404(GeneratedImage, id=id, description__user=request.user)
    image.is_active = False
    image.save()
    messages.success(request, 'Image deleted successfully.')
    return redirect('ai:desc_to_image')

@login_required
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
    openai.api_type = "azure"
    openai.api_base = "https://chat-gpt4.openai.azure.com/"
    openai.api_version = "2023-06-01-preview"
    openai.api_key = KEY
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


@login_required
def get_ideas(request):
    chack_if_user_has_trials(request)
    new_generated_ideas = []
    generated_ideas = GeneratedIdeas.objects.filter(idea_request__user=request.user)
    user_trials = Trial.objects.filter(user=request.user).first()

    if request.method == 'POST':
        area_id = request.POST.get('area')
        level_id = request.POST.get('level')
        description = request.POST.get('description')
        number_of_ideas = int(request.POST.get('number_of_ideas'))
        referal_code = request.POST.get('referal_code')
        if number_of_ideas < 1 and number_of_ideas > 10:
            messages.warning(request, 'Number of Images should be between 1 and 10')
            return redirect('ai:get_ideas')
        refered_by = None
        if referal_code:
            referal =  Referal.objects.filter(code=referal_code)
            if referal.exists:
                refered_by = referal.first().user
            else:
                messages.warning(request, 'Invalid Referal Code!!')
                return redirect('ai:get_ideas')
        try:
            area_choice = AreaChoice.objects.get(pk=area_id)
            level_choice = LevelChoice.objects.get(pk=level_id)
            ideas_pool = IdeaPool.objects.filter(pool_category__academic_level=level_choice, pool_category__subject_area=area_choice)
            if ideas_pool.count() < number_of_ideas:
                messages.warning(request, f'{ideas_pool.count()} ideas Found, {number_of_ideas} required! Try a number less than or equal to {ideas_pool.count()}')
                return redirect('ai:get_ideas')

            idea_request = IdeaRequest.objects.create(
                user=request.user,
                area=area_choice,
                level=level_choice,
                description=description,
                number_of_ideas = number_of_ideas,
                refered_by = refered_by
            )
            idea_request.save()
            for idea in ideas_pool[:number_of_ideas]:
                new_generated_ideas.append(idea)
                new_idea = GeneratedIdeas.objects.create(
                    idea_request=idea_request,
                    idea=idea,
                )
                new_idea.save()
            messages.success(request, 'Project Ideas Generated Successfully!')
            if user_trials:
                if user_trials.ideas_trial < 1:
                    amount = idea_request.get_amount()
                    payment = Payment.objects.create(
                        idea_request = idea_request,
                        transaction_code = generate_unique_code(),
                        amount = amount
                    )
                    payment.save()
                    messages.warning(request, f'Make payment of Ksh. {amount} to Complete process.')
                    return redirect('ai:make_payment', payment.transaction_code)
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
        'generated_ideas': generated_ideas,
    }
    return render(request, 'ai/get-ideas.html', context)

@login_required
def make_payment(request, payment_code):
    payment = get_object_or_404(Payment, transaction_code=payment_code, idea_request__user=request.user)
    title = f'Make Payment of Ksh. {payment.amount}'
    if payment.is_paid:
        title = f'Payment of Ksh. {payment.amount} Completed'
    context = {
        'title': title,
        'payment': payment
    }
    return render(request, 'ai/make-payment.html', context)