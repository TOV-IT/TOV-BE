import unittest

from pages.models import *
from pages.utils import construct_component


class ModelTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        Page.objects.all().delete()
        Component.objects.all().delete()
    
    def test_create_page(self):
        
        page = Page(
            title="title",
            order=2
        )
        page.save()
        
        self.assertIsInstance(page, BasePage)
        self.assertEqual(page.title, "title")
    
    def test_create_components(self):
        page = Page(
            title="title",
            order=2
        )
        page.save()
        
        page_id = page.id
        
        data = {
            'title': "main banner",
            'sub_title': "sub title",
            'body': "hello",
            'order': 3,
            'type': "banner",
            'sub_type': "banner2",
            'bg_color_type': "#FFF"
        }
        component = construct_component(data['type'])

        for k, v in data.items():
            setattr(component, k, v)
        component.page = Page.objects.get(pk=page_id)
        component.save()
        
        self.assertIsInstance(component, Banner)
        self.assertEqual(component.body, 'hello')
    
    def test_create_pageImages(self):
        page = Page()
        page.save()
        banner = Banner(page=page)
        banner.save()
        
        data = {
            'alt': 'picture',
            'image_url': 'https://cloud',
            'order': 2,
        }
        pageimage = PageImage()
        for k, v in data.items():
            setattr(pageimage, k, v)
        pageimage.component = banner
        pageimage.save()
        
        self.assertIsInstance(pageimage, PageImage)
        self.assertEqual(pageimage.alt, "picture")
        

if __name__ == '__main__':
    unittest.main()
