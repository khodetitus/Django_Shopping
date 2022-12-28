from .models import Category


def category_list(request):
    categories = Category.objects.get_active_list().filter(is_sub=False)
    return {"categories": categories}
