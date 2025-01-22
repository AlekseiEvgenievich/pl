from main.models import Seller,Category,Tag,Ad
from django.contrib.auth.models import User

user2 = User.objects.create_user('john')
user3 = User.objects.create_user('ivan')
user = User.objects.get(username="aleks")
seller1 = Seller(user=user)
seller1.save()
seller2 = Seller(user=user1)
seller2.save()
seller3 = Seller(user=user2)
seller3.save()

>>> Tag.objects.create(name="a")
<Tag: Tag object (1)>
>>> Tag.objects.create(name="b")
<Tag: Tag object (2)>
>>> Tag.objects.create(name="c")
<Tag: Tag object (3)>
>>> Category.objects.create(name="Product")
<Category: Category object (1)>
>>> Category.objects.create(name="Alcolol")
<Category: Category object (2)>
>>> Category.objects.create(name="Alcolol")
<Category: Category object (3)>
>>> Category.objects.create(name="Fruit")
<Category: Category object (4)>
>>> Category.objects.create(name="Snacks")
<Category: Category object (5)>
>>> tag1 = Tag.objects.get(name = 'a')
>>> tag2 = Tag.objects.get(name = 'b')
>>> tag3 = Tag.objects.get(name = 'c')
>>> cat1 = Category.objects.get(name = "Product")
>>> cat2 = Category.objects.get(name = "Alcolol")
>>> cat3 = Category.objects.get(name = "Fruit")
>>> cat4 = Category.objects.get(name = "Snacks")
>>> Ad.objects.create(name='banana', seller = seller1, category = cat1).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='beer', seller = seller1, category = cat2).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='apple', seller = seller1, category = cat3).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='chips', seller = seller1, category = cat4).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='chips', seller = seller2, category = cat4).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='apple', seller = seller3, category = cat3).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='apple', seller = seller2, category = cat3).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='beer', seller = seller2, category = cat2).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='banana', seller = seller2, category = cat1).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='banana', seller = seller3, category = cat1).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='beer', seller = seller3, category = cat2).tags.add(tag1,tag2,tag3)
>>> Ad.objects.create(name='chips', seller = seller3, category = cat4).tags.add(tag1,tag2,tag3)
> Ad.objects.filter(category__name__contains = 'Product')
