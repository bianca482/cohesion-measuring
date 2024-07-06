# TeaStore cohesion

This project contains logs retrieved from the TeaStore application

## Calculate cohesion

Note, that the `cohesion_calculator` library has to be installed - currently only available locally. Follow instructions in `scom\readme.md` to use the library locally.

The file `scom_for_teastore.py` contains some sample code to retrieve cohesion values as well as additional information like grouped logs and number of calls for each database table per url. Run with `python scom_for_teastore.py`. This file assumes that there are sample logs for each service in a folder named `test_data`. To get data for each service, start the TeaStore application and make calls, for example with the locust file provided like described in the documentation of the repository.

### SCOM Results - GRPC (mit Gewichtung)

#### Auth

Cohesion for Service tools.descartes.teastore.auth: 0.31586706579290386

Grouped logs for auth.json: {'tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']}

Number of endpoint calls: {'tools.descartes.teastore.auth/rest/cart/add/': 13040, 'tools.descartes.teastore.auth/rest/useractions/isloggedin/': 197788, 'tools.descartes.teastore.auth/rest/useractions/login/': 8100, 'tools.descartes.teastore.auth/rest/useractions/logout/': 3558}

#### Image

Cohesion for Service tools.descartes.teastore.image: 1.0

Grouped logs for image.json: {'tools.descartes.teastore.image/rest/image/getProductImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.image/rest/image/getWebImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Number of endpoint calls: {'tools.descartes.teastore.image/rest/image/getProductImages/': 98064, 'tools.descartes.teastore.image/rest/image/getWebImages/': 96120}

#### Persistence

Cohesion for Service tools.descartes.teastore.persistence: 0.11866372228415054

Grouped logs for persistence.json: {'tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/generatedb/finished/': ['DATABASEMANAGEMENTENTITY'], 'tools.descartes.teastore.persistence/rest/products/category/': ['PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/orders/': ['PERSISTENCEORDER'], 'tools.descartes.teastore.persistence/rest/orderitems/': ['PERSISTENCEUSER', 'PERSISTENCEPRODUCT', 'PERSISTENCEORDER', 'PERSISTENCEORDERITEM']}

Number of endpoint calls: {'tools.descartes.teastore.persistence/rest/categories/': 133268, 'tools.descartes.teastore.persistence/rest/users/name/': 8100, 'tools.descartes.teastore.persistence/rest/products/': 73980, 'tools.descartes.teastore.persistence/rest/generatedb/finished/': 28, 'tools.descartes.teastore.persistence/rest/products/category/': 20, 'tools.descartes.teastore.persistence/rest/orders/': 4, 'tools.descartes.teastore.persistence/rest/orderitems/': 928}

#### Recommender

Cohesion for Service tools.descartes.teastore.recommender: Undefined (There are too few endpoints to calculate SCOM)

Grouped logs for recommender.json: {'tools.descartes.teastore.recommender/rest/recommend/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

#### Registry

Cohesion for Service tools.descartes.teastore.registry: Undefined (There are too few endpoints to calculate SCOM)

Grouped logs for registry.json: {}

#### WebUI

Cohesion for Service tools.descartes.teastore.webui: 0.3395138762043564

Grouped logs for webui.json: {'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/cart/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT']}

Number of endpoint calls: {'tools.descartes.teastore.webui/product/': 61940, 'tools.descartes.teastore.webui/cart/': 60940, 'tools.descartes.teastore.webui/cartAction/': 14232, 'tools.descartes.teastore.webui/': 18736, 'tools.descartes.teastore.webui/profile/': 3588, 'tools.descartes.teastore.webui/loginAction/': 11658, 'tools.descartes.teastore.webui/login/': 13500, 'tools.descartes.teastore.webui/category/': 36128, 'tools.descartes.teastore.webui/order/': 2960}

### SCOM Results - GRPC (ohne Gewichtung)

#### Auth

Cohesion for Service tools.descartes.teastore.auth: 0.3333333333333333

Grouped traces for auth.json: {'tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']}

#### Image

Cohesion for Service tools.descartes.teastore.image: 1.0

Grouped traces for image.json: {'tools.descartes.teastore.image/rest/image/getProductImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.image/rest/image/getWebImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

#### Persistence

Cohesion for Service tools.descartes.teastore.persistence: 0.3333333333333333

Grouped traces for persistence.json: {'tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/generatedb/finished/': ['DATABASEMANAGEMENTENTITY'], 'tools.descartes.teastore.persistence/rest/products/category/': ['PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/orders/': ['PERSISTENCEORDER'], 'tools.descartes.teastore.persistence/rest/orderitems/': ['PERSISTENCEUSER', 'PERSISTENCEPRODUCT', 'PERSISTENCEORDER', 'PERSISTENCEORDERITEM']}

#### Recommender

Cohesion for Service tools.descartes.teastore.recommender: Undefined (There are too few endpoints to calculate SCOM)

Grouped traces for recommender.json: {'tools.descartes.teastore.recommender/rest/recommend/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

#### Registry

Cohesion for Service tools.descartes.teastore.registry: Undefined (There are too few endpoints to calculate SCOM)

Grouped traces for registry.json: {}

#### WebUI

Cohesion for Service tools.descartes.teastore.webui: 0.6428571428571429

Grouped traces for webui.json: {'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/cart/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT']}
