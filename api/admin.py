from django.contrib import admin
from .models import Vacancy, Resume, Application, FavoriteVacancy, Company

admin.site.register(Vacancy)
admin.site.register(Resume)
admin.site.register(Application)
admin.site.register(FavoriteVacancy)
admin.site.register(Company)


