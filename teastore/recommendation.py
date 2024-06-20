from cohesion_calculator import cohesion
from cohesion_calculator import log
import json

#files = ["auth_050624.json", "image_050624.json", "persistence_050624.json", "recommender_050624.json", "registry_050624.json", "webui_050624.json"]
files = ["auth_090624.json", "image_090624.json", "persistence_090624.json", "recommender_090624.json", "registry_090624.json", "webui_090624.json"]
service_names = ["tools.descartes.teastore.auth", "tools.descartes.teastore.image", "tools.descartes.teastore.persistence", "tools.descartes.teastore.recommender", "tools.descartes.teastore.registry", "tools.descartes.teastore.webui"]

auth_logs = {
'tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']
}

auth_calls = {
'tools.descartes.teastore.auth/rest/useractions/isloggedin/': 11886,
'tools.descartes.teastore.auth/rest/cart/add/': 829,
'tools.descartes.teastore.auth/rest/useractions/logout/': 249,
}

print(f"Authentication without weights: {cohesion.scom(auth_logs, auth_calls, False)}")
print(f"Authentication with weights: {cohesion.scom(auth_logs, auth_calls, True)}")

persistence_logs = {
'tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.persistence/rest/products/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'],
'tools.descartes.teastore.persistence/rest/products/count/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY']}

persistence_calls = {
'tools.descartes.teastore.persistence/rest/categories/': 8468,
'tools.descartes.teastore.persistence/rest/products/': 4997,
'tools.descartes.teastore.persistence/rest/products/category/': 110,
'tools.descartes.teastore.persistence/rest/products/count/': 264}

print(f"Persistence without weights: {cohesion.scom(persistence_logs, persistence_calls, False)}")
print(f"Persistence with weights: {cohesion.scom(persistence_logs, persistence_calls, True)}")


webui_logs = {
'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.webui/cart/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT']}

webui_calls = {
'tools.descartes.teastore.webui/category/': 1331,
'tools.descartes.teastore.webui/': 805,
'tools.descartes.teastore.webui/profile/': 177,
'tools.descartes.teastore.webui/login/': 550,
'tools.descartes.teastore.webui/cartAction/': 607,
'tools.descartes.teastore.webui/product/': 2353,
'tools.descartes.teastore.webui/cart/': 2431,
'tools.descartes.teastore.webui/order/': 145}

print(f"WebUI without weights: {cohesion.scom(webui_logs, webui_calls, False)}")
print(f"WebUI with weights: {cohesion.scom(webui_logs, webui_calls, True)}")

new_logs = { 'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'], 
            'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'],
            'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER']}

new_calls = {'tools.descartes.teastore.auth/rest/useractions/login/': 486, 
             'tools.descartes.teastore.persistence/rest/users/name/': 576,
             'tools.descartes.teastore.webui/loginAction/': 516
             }

print(f"New service without weights: {cohesion.scom(new_logs, new_calls, False)}")
print(f"New service with weights: {cohesion.scom(new_logs, new_calls, True)}")