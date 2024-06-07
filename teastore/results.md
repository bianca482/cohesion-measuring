### Auth

Cohesion for Service auth: 0.3333333333333333

Grouped logs for auth_050624.json: {'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']}

Number of calls for auth_050624.json: {'tools.descartes.teastore.auth/rest/useractions/login/': {'PERSISTENCEUSER': 107}, 'tools.descartes.teastore.auth/rest/useractions/isloggedin/': {'PERSISTENCECATEGORY': 1065, 'PERSISTENCEPRODUCT': 579}, 'tools.descartes.teastore.auth/rest/cart/add/': {'PERSISTENCEPRODUCT': 32}}

### Image

Cohesion for Service image: 1.0

Grouped logs for image_050624.json: {'tools.descartes.teastore.image/rest/image/getWebImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.image/rest/image/getProductImages/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY']}

Number of calls for image_050624.json: {'tools.descartes.teastore.image/rest/image/getWebImages/': {'PERSISTENCECATEGORY': 880, 'PERSISTENCEPRODUCT': 168}, 'tools.descartes.teastore.image/rest/image/getProductImages/': {'PERSISTENCEPRODUCT': 570, 'PERSISTENCECATEGORY': 572}}

### Persistence

Cohesion for Service persistence: 0.6

Grouped logs for persistence_050624.json: {'tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/products/count/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.persistence/rest/products/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY']}

Number of calls for persistence_050624.json: {'tools.descartes.teastore.persistence/rest/categories/': {'PERSISTENCECATEGORY': 844, 'PERSISTENCEPRODUCT': 467}, 'tools.descartes.teastore.persistence/rest/users/name/': {'PERSISTENCEUSER': 107}, 'tools.descartes.teastore.persistence/rest/products/': {'PERSISTENCECATEGORY': 190, 'PERSISTENCEPRODUCT': 78}, 'tools.descartes.teastore.persistence/rest/products/count/': {'PERSISTENCEPRODUCT': 46, 'PERSISTENCECATEGORY': 23}, 'tools.descartes.teastore.persistence/rest/products/category/': {'PERSISTENCEPRODUCT': 20, 'PERSISTENCECATEGORY': 10}}

### Recommender

Cohesion for Service recommender: Too few endpoints

Grouped logs for recommender_050624.json: {'tools.descartes.teastore.recommender/rest/recommend/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Number of calls for recommender_050624.json: {'tools.descartes.teastore.recommender/rest/recommend/': {'PERSISTENCECATEGORY': 1356, 'PERSISTENCEPRODUCT': 249}}

### Registry

Cohesion for Service registry: Too few endpoints

Grouped logs for registry_050624.json: {'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Number of calls for registry_050624.json: {'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image/': {'PERSISTENCECATEGORY': 39, 'PERSISTENCEPRODUCT': 4}}

### Webui

Cohesion for Service webui: 0.6428571428571429

Grouped logs for webui_050624.json: {'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/cart/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER']}

Number of calls for webui_050624.json: {'tools.descartes.teastore.webui/login/': {'PERSISTENCECATEGORY': 167}, 'tools.descartes.teastore.webui/category/': {'PERSISTENCEPRODUCT': 430, 'PERSISTENCECATEGORY': 215}, 'tools.descartes.teastore.webui/cart/': {'PERSISTENCEPRODUCT': 41, 'PERSISTENCECATEGORY': 170}, 'tools.descartes.teastore.webui/product/': {'PERSISTENCECATEGORY': 164, 'PERSISTENCEPRODUCT': 18}, 'tools.descartes.teastore.webui/cartAction/': {'PERSISTENCEPRODUCT': 28}, 'tools.descartes.teastore.webui/order/': {'PERSISTENCECATEGORY': 23}, 'tools.descartes.teastore.webui/': {'PERSISTENCECATEGORY': 115}, 'tools.descartes.teastore.webui/loginAction/': {'PERSISTENCEUSER': 93}}
