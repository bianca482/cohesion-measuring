# TeaStore cohesion

This project contains logs retrieved from the TeaStore application

## Calculate cohesion

In the folder `test_data` there are some sample logs available for each microservice.

Note, that the `cohesion_calculator` library has to be installed - currently only available locally. Follow instructions in `scom\readme.md` to use the library locally.

The file `scom_for_teastore.py` contains some sample code to retrieve cohesion values as well as additional information like grouped logs and number of calls for each database table per url. Run with `python scom_for_teastore.py`.

## Results

Mit Berücksichtigung aller Calls

### Auth

Cohesion for Service tools.descartes.teastore.auth: 0.3151177199504337

Grouped logs for auth_090624.json: {
'tools.descartes.teastore.auth/rest/useractions/isloggedin/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'],
'tools.descartes.teastore.auth/rest/cart/add/': ['PERSISTENCEPRODUCT']}

Number of endpoint calls: {
'tools.descartes.teastore.auth/rest/useractions/isloggedin/': 11886,
'tools.descartes.teastore.auth/rest/cart/add/': 829,
'tools.descartes.teastore.auth/rest/useractions/logout/': 249,
'tools.descartes.teastore.auth/rest/useractions/login/': 486}

### Image

Cohesion for Service tools.descartes.teastore.image: 1.0

Grouped logs for image_090624.json: {
'tools.descartes.teastore.image/rest/image/getProductImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.image/rest/image/getWebImages/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Number of endpoint calls: {
'tools.descartes.teastore.image/rest/image/getProductImages/': 8257,
'tools.descartes.teastore.image/rest/image/getWebImages/': 8274}

### Persistence

Cohesion for Service tools.descartes.teastore.persistence: 0.288012486992716

Grouped logs for persistence_090624.json: {
'tools.descartes.teastore.persistence/rest/categories/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.persistence/rest/products/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'],
'tools.descartes.teastore.persistence/rest/products/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'],
'tools.descartes.teastore.persistence/rest/products/count/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY']}

Number of endpoint calls: {
'tools.descartes.teastore.persistence/rest/categories/': 8468,
'tools.descartes.teastore.persistence/rest/products/': 4997,
'tools.descartes.teastore.persistence/rest/users/name/': 576,
'tools.descartes.teastore.persistence/rest/products/category/': 110,
'tools.descartes.teastore.persistence/rest/products/count/': 264}

### Recommender

Cohesion for Service tools.descartes.teastore.recommender: Too few endpoints

Grouped logs for recommender_090624.json: {
'tools.descartes.teastore.recommender/rest/recommend/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT']}

Number of endpoint calls: {
'tools.descartes.teastore.recommender/rest/recommend/': 23667}

### Registry

Cohesion for Service tools.descartes.teastore.registry: Too few endpoints

Grouped logs for registry_090624.json: {}

Number of endpoint calls: {
'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.auth/': 116, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.persistence/': 462, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.recommender/recommender:8080/': 116, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.persistence/persistence:8080/': 116, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.recommender/': 230, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.webui/webui:8080/': 115, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.auth/auth:8080/': 115, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image/image:8080/': 115, 'tools.descartes.teastore.registry/rest/services/tools.descartes.teastore.image/': 115}

### Webui

Cohesion for Service tools.descartes.teastore.webui: 0.1843241727425687

Grouped logs for webui_090624.json: {
'tools.descartes.teastore.webui/category/': ['PERSISTENCEPRODUCT', 'PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/': ['PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/login/': ['PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/product/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER'],
'tools.descartes.teastore.webui/cart/': ['PERSISTENCECATEGORY', 'PERSISTENCEPRODUCT'],
'tools.descartes.teastore.webui/order/': ['PERSISTENCECATEGORY'],
'tools.descartes.teastore.webui/cartAction/': ['PERSISTENCEPRODUCT']}

Number of endpoint calls: {
'tools.descartes.teastore.webui/category/': 1331,
'tools.descartes.teastore.webui/': 805,
'tools.descartes.teastore.webui/login/': 550,
'tools.descartes.teastore.webui/profile/': 177,
'tools.descartes.teastore.webui/loginAction/': 516,
'tools.descartes.teastore.webui/cartAction/': 607,
'tools.descartes.teastore.webui/product/': 2353,
'tools.descartes.teastore.webui/cart/': 2431,
'tools.descartes.teastore.webui/order/': 145}
