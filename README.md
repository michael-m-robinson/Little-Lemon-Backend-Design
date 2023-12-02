# Little Lemon Meta Project

A project by Michael Robinson

This project demonstrates how a hypothetical restaurant's site might look. This restaurant is the Little Lemon, based out of Chicago. They specialize in Mediterranean cuisine (Italian, Greek, etc). This website allows you to look at the menu and book a reservation if you a logged in. The reservation API itself has no security protecting it, therefore you can access it using tools like insomnia. 

If you wish to try this out please fire up the project, and visit the following link:

   

http://127.0.0.1:8000/api/bookings

to GET reservations, follow this example:

http://127.0.0.1:8000/api/bookings?date=2023-11-30

to POST reservations, follow this example:

http://127.0.0.1:8000/api/bookings/

Fields in json:

```json
{
	"first_name": "Michael Robinson",
	"reservation_date": "2023-12-01",
	"reservation_slot": 10
}
```

If you wish to try out the menu API, please fire up the project, and visit the following link:

http://127.0.0.1:8000/api/menu-items/

To GET a menu item, follow this example:

http://127.0.0.1:8000/api/menu-items/1

to DELETE a menu item, follow this example:

http://127.0.0.1:8000/api/menu-items/1

to POST a menu item, follow this example:

http://127.0.0.1:8000/api/menu-items/

Fields in json:

```json
{
	"title": "Little Lemon Steak",
	"price": 25.4,
	"inventory": 20
}


```

Thanks for looking at my project, and have a nice day. 🤗

