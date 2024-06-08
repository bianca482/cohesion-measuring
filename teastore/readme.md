# TeaStore cohesion

This project contains logs retrieved from the TeaStore application

## Calculate cohesion

In the folder `test_data` there are some sample logs available for each microservice.

Note, that the `cohesion_calculator` library has to be installed - currently only available locally. Follow instructions in `scom\readme.md` to use the library locally.

The file `scom_for_teastore.py` contains some sample code to retrieve cohesion values as well as additional information like grouped logs and number of calls for each database table per url. Run with `python scom_for_teastore.py`.

## Results

### Auth

Cohesion for Service auth: 0.3333333333333333

Grouped logs for auth_050624.json: {'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']}

Number of calls per table: {'tools.descartes.teastore.auth/rest/useractions/login/': {'PERSISTENCEUSER': 107}, 'tools.descartes.teastore.auth/rest/useractions/isloggedin/': {'PERSISTENCECATEGORY': 1065, 'PERSISTENCEPRODUCT': 579}, 'tools.descartes.teastore.auth/rest/cart/add/': {'PERSISTENCEPRODUCT': 32}}

Number of endpoint calls: {'tools.descartes.teastore.auth/rest/useractions/login/': 642, 'tools.descartes.teastore.auth/rest/cart/add/': 912, 'tools.descartes.teastore.auth/rest/useractions/isloggedin/': 12581, 'tools.descartes.teastore.auth/rest/useractions/logout/': 120, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.auth/auth:8080/': 5}

### Image

Cohesion for Service image: 1.0

Grouped logs for image_050624.json: {'tools.descartes.teastore.image/rest/image/getWebImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.image/rest/image/getProductImages/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY']}

Number of calls per table: {'tools.descartes.teastore.image/rest/image/getWebImages/': {'PERSISTENCECATEGORY': 880, 'PERSISTENCEPRODUCT': 168}, 'tools.descartes.teastore.image/rest/image/getProductImages/': {'PERSISTENCEPRODUCT': 570, 'PERSISTENCECATEGORY': 572}}

Number of endpoint calls: {'tools.descartes.teastore.image/rest/image/getWebImages/': 7838, 'tools.descartes.teastore.image/rest/image/getProductImages/': 8715, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image/image:8080/': 24}

### Persistence

Cohesion for Service persistence: 0.6

Grouped logs for persistence_050624.json: {'tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/products/count/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.persistence/rest/products/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY']}

Number of calls per table: {'tools.descartes.teastore.persistence/rest/categories/': {'PERSISTENCECATEGORY': 844, 'PERSISTENCEPRODUCT': 467}, 'tools.descartes.teastore.persistence/rest/users/name/': {'PERSISTENCEUSER': 107}, 'tools.descartes.teastore.persistence/rest/products/': {'PERSISTENCECATEGORY': 190, 'PERSISTENCEPRODUCT': 78}, 'tools.descartes.teastore.persistence/rest/products/count/': {'PERSISTENCEPRODUCT': 46, 'PERSISTENCECATEGORY': 23}, 'tools.descartes.teastore.persistence/rest/products/category/': {'PERSISTENCEPRODUCT': 20, 'PERSISTENCECATEGORY': 10}}

Number of endpoint calls: {'tools.descartes.teastore.persistence/rest/products/': 4477, 'tools.descartes.teastore.persistence/rest/categories/': 8497, 'tools.descartes.teastore.persistence/rest/users/name/': 642, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.persistence/persistence:8080/': 103, 'tools.descartes.teastore.persistence/rest/products/count/': 253, 'tools.descartes.teastore.persistence/rest/products/category/': 110}

### Recommender

Cohesion for Service recommender: Too few endpoints

Grouped logs for recommender_050624.json: {'tools.descartes.teastore.recommender/rest/recommend/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Number of calls per table: {'tools.descartes.teastore.recommender/rest/recommend/': {'PERSISTENCECATEGORY': 1356, 'PERSISTENCEPRODUCT': 249}}

Number of endpoint calls: {'tools.descartes.teastore.recommender/rest/recommend/': 25992, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.recommender/': 47, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.recommender/recommender:8080/': 47}

### Registry

Cohesion for Service registry: Too few endpoints

Grouped logs for registry_050624.json: {'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Number of calls per table: {'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image/': {'PERSISTENCECATEGORY': 39, 'PERSISTENCEPRODUCT': 4}}

Number of endpoint calls: {'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.persistence/': 1763, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image/': 500, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.webui/webui:8080/': 103, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.auth/auth:8080/': 102, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.recommender/': 193, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.auth/': 102, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.persistence/persistence:8080/': 99, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image/image:8080/': 91, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.recommender/recommender:8080/': 91}

### Webui

Cohesion for Service webui: 0.6428571428571429

Grouped logs for webui_050624.json: {'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/cart/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER']}

Number of calls per table: {'tools.descartes.teastore.webui/login/': {'PERSISTENCECATEGORY': 167}, 'tools.descartes.teastore.webui/category/': {'PERSISTENCEPRODUCT': 430, 'PERSISTENCECATEGORY': 215}, 'tools.descartes.teastore.webui/cart/': {'PERSISTENCEPRODUCT': 41, 'PERSISTENCECATEGORY': 170}, 'tools.descartes.teastore.webui/product/': {'PERSISTENCECATEGORY': 164, 'PERSISTENCEPRODUCT': 18}, 'tools.descartes.teastore.webui/cartAction/': {'PERSISTENCEPRODUCT': 28}, 'tools.descartes.teastore.webui/order/': {'PERSISTENCECATEGORY': 23}, 'tools.descartes.teastore.webui/': {'PERSISTENCECATEGORY': 115}, 'tools.descartes.teastore.webui/loginAction/': {'PERSISTENCEUSER': 93}}

Number of endpoint calls: {'tools.descartes.teastore.webui/login/': 835, 'tools.descartes.teastore.webui/category/': 2365, 'tools.descartes.teastore.webui/cart/': 3174, 'tools.descartes.teastore.webui/product/': 3134, 'tools.descartes.teastore.webui/cartAction/': 758, 'tools.descartes.teastore.webui/order/': 115, 'tools.descartes.teastore.webui/': 575, 'tools.descartes.teastore.webui/loginAction/': 660, 'tools.descartes.teastore.webui/profile/': 135, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.webui/webui:8080/': 56}
