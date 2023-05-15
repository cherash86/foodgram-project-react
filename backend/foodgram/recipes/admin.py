from django.contrib import admin

from .models import Recipe, Favorite, RecipeIngredients


class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredients
    min_num = 1
    extra = 1


@admin.register(RecipeIngredients)
class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipe',
        'ingredient',
        'amount',
    )
    list_filter = ('id', 'recipe', 'ingredient')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'text',
        'pub_date',
        'author',
        'in_favorite',
    )
    list_filter = ('name', 'author', 'tags',)
    readonly_fields = ('in_favorite',)
    inlines = (RecipeIngredientsInline,)
    empty_value_display = '-пусто-'

    def in_favorite(self, obj):
        return obj.in_favorite.all().count()

    in_favorite.short_description = ('Количество добавлений в избранное')


@admin.register(Favorite)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )