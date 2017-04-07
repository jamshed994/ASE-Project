from django.test import TestCase

from performer.models import User
from django.test import RequestFactory
from performer.views import CreateNewListing,LikeListing
from performer.models import Listing
from performer.forms import UserCreationForm,PerformerUpdateForm


# Create your tests here.

class PerformerViewsTestCase(TestCase):
	def test_index(self):
		resp=self.client.get('/')
		self.assertEqual(resp.status_code,200)

class UserModelTest(TestCase):

    def test_data_set_up(self):
        #Set up non-modified objects used by all test methods
        a=User.objects.create(first_name='Big', last_name='Bob',username='BigBob')
        self.assertEqual(a.username,'BigBob')

    def test_DB_entry(self):
        a=User.objects.create(first_name='Big', last_name='Bob',username='BigBob')
        a.save()

    def test_first_name_label(self):
    	a=User.objects.create(first_name='Big', last_name='Bob',username='BigBob')
    	a.save()
    	user=User.objects.get(username='BigBob')
    	field_label = user.first_name
    	self.assertEquals(field_label,'Big')

    def test_listing_create(self):
    	#Testing Foreign Key Constraint
    	a=User.objects.create(first_name='Big', last_name='Bob',username='BigBob')
    	a.save()
    	x=Listing.objects.create(subject='test_subject', listing_id='12345', contact='test_contact',message='test_message',listing_venue=a)
    	x.save()

    def test_listing_entry(self):
    	a=User.objects.create(first_name='Big', last_name='Bob',username='BigBob')
    	a.save()
    	x=Listing.objects.create(subject='test_subject', listing_id='12345', contact='test_contact',message='test_message',listing_venue=a)
    	x.save()
    	entry=Listing.objects.get(listing_id='12345')
    	field_label = entry.listing_venue.first_name
    	self.assertEquals(field_label,'Big')

    def test_listing_class(self):
        a=User.objects.create(first_name='Big', last_name='Bob',username='BigBob')
        a.save()
        x=Listing.objects.create(subject='test_subject', listing_id='12345', contact='test_contact',message='test_message',listing_venue=a,)
        x.save()
        cat = Listing.objects.get(listing_id="12345")
        field_label=cat.subject
        #self.assertEquals(field_label,'test_subject')
        entry = Listing(listing_id="12345")

        self.assertEqual(str("test_subject"),field_label )

    def test_names(self):
       a=User.objects.create(first_name='Big', last_name='Bob',username='BigBob')
       a.save()
       user=User.objects.get(username='BigBob')
       field_label = user.first_name
       fm=user.get_full_name()
       sn=user.get_short_name()
       sc3=user.get_youtube_link3()
       self.assertEquals(field_label,'Big')




class ViewTest(TestCase):
	#View Test 1
	def test_Login(self):
		response=self.client.get('/performer/login/')
		self.assertEquals(response.status_code,200)

	#View Test 2
	def test_create_listing(self):
		request_factory = RequestFactory()
		request = request_factory.post('listing/create', data={'subject':"fbsjkfbksbfj",'listing_id':"318959",'message':'iufbnsdjndskj'})
		response= CreateNewListing(request)
		self.assertEquals(response.status_code,200)    
    
    # def test_create_listing1(self):
    #     request_factory = RequestFactory()
    #     request = request_factory.post('listing/create', data={'subject':"fbsjkfbksbfj",'listing_id':"318959",'message':'iufbnsdjndskj'})
    #     response= CreateNewListing(request)
    #     self.assertEquals(response.status_code,200)

	def test_LikeListing(self):
		request_factory = RequestFactory()
		a=User.objects.create(first_name='Big12', last_name='Bob',username='venue1234456')
		a.save()
		b=User.objects.create(first_name='Big', last_name='Bob',username='BigBob')
		b.save()
		request = RequestFactory().post('listing/create', data={'subject':'fbsjkfbksbfj','listing_id':'318959','message':'iufbnsdjndskj', 'listing_venue':'venue1234456'})
		response= CreateNewListing(request)
		self.assertEquals(response.status_code,200)   
		request = RequestFactory().post('listing/create',data={'user':"BigBob"})
		#response= LikeListing(request, listing_id='318959')

class FormTest(TestCase):
	#Form Test 1
	def test_form(self):
		form_data = {'username': 'BigBob56','email':'bb@gmail.com','first_name': 'big','last_name':'bob','type_pv':'P','password1':'password1234', 'password2':'password1234'}
		form = UserCreationForm(data=form_data)
		self.assertTrue(form.is_valid())

	def test_update_performer(self):
		form_data = {'username': 'BigBob56','email':'bb@gmail.com','first_name': 'big','last_name':'bob','bio':'test_bio'}
		form = PerformerUpdateForm(data=form_data)
		self.assertTrue(form.is_valid())



