from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, SavedPost, Review
from .forms import ReviewForm

# View to save or unsave a post
@login_required
def save_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    saved_post = SavedPost.objects.filter(user=request.user, post=post)
    
    if saved_post.exists():
        saved_post.delete()  # Unsave if already saved
        saved = False
    else:
        SavedPost.objects.create(user=request.user, post=post)  # Save post
        saved = True
    
    return JsonResponse({'saved': saved})

# View to display post details and handle reviews
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    reviews = post.reviews.all()
    is_saved = SavedPost.objects.filter(user=request.user, post=post).exists() if request.user.is_authenticated else False
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.user = request.user
            review.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = ReviewForm()
    
    return render(request, 'post_detail.html', {
        'post': post,
        'reviews': reviews,
        'form': form,
        'is_saved': is_saved
    })