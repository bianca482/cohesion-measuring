Cohesion for Service auth: 0.3333333333333333
Grouped logs for auth_050624.json:
{'/tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'],
'/tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'/tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']

}
Cohesion for Service image: 1.0
Grouped logs for image_050624.json:
{'/tools.descartes.teastore.image/rest/image/getWebImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'/tools.descartes.teastore.image/rest/image/getProductImages/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY']
}

Cohesion for Service persistence: 0.6
Grouped logs for persistence_050624.json:
{'/tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'/tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'],
'/tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'/tools.descartes.teastore.persistence/rest/products/category/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'/tools.descartes.teastore.persistence/rest/products/count/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY']
}

Cohesion for Service recommender: Too few endpoints
Grouped logs for recommender_050624.json: {
'/tools.descartes.teastore.recommender/rest/recommend/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']
}

Cohesion for Service registry: Too few endpoints
Grouped logs for registry_050624.json: {
'/tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image//': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']
}

Cohesion for Service webui: 0.6428571428571429
Grouped logs for webui_050624.json:
{'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/cart/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT'],
'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER']
}
