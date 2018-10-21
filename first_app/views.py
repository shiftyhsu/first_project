from django.shortcuts import render
from first_app.models import Topic,Webpage,AccessRecord,SAVE
from first_app.forms import UserForm,UserProfileInfoForm,FormName
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
import random
import urllib
from sklearn.neighbors import NearestNeighbors
def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'first_app\_register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
def index(request):
    my_dict={'insert_me':'Hello from the other side!!!','check':str(3+5)}
    wblist=AccessRecord.objects.order_by('date')
    date_dict={'access_records':wblist}
    return render(request,'first_app\index.html')
def other(request):
    return render(request,'first_app\other.html')
def mat(request):
    return render(request,'first_app\matplotlib.html')
def hyper(request):
    return render(request,'first_app\hyper.html')
def Undex(request):
    my_dict={'insert_me':'Hello from the other side!!!','check':str(3+5)}
    wblist=AccessRecord.objects.order_by('date')
    date_dict={'access_records':wblist}
    return render(request,'first_app\index.html',date_dict)
def help(request):
    my_dictT={'insert_me':'you do not know me!','help_me':'It is Final Countdown'}
    return render(request,'first_app\second.html',context=my_dictT)
def form_name_view(request):
    form=FormName()
    if request.method=='POST':
        form=FormName(request.POST)

        if form.is_valid():
                form.save(commit=True)
                print('VALIDATION SUCCESS!')
                print('NAME: '+form.cleaned_data['name'])
                print('EMAIL: '+form.cleaned_data['email'])
                print('TEXT: '+form.cleaned_data['text'])
                return Undex(request)
        else:
            print('Validation Not Pass')

    return render(request,'first_app\_formpage.html',{'form':form})
def folium (request):
    return render_to_response('first_app\_2017_m1ymap.html')
def folium_Market_Select (request):
    return render_to_response('first_app\Market_Select.html')

def profile(request):
    return render(request,'first_app\profile.html')
import os
from django.conf import settings
from django.http import HttpResponse

import os
from django.conf import settings
from django.http import HttpResponse

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename=CV.pdf' + os.path.basename(file_path)
            return response
    raise Http404




@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'first_app\login.html', {})
###############################################################
def recommender(request):
    dft=pd.read_csv('first_app\MCL_R.csv',engine='python')
    lt=['Action', 'Adventure',
       'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama',
       'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance',
       'Sci-Fi', 'Thriller', 'War', 'Western']
    dist1=[]
    dist2=[]
    for i in lt:
        lus=list(dft[dft[i]==1]['name'])
        dist1.append(i)
        dist2.append(lus)
    return render(request,'first_app\movierecommender.html',context={'Dist1':dist1,'Dist2':dist2})
def recommender_list(request):
    dfu=pd.read_csv('first_app\MCL_R.csv',engine='python')
    def movies_concector(MR,Name,n=16,k=5):
        neigh = NearestNeighbors(16,'cosine')
        neigh.fit(MR.iloc[:,23:].values)
        top_k_distances,top_k_movies = neigh.kneighbors(MR.iloc[:,23:].values, return_distance=True)
        Id=int(list(MR.movieid)[list(MR.name).index(Name)])
        listid=[i for i in top_k_movies[Id-1][1:n]]
        distance=[j for j in top_k_distances[Id-1][1:n]]
        lst=[MR.name[r] for r in listid]
        pb=[1/i if i!=0 else 1000 for i in distance]
        ps=[u/sum(pb) for u in pb]
        lstr=list(np.random.choice(lst,k,p=ps,replace=False))
        return lstr
    if 'id' in request.GET:
        print(type(request.GET['id']))
        val=request.GET['id']
        result=movies_concector(dfu,val,n=16,k=11)
        def genre_l(u):
            return [dfu.columns[5:23][ix] for ix,i in enumerate(dfu[dfu.name==u].iloc[:,5:23].values.tolist()[0]) if i==1]
        M_Dict={}
        M_Dict.update({'Name':val,'MovieId':list(dfu[dfu.name==val]['movieid'])[0],'URL_Result':urllib.parse.quote_plus(val),'ADDRESS':list(dfu[dfu.name==val]['address'])[0],'DATE':list(dfu[dfu.name==val]['date'])[0],'Genre':genre_l(val)})
        S_Dict={}
        url_result=[urllib.parse.quote_plus(i) for i in result]
        perid=[list(dfu.name).index(i) for i  in result]
        lislength=list(range(len(result)))
        print(perid)
        S_Dict.update({'Result':result,'Movieid':list(dfu.loc[perid,'movieid']),'URL_Result':url_result,'ADDRESS':list(dfu.loc[perid,'address']),'DATE':list(dfu.loc[perid,'date']),'Genre':[genre_l(g) for g in result]})
        return render_to_response('first_app\movielist.html',locals())
    else:
        return HttpResponseRedirect(request,"first_app\movierecommender.html")
