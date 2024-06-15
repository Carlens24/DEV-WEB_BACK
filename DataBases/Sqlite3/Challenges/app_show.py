import app

app.add_one('Zumbi', 'Dandara', 'zumbidandara@gmail.com')

app.remove_one('Maria')

many = [
    ('Nanda', 'pyhol', 'nandapyhol@gmail.com'),
    ('danoel', 'pratchul', 'danoelpatchul@gmail.com')
]

app.many(many)

app.show_app()
