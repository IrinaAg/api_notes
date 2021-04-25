from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'created']

numbers = [0, 1]
odd_numbers = []
while numbers[0] < 1000000:
    need = numbers[0] + numbers[1]
    numbers[0], numbers[1] = numbers[1], need
    if (need % 2) == 0:
        odd_numbers.append(need)
        # print(odd_numbers)
print(odd_numbers[:5])



