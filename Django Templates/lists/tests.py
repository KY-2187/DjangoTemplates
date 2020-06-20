from django.test import TestCase

from .models import Item

class HomePageTest(TestCase):

	def test_home_page_returns_correct_html(self):
		

	def test_can_save_POST_request(self):
		

#class ListPageTest(TestCase):


#class CreatePageTest(TestCase):


class ItemModelTest(TestCase):
	
	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'First Item'
		first_item.save()
		#Shortcut
		#first_item = Item.objects.create(text='First Item')
		
		second_item = Item()
		second_item.text = 'Second Item'
		second_item.save()

		items = Item.objects.all()
		#Item.objects.get('value') gives a single record
		#Item.objects.filter() modifies the ???
		#Item.objects.order_by(field that you want to order it by) have the results in a different order
		#Item.objects.values_list('text') attributes 
		#Item.objects.filter(id__in(1,2)).order_by('id DESC').values_list('text')
		#SELECT text from item where id in(1,2) ORDER BY id; 
		self.assertEqual(items.count(), 2)

		saved_item_one = items[0]
		saved_item_two = items[1]

		self.assertEqual(saved_item_one.text, 'First Item')
		self.assertEquall(saved_item_one.text, 'Second Item')
