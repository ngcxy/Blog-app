## React
- use material ui (mui)
  - useStyles to customize style
- use simple JWT, along with axios to authenticate (log in service provided in django)
	- access and refresh tokens
	- this should be listed in the Django part?
- Create own user table and admin part of it?

## Django
- django cors headers
  - to allow in-web communication
- use postman to track and test the end-to-end communication
- permission setting on project, view level
  - custom permission: only one creating it can delete it
- authentication based on JWT token via simple JWT
- ModalViewSet  一种wrapped, integrated集成的viewset， 提供多种已经编好的数据处理的api
- schema page via pyyaml, and to put it into a nice interface

## To learn
- react life cycle
- testing in each part (skipped)
- django generics and viewset?
- in Django different app?

## The HARDEST part

- use JWT token to manage user authentication, and get & post the access token and refresh token via axios
  - I faced with so many errors: No. 404, 400, 401(not authorized appears most), 500 ......
  - access token and refresh token have different functions and different lifetime, easy to confuse
  - expire
  - when logging out, we need to blacklist the access token, but we also need to refresh the access token?
- how solved? I used console.log() to debug line by line to figure out how these tokens work. I also watched videos about JWT to learn how exactly JWT tokens work.

## To Do
- [ ] after log in, hi XXX
- [ ] add a successfully-logged-out page for logout
- [ ] modify the single post page
- [ ] search: backend finished, but frontend has some problem on the searchBar
- [ ] what to do when access token expires?
- [ ] log in, if info is not right
