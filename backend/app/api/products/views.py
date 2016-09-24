""" This file contains views associated with this module """

from __future__ import absolute_import, division, print_function    # Python 3 features

from flask_restful import Resource, reqparse

from .models import *
class Products(Resource):

    def get(self):
        product_list = []
        try:
            for product in Product.objects():
                product_list.append({'_id': str(product.id), 'title': product.name})
            return product_list
        except Exception as e:
            return build_error_message((e))


    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument(
            'productName', type=str, location='json', required=True)
        parse.add_argument(
            'productURL', type=str, location='json', required=False)

        args = parse.parse_args()
        name, product_url = args['productName'], args['productURL']
        try:
            query = {'name':name}
            result = Product.objects(**query).update(
                set__name=name,
                set__callback_url=product_url,
                upsert=True,
                full_result=True
            )
            product_reference=Product.objects(**query).get()
            print(product_reference.callback_url)
            ret_status = (fetch_save_action_schemas(product_reference=product_reference, product_url=product_reference.callback_url, productName=name))
            if ret_status["status"] == "ERROR":
                return ret_status


        except Exception as e:
            print("Product update error")
            return build_error_message("Error during the operation: {}".format(e))
        print("calling fetch_save_action_schemas")


        return build_success_message("Added the Product {!r}".format(name))

    def delete(self):
        try:
            Product.objects().delete()
            return build_success_message("All Products deleted successfully")
        except Exception as e:
            return build_error_message("Unable to delete products {}".format(e))



class ProductDetails(Resource):

    def get(self, productName):
        try:
            product = Product.objects.get(name=productName)
            return {'name': str(product.name), 'description': product.description}
        except Exception as e:
            return build_error_message("Error during the operation: {}".format(e))

    def delete(self, productName):
        print(productName)
        try:
            Product.objects(name=productName).delete()
            return build_success_message("Product name: {} deleted successfully".format(productName))
        except Exception as e:
            return build_error_message("Unable to delete product - Product name: {}".format(productName))


class ProductActionSchemas(Resource):

    def get(self, productName):
        try:
            action_list = []
            for action_schema in ActionSchema.objects(productName=productName):
                action_list.append({'name': str(action_schema.name), 'productName': str(action_schema.productName),
                                    'schemaID': str(action_schema.id)})
            return (action_list)
        except Exception as e:
            return build_error_message("Error during the operation: {}".format(e))
