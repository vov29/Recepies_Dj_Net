from django.shortcuts import render
from django.http import Http404

# Create your views here.
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def dishes(request, dish):
    what_dish = DATA.get(dish)
    if what_dish is None:
        raise Http404('Рецепта нет')
    number = request.GET.get('servings', 1)
    try:
        number = int(number)
    except ValueError:
        number = 1
    ingredients = {ingredient: number*count for ingredient, count in what_dish.items()}
    context = {'recipe': ingredients}
    return render(request, 'calculator/calculator.html', context)    