from django.core.mail import send_mail

from django.db import models
from django.core import validators
from django.conf import settings

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    """
    Users within the Django authentication system are represented by this
    model.
    Username, password and email are required. Other fields are optional.
    """

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('<br /> Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'), 
        validators=[validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')]
    )

    type_pv = models.CharField(_('Type: '), help_text=_('<br /> Chose P for Performer, V for Venue'), max_length=1, blank=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    birthday = models.CharField(_('birthday'), max_length=30, blank=True)
    bio = models.CharField(_('bio'), max_length=100, blank=True)
    gender = models.CharField(_('gender'), max_length=30, blank=True)
    status = models.CharField(_('status'), max_length=50, blank=True)


    youtube1 = models.CharField(_('youtube1 link'), max_length=100, blank=True)
    youtube2 = models.CharField(_('youtube2 link'), max_length=100, blank=True)
    youtube3 = models.CharField(_('youtube3 link'), max_length=100, blank=True)
    soundcloud1 = models.CharField(_('soundcloud1 link'), max_length=100, blank=True)
    soundcloud2 = models.CharField(_('soundcloud2 link'), max_length=100, blank=True)
    soundcloud3 = models.CharField(_('soundcloud3 link'), max_length=100, blank=True)

    y1d = models.CharField(_('Youtube 1 Description'), max_length=100, blank=True)
    y2d = models.CharField(_('Youtube 2 Description'), max_length=100, blank=True)
    y3d = models.CharField(_('Youtube 3 Description'), max_length=100, blank=True)
    s1d = models.CharField(_('Soundcloud 1 Description'), max_length=100, blank=True)
    s2d = models.CharField(_('Soundcloud 2 Description'), max_length=100, blank=True)
    s3d = models.CharField(_('Soundcloud 3 Description'), max_length=100, blank=True)


    location = models.CharField(_('location string'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)

    photo = models.CharField(_('photo link'), max_length=200, blank=True, null=True)

    capacity = models.CharField(_('capacity string'), max_length=30, blank=True)
    description = models.CharField(_('description string'), max_length=30, blank=True)
    address = models.CharField(_('address string'), max_length=100, blank=True)
    venue_name = models.CharField(_('venue name string'), max_length=30, blank=True)




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

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def youtube_link1(self):
        return self.get_youtube_link1()

    def get_youtube_link1(self):
        return self.youtube1.replace('watch?v=', 'embed/')

    @property
    def youtube_link2(self):
        return self.get_youtube_link2()

    def get_youtube_link2(self):
        return self.youtube2.replace('watch?v=', 'embed/')

    @property
    def youtube_link3(self):
        return self.get_youtube_link3()

    def get_youtube_link3(self):
        return self.youtube3.replace('watch?v=', 'embed/')

    def get_absolute_url(self):
        return settings.LOGIN_REDIRECT_URL


    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Listing(models.Model):
    listing_id = models.CharField(
        _('listing_id'),
        max_length=30,
        unique=True,
        help_text=_('<br /> Required. 30 characters or fewer. Letters and digits and only.'), 
        validators=[validators.RegexValidator(r'^[\w]+$', _('Enter a valid listing_id.'), 'invalid')]
    )
    listing_id = models.CharField(max_length=30, primary_key=True)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    contact = models.EmailField()
    ldatetime = models.DateTimeField(default=None, blank=True, null=True)
    listing_venue = models.ForeignKey(User, related_name="listing_venue")
    performers_liked = models.ManyToManyField(User,  related_name="performers_liked")
    final_performer = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name="final_performer")
    class Meta:
        verbose_name = 'Listing'
