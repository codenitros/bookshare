from django.shortcuts import render, redirect, get_object_or_404
from login.forms import RegistrationForm, sellform, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from .models import Books, UserProfile
from django.contrib.auth.models import User
from django.conf import settings
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger


def register(request):
	if request.method == 'POST':
		form_1 = RegistrationForm(request.POST)
		form_2 = UserProfileForm(request.POST)
		
		if form_1.is_valid() and form_2.is_valid():
			new_user = form_1.save(commit=False)
			new_user.set_password(form_1.cleaned_data['password1'])
			new_user.save()
			UserProfile.objects.create(user=new_user,
									    USN=form_2.cleaned_data['USN'],
									    year=form_2.cleaned_data['year'],
									    sem=form_2.cleaned_data['sem'],
									    phone=form_2.cleaned_data['phone'])

			#subject = 'Thank you  for registering with Book-Share'
			#message = 'Dear User,\n\n      Hope you take the best advantage of UVCE Book-share platform . Have a nice time !\n\n Thank You'
			#from_email = settings.EMAIL_HOST_USER
			#to_list = [save_1.email]
			#send_mail(subject,message,from_email,to_list,fail_silently=True)
			messages.success(request, 'Thank you for registering ! Login Here ')
			return redirect('/login/')
	else:
		form_1 = RegistrationForm()
		form_2 = UserProfileForm()

	args = {'form_1': form_1, 'form_2': form_2}
	return render(request, 'account/register.html', args)


@login_required
def edit(request):
	if request.method == 'POST':
		profile_form = UserProfileForm(instance=request.user.userprofile, data=request.POST, files=request.FILES)
		try:
			if profile_form.is_valid():
				profile_form.save()
				messages.success(request, "Your profile was updated successfully ")
				return redirect('/me/')
		except Exception as e:
			messages.warning(request, "Your profile could not be updated: Error{} ".format(e))
			return redirect('/me/')

	else:
		profile_form = UserProfileForm(instance=request.user.userprofile)
	
	return render(request, 'account/edit.html', {'profile_form': profile_form})


def index(request):
	return render(request, 'main/index.html')


@login_required
def home(request):
	if request.method == 'GET':
		return render(request, 'main/home.html')


@login_required
def sell(request):

	if request.method == 'POST':
		form = sellform(request.POST)

		if form.is_valid():
			m = form.save(commit=False)
			m.user = request.user
			m.book_name = 'notworking'
			m.save()
			messages.success(request, 'Your Book ad has been successfully added ')
			return redirect('/me/my-ads/')
	else:
		form = sellform()
	args = {'form': form}
	return render(request, 'books/sell.html', args)


@login_required
def buy(request):
	book_name = request.POST.get('dropdown')
	book_list = Books.objects.filter(book_name=book_name).order_by('-date_posted')
	return render(request, 'books/buy.html', {'book_list': book_list})


@login_required
def contact(request):
	if request.method == 'GET':
		return render(request, 'contact/contact.html')
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Enter a subject.')
		if not request.POST.get('message', ''):
			errors.append('Enter a message.')
		if not request.POST.get('e-mail', '') and '@' not in request.POST['e-mail']:
			errors.append('Enter a subject.')
		if not errors:
			send_mail(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('e-mail', 'noreply@example.com'), ['santoshbhat1998@gmail.com'], fail_silently=True)
			return render(request, 'contact/thanks.html')
	return redirect(reverse('contact/contact.html'))


@login_required
def show_profile(request):
	return render(request, 'account/profile.html')


@login_required
def delete_act(request):
	present_user = User.objects.get(username=request.user)
	present_user.is_active = False
	present_user.save()
	messages.success(request, 'Your Account has been successfully deleted ')
	return redirect('main/index.html')


@login_required
def ads(request):
	ad_list = Books.objects.filter(user=request.user).order_by('-date_posted')

	return render(request, 'account/myads.html', {'ad_list': ad_list})


@login_required
def update_ad(request, pk):
	template = 'books/sell.html'
	post = get_object_or_404(Books, pk=pk)

	if request.method == 'POST':
		form = sellform(request.POST, instance=post)
		try:
			if form.is_valid():
				form.save()
				messages.success(request, "The Ad has been updated successfully ")
				return redirect('/me/my-ads/')
		except Exception as e:
			messages.warning(request, 'The Ad could not be deleted : Error{}'.format(e))
			return redirect('/me/my-ads/')

	else:
		form = sellform(instance=post)
	return render(request, template, {'form': form})


@login_required
def delete_ad(request, pk):
	template = 'books/sell.html'
	post = get_object_or_404(Books, pk=pk)

	try:
		if request.method == 'POST':
				post.delete()
				messages.success(request, "The Ad has been deleted successfully ")
				return redirect('/me/my-ads/')
		else:
			form = sellform(instance=post)

	except Exception as e:
		messages.warning(request, 'The Ad could not be deleted : Error{}'.format(e))
		return redirect(request, '/me/my-ads/')
	
	return render(request, template, {'form': form})


@login_required
def books(request):
		if request.method == 'GET':
			return render(request, 'books/books_main.html')


@login_required
def sem1(request):
	if request.method == 'GET':
			return render(request, 'books/sem1.html')





