from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from pages.utils import construct_component
from pages.models import *



class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'order',
        )

class ImageListerializer(serializers.ModelSerializer):
    class Meta:
        model = PageImage
        fields = (
            'alt',
            'image_url',
            'order',
        )
        
    

# class BannerCreateSerializer(ComponentCreateSerializer):
#     pass
    

class ComponentCreateSerializer(serializers.ModelSerializer):
    pageimages = ImageListerializer(many=True)
    
    class Meta:
        model = Component
        fields = (
            'title',
            'sub_title',
            'body',
            'order',
            'type',
            'sub_type',
            'bg_color_code',
            'page',
            'pageimages'
        )
        # read_only_fields=('id', )

    def create(self, validated_data):
        print(validated_data)
        type = validated_data['type']
        
        # Get Page object
        page = validated_data['page']
        
        # Get superuser
        # user = None
        # request = self.context.get("request")
        # if request and hasattr(request, "user"):
        #     user = request.user
        #     if not user.is_superuser():
        #         raise serializers.ValidationError('Only Superuser can create Component')
        # else:
        #     raise serializers.ValidationError('Need Authentication')

        # Create the Component
        component = construct_component(type)
        
        for key, value in validated_data.items():
            if key == 'pageimages':
                continue
            setattr(component, key, value)
        
        component.page = page
        component.save()
        
        pageimage_datas = validated_data['pageimages']
        for pageimage_data in pageimage_datas:
            PageImage.objects.create(
                component=component, 
                **pageimage_data)
            
        return component
