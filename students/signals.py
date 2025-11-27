from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import Profile, Student, Teacher


@receiver(post_save, sender=Profile)
def create_profile_user(sender, instance, created, **kwargs):
    """ this function create profile for users """
    if created:
        if instance.is_student:
            # create Student
            Student.objects.create(
                fullname= f"{instance.user.firstname} {instance.user.lastname}",
                profile= instance
            )
        else:
            # create Teacher
            Teacher.objects.create(
                fullname= f"{instance.user.firstname} {instance.user.lastname}",
                profile= instance
            )