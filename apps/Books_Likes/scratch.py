Users.objects.create(first_name="Jon", last_name="Bones", email="jon@yahoo.com")
Users.objects.create(first_name="Brandy", last_name="Johnson", email="brandy@yahoo.com")
Users.objects.create(first_name="James", last_name="Feeney", email="james@yahoo.com"

user3 = Books.objects.create(name = "CSS", desc="front-end language", uploaded = Users.objects.get(id=11))

user3 = Users.objects.get(id=11)
all_books = Books.objects.all()
for bo in all_books:
    Likes.objects.create(user=user3, book=bo)
like1 = Likes.objects.create(user=user2, book=book1)

book1 =Likes.objects.filter(book=Books.objects.first())
print book1

book2 =Likes.objects.filter(book=Books.objects.get(id=3))
print book2

book1 =Books.objects.get(id=3)
print book1.uploaded.first_name
