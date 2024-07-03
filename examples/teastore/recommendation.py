from cohesion_calculator import cohesion

files = ["auth.json", "image.json", "persistence.json", "recommender.json", "registry.json", "webui.json"]
service_names = ["tools.descartes.teastore.auth", "tools.descartes.teastore.image", "tools.descartes.teastore.persistence", "tools.descartes.teastore.recommender", "tools.descartes.teastore.registry", "tools.descartes.teastore.webui"]
path = "../grpc/"

auth_logs = {
    'tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
    'tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']
}


auth_calls = {
    'tools.descartes.teastore.auth/rest/cart/add/': 13040, 
    'tools.descartes.teastore.auth/rest/useractions/isloggedin/': 197788, 
}

print(f"Authentication without weights: {cohesion.scom(auth_logs, auth_calls, False)}")
print(f"Authentication with weights: {cohesion.scom(auth_logs, auth_calls, True)}")

persistence_logs = {  
    'tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 
    'tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 
    'tools.descartes.teastore.persistence/rest/generatedb/finished/': ['DATABASEMANAGEMENTENTITY'], 
    'tools.descartes.teastore.persistence/rest/products/category/': ['PERSISTENCEPRODUCT'], 
    'tools.descartes.teastore.persistence/rest/orders/': ['PERSISTENCEORDER'], 
    'tools.descartes.teastore.persistence/rest/orderitems/': ['PERSISTENCEUSER', 'PERSISTENCEPRODUCT', 'PERSISTENCEORDER', 'PERSISTENCEORDERITEM']
}

persistence_calls = {
    'tools.descartes.teastore.persistence/rest/categories/': 133268, 
    'tools.descartes.teastore.persistence/rest/products/': 73980, 
    'tools.descartes.teastore.persistence/rest/generatedb/finished/': 28, 
    'tools.descartes.teastore.persistence/rest/products/category/': 20, 
    'tools.descartes.teastore.persistence/rest/orders/': 4, 
    'tools.descartes.teastore.persistence/rest/orderitems/': 928
} 

print(f"Persistence without weights: {cohesion.scom(persistence_logs, persistence_calls, False)}")
print(f"Persistence with weights: {cohesion.scom(persistence_logs, persistence_calls, True)}")

webui_logs = {
    'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 
    'tools.descartes.teastore.webui/cart/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 
    'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'], 
    'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'], 
    'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 
    'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY'], 
    'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT']
}

webui_calls = {
    'tools.descartes.teastore.webui/product/': 61940, 
    'tools.descartes.teastore.webui/cart/': 60940, 
    'tools.descartes.teastore.webui/cartAction/': 14232, 
    'tools.descartes.teastore.webui/': 18736, 
    'tools.descartes.teastore.webui/profile/': 3588, 
    'tools.descartes.teastore.webui/login/': 13500, 
    'tools.descartes.teastore.webui/category/': 36128, 
    'tools.descartes.teastore.webui/order/': 2960
}

print(f"WebUI without weights: {cohesion.scom(webui_logs, webui_calls, False)}")
print(f"WebUI with weights: {cohesion.scom(webui_logs, webui_calls, True)}")


new_logs = {
    'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'], 
    'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'],
    'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER']
}

new_calls = {
    'tools.descartes.teastore.auth/rest/useractions/login/': 8100,
    'tools.descartes.teastore.persistence/rest/users/name/': 8100, 
    'tools.descartes.teastore.webui/loginAction/': 11658
}

print(f"New service without weights: {cohesion.scom(new_logs, new_calls, False)}")
print(f"New service with weights: {cohesion.scom(new_logs, new_calls, True)}")