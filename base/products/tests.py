from django.test import TestCase
from .models import Category, Product, ProductFeature, Comment
from customers.models import User


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="category", slug="category", sub_category=None, is_sub=False)

    def test_category_creation(self):
        self.assertEqual(self.category.name, "category")
        self.assertEqual(self.category.slug, "category")
        self.assertEqual(self.category.sub_category, None)
        self.assertEqual(self.category.is_sub, False)

    def test_category_str(self):
        self.assertEqual(str(self.category), "category")


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='test', slug='test', sub_category=None, is_sub=False, )
        self.product = Product.objects.create(category=self.category, name="test", slug="test", image="test",
                                              description="test", price=1000, is_available=True, stock=10, )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "test")
        self.assertEqual(self.product.slug, "test")
        self.assertEqual(self.product.price, 1000)
        self.assertEqual(self.product.is_available, True)
        self.assertEqual(self.product.stock, 10)
        self.assertEqual(self.product.image, "test")
        self.assertEqual(self.product.description, "test")

    def test_product_str(self):
        self.assertEqual(str(self.product), 'test')


class ProductFeatureModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="category", slug="category", sub_category=None, is_sub=False)
        self.product = Product.objects.create(category=self.category, name="product", slug="product", price=1000,
                                              is_available=True, stock=10, image="image", description="description")
        self.product_feature = ProductFeature.objects.create(color="red", type="type", material="material",
                                                             product=self.product)

    def test_product_feature_creation(self):
        self.assertEqual(self.product_feature.color, "red")
        self.assertEqual(self.product_feature.type, "type")
        self.assertEqual(self.product_feature.material, "material")
        self.assertEqual(self.product_feature.product, self.product)

    def test_product_feature_str(self):
        self.assertEqual(str(self.product_feature), "red")


class CommentModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="category", slug="category", sub_category=None, is_sub=False)
        self.product = Product.objects.create(category=self.category, name="product", slug="product", price=1000,
                                              is_available=True, stock=10, image="image", description="description")
        self.customer = User.objects.create(username="masoud", email="masoudpro2@gmail.com",
                                            phone_number="09120572655", password="123456")
        self.comment = Comment.objects.create(title="title", body="body", customer=None, product=self.product)

    def test_comment_creation(self):
        self.assertEqual(self.comment.title, "title")
        self.assertEqual(self.comment.body, "body")
        self.assertEqual(self.comment.customer, None)
        self.assertEqual(self.comment.product, self.product)

    def test_comment_str(self):
        self.assertEqual(str(self.comment), "title")
