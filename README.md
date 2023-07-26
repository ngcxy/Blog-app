# Blog-app

My website of the blog app: ~~[https://xinyi-blog-backend-d2d1d1896e7c.herokuapp.com/](https://xinyi-blog-frontend-19d2ab0c45dd.herokuapp.com)~~

!! This link is no longer available due to Heroku's removing the free plan.

This project is now deployed on Vercel. You can access it [here](https://my-blog-app-silk.vercel.app/)

---

## Features:

- The Blog app provides a home page that displays all public blogs in thumbnail cards:
![Screen Shot 2023-07-25 at 11 08 23 PM](https://github.com/ngcxy/Blog-app/assets/75980578/30281ffb-b125-4322-a939-2f77728a76b6)


- Clicking on a card allows users to view the specific content of the blog, along with its title and excerpt:
![Screen Shot 2023-07-25 at 11 09 16 PM](https://github.com/ngcxy/Blog-app/assets/75980578/3649fcc2-9167-4a33-9569-83c2b7d7e642)


- Users have the option to create an account, log in, and log out:
![Screen Shot 2023-07-25 at 11 09 52 PM](https://github.com/ngcxy/Blog-app/assets/75980578/f472ae5d-c624-4b54-aee0-741c488469fe)
![Screen Shot 2023-07-25 at 11 10 08 PM](https://github.com/ngcxy/Blog-app/assets/75980578/7677744c-18fd-4511-8fa3-1ef7a08f64e5)

- They can manage their blogs by creating, editing, and deleting them on the admin panel:
![IMG_6115](https://github.com/ngcxy/Blog-app/assets/75980578/3a7e675d-33cd-47dd-80ff-73fda4116cfe)
![Screen Shot 2023-07-25 at 11 15 05 PM](https://github.com/ngcxy/Blog-app/assets/75980578/0742ae01-8011-416e-a72e-d3e982591eab)


## Tools

- **Frontend**: Built with React.js, **Backend server**: Powered by Django
- Database: Postgresql (with [supabase](https://supabase.com/))
- Database for image: AWS S3
- User authentication: JWT token
- React ui library: [Material UI](https://mui.com/)

## Getting Started

To run the project locally, follow these steps:
1. Clone the repository
2. For the frontend, you need to change the url of the backend to local, for example: http://127.0.0.1:8000
3. Cd to blogreact, then run `npm install`
4. Run `npm start` to start the app


