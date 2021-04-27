role =input()

is_admin = role == "Admin"
is_secondary_admin = role == "Secondary admin"
is_user = role == "User"

if is_admin:
    print("Hello admin")
elif is_secondary_admin:
    print("Hello, you don't have full rights")
elif is_user:
    print("Hello, you can't open this page")
