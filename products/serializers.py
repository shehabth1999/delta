from rest_framework import serializers 
from .models import Product, Image, Location

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1 

    def get_images(self, instance):
        images = Image.objects.filter(product=instance)
        images_data = ImageSerializer(images, many=True).data
        image_list = [item["image"] for item in images_data]
        return image_list
