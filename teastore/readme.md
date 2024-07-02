# TeaStore cohesion

This project contains logs retrieved from the TeaStore application

## Calculate cohesion

In the folder `test_data` there are some sample logs available for each microservice.

Note, that the `cohesion_calculator` library has to be installed - currently only available locally. Follow instructions in `scom\readme.md` to use the library locally.

The file `scom_for_teastore.py` contains some sample code to retrieve cohesion values as well as additional information like grouped logs and number of calls for each database table per url. Run with `python scom_for_teastore.py`.

### SCOM Results

Mit Berücksichtigung aller Calls

#### JaegerUI

Cohesion for Service tools.descartes.teastore.auth: 0.31525407385980136
Grouped logs for auth.json: {'tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']}

Cohesion for Service tools.descartes.teastore.image: 1.0
Grouped logs for image.json: {'tools.descartes.teastore.image/rest/image/getProductImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.image/rest/image/getWebImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Cohesion for Service tools.descartes.teastore.persistence: 0.3333333333333333
Grouped logs for persistence.json: {'tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER']}

Cohesion for Service tools.descartes.teastore.recommender: Undefined (There are too few endpoints to calculate SCOM)
Grouped logs for recommender.json: {'tools.descartes.teastore.recommender/rest/recommend/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Cohesion for Service tools.descartes.teastore.registry: Undefined (There are too few endpoints to calculate SCOM)
Grouped logs for registry.json: {}

Cohesion for Service tools.descartes.teastore.webui: 0.33893696841649057
Grouped logs for webui.json: {'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/cart/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY']}

#### GRPC

Cohesion for Service tools.descartes.teastore.auth: 0.31586706579290386
Grouped logs for auth.json: {'tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']}

Cohesion for Service tools.descartes.teastore.image: 1.0
Grouped logs for image.json: {'tools.descartes.teastore.image/rest/image/getProductImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.image/rest/image/getWebImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Cohesion for Service tools.descartes.teastore.persistence: 0.11866372228415054
Grouped logs for persistence.json: {'tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/generatedb/finished/': ['DATABASEMANAGEMENTENTITY'], 'tools.descartes.teastore.persistence/rest/products/category/': ['PERSISTENCEPRODUCT'], 'tools.descartes.teastore.persistence/rest/orders/': ['PERSISTENCEORDER'], 'tools.descartes.teastore.persistence/rest/orderitems/': ['PERSISTENCEUSER', 'PERSISTENCEPRODUCT', 'PERSISTENCEORDER', 'PERSISTENCEORDERITEM']}

Cohesion for Service tools.descartes.teastore.recommender: Undefined (There are too few endpoints to calculate SCOM)
Grouped logs for recommender.json: {'tools.descartes.teastore.recommender/rest/recommend/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Cohesion for Service tools.descartes.teastore.registry: Undefined (There are too few endpoints to calculate SCOM)
Grouped logs for registry.json: {}

Cohesion for Service tools.descartes.teastore.webui: 0.3395138762043564
Grouped logs for webui.json: {'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/cart/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'], 'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER'], 'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY'], 'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT']}

### LSCC Results

LSCC Cohesion for Service tools.descartes.teastore.auth: 0.1111111111111111

LSCC Cohesion for Service tools.descartes.teastore.image: 1.0

LSCC Cohesion for Service tools.descartes.teastore.persistence: 0.4

LSCC Cohesion for Service tools.descartes.teastore.recommender: 1

LSCC Cohesion for Service tools.descartes.teastore.registry: Both tables and apis are null

LSCC Cohesion for Service tools.descartes.teastore.webui: 0.25

## Results grpc
