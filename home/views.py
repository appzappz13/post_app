from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from account.models import Post

# Create your views here


@login_required
def home(request):
    post = Post.objects.all().order_by('-post_time')
    current_user = request.user
    c_username = current_user.username
    
    
    context= {"user": current_user, "post": post,"c_username":c_username}
    return render(request,'home.html',context )


def posting(request):
    current_user = request.user.id
    print("current user : ",current_user)

    if request.method == "POST":
        post_content = request.POST.get('post_content')
        post_image = request.FILES.get('post_image')

        if post_image and post_content:
            new_post = Post(post_content=post_content,username_id=current_user, post_image = post_image, post_like=0)
            new_post.save()
            
        else:
            new_post = Post(post_content=post_content,username_id=current_user, post_like=0)
            new_post.save()

    return redirect('home')



def edit_post(request,post_id):
    print(post_id)
    current_post= Post.objects.filter(id=post_id).all() 
    print(current_post)
    

    return render(request,'edit_post.html',{"current_post": current_post })



def update_post(request,post_id):
    print("form passed data :",post_id)
    if request.method == "POST":
        print("post true ")
        update_content = request.POST.get('update_content')
        update_image  = request.FILES.get('update_image')
        print("update_content :",update_content)
        print("update_image :", update_image)
        if update_content :
                if update_image :
                    update_data = Post.objects.get(id = post_id)
                    update_data.post_image = update_image
                    update_data.post_content = update_content
                    update_data.save()

                    print("success")
                elif update_image is None:
                    Post.objects.filter(id = post_id).update( post_content = update_content)
                    print("content _success")
                else :
                    print("no data")


        else:
            Post.objects.filter(id = post_id).update( post_image = update_image )
            print("success")



    return redirect('home')


