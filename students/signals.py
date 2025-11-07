from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import Student, Profile


@receiver(post_save, sender=Student)
def create_profile_student(sender, instance, created, **kwargs):
    """ this function create profile for students """
    if created:
        # create Profile
        Profile.objects.create(
            bio = f"{instance.fullname} bio",
            student=instance
        )