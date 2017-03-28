from django.core.mail import send_mail

from django.db import models
from django.core import validators
from django.conf import settings

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, AbstractUser


# class User(AbstractBaseUser, PermissionsMixin):
#     """
#     Users within the Django authentication system are represented by this
#     model.
#     Username, password and email are required. Other fields are optional.
#     """



class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')]
    ) 
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)

    #location= models.CharField(_('location string'), max_length=30, blank=True)


    photo = models.ImageField(upload_to='users', blank=True, null=True)

    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @property
    def full_name(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

 
class Performer(User):
    performer_id = models.CharField(max_length=30, unique=True)
 
    class Meta:
        verbose_name = 'Performer'



    # username = models.CharField(
    #     _('username'),
    #     max_length=30,
    #     unique=True,
    #     help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     validators=[validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')]
    # )

    # first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last_name = models.CharField(_('last name'), max_length=30, blank=True)

    birthday = models.CharField(_('birthday'), max_length=30, blank=True)
    bio = models.CharField(_('bio'), max_length=100, blank=True)
    gender = models.CharField(_('gender'), max_length=30, blank=True)
    status = models.CharField(_('status'), max_length=50, blank=True)


    youtube = models.CharField(_('youtube link'), max_length=100, blank=True)
    soundcloud = models.CharField(_('soundcloud link'), max_length=100, blank=True)
    # location = models.CharField(_('location string'), max_length=30, blank=True)
    # email = models.EmailField(_('email address'), blank=True)

    # photo = models.ImageField(upload_to='users', blank=True, null=True)

    # is_staff = models.BooleanField(
    #     _('staff status'), default=False,
    #     help_text=_('Designates whether the user can log into this admin '
    #                 'site.'))
    # is_active = models.BooleanField(
    #     _('active'), default=True,
    #     help_text=_('Designates whether this user should be treated as '
    #                 'active. Unselect this instead of deleting accounts.'))
    # date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    # objects = UserManager()

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']

    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')

    # @property
    # def full_name(self):
    #     return self.get_full_name()

    @property
    def youtube_link(self):
        return self.get_youtube_link()

    def get_absolute_url(self):
        return settings.LOGIN_REDIRECT_URL


    def get_youtube_link(self):
        return self.youtube.replace('watch?v=', 'embed/')

    # def get_full_name(self):
    #     """
    #     Returns the first_name plus the last_name, with a space in between.
    #     """
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
