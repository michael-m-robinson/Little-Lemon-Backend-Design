# Little Lemon Meta Project

A project by Michael Robinson

This project shows how a hypothetical restaurant's site might look. This restaurant is the Little Lemon, based out of Chicago. They specialize in Mediterranean cuisine (Italian, Greek, etc). This website allows you to look at the menu and book a reservation if you a logged in. The reservation API itself has no security protecting it, therefore you can access it using tools like insomnia. 

This project has two notable APIs: the booking API and the menu API. 

### Booking API

Please note, to use the booking API, you must have a registered account in the system. Once registered, send a GET method with your username and password to the following address: /auth/token/login. Doing so will provide a token to use with the API. 

With the bearer token, you can test out the booking API using insomnia or your preferred rest client, fire up the project and use the following examples to guide your evaluation.

#### Get Reservation

GET http://yourserver/api/bookings/{primary key}

#### Make a Reservation

POST http://yourserver/api/bookings/

Fields in Json:

```json
{
	"first_name": "Michael Robinson",
	"reservation_date": "2023-12-01",
	"reservation_slot": 10
}
```

#### Get Reservations

GET http://yourserver/api/bookings/

#### Get Reservations by date

http://yourserver/api/bookings/2023/12/3/

### Menu API

Please note that the menu API requires you to be a super user for certain functions, like creating a menu item. Once you've created a superuser account, send a GET method with your username and password to the following address: /auth/token/login. Doing so will provide a token to use with the API.

#### Get all menu items

http://127.0.0.1:8000/api/menu-items/

#### Get a menu item

http://127.0.0.1:8000/api/menu-items/1

#### Delete a menu item

http://127.0.0.1:8000/api/menu-items/1

#### Create a menu item

http://127.0.0.1:8000/api/menu-items/

Fields in json:

```json
{
	"name": "Little Lemon Steak",
	"price": 25.4,
	"inventory": 20
}


```

Thanks for looking at my project, and have a nice day. 🤗

