import redis
from django.conf import settings
from . models import Product

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)
class Recommender:
    def get_product_key(self, id):
        return f'product:{id}:purchased_with'

    def products_bougth(self, products):
        product_ids =[p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
                if product_id ! = with_id:
                    r.zincrby(self.get_product_key(product_id),
                                                   1,
                                                   with_id)
    def suggest_products_for(self,products, max_result=6):
        product_ids =[p.id for p in products]
        if len(products) == 1:

            suggestions = r.zrange(self.get_product_key(product_ids[0]),
                                   0, -1, desc=true_[:max_result]
        else:
            flat_ids = ''.join([(str(id)] for id product_ids)
            tmp_key = f'm'

