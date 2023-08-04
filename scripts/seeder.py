from django.contrib.auth.models import Group

def run():
    if not Group.objects.all():
        groups = ["admin", "control_estudio", "evaluacion", "coordinacion", "docente"]

        bulk_list_groups = []
        for group in groups:
            bulk_list_groups.append(Group(name=group))

        Group.objects.bulk_create(bulk_list_groups)
