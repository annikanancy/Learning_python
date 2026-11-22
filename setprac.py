form_a = ["Riya", "Kabir", "Ananya", "Riya", "Dev"]
form_b = ["Dev", "Meera", "Kabir", "Jaya"]

def clean_guest_list(form_a, form_b):
    set_a = set(form_a)
    set_b = set(form_b)
    guests = set_a | set_b
    return guests
print(clean_guest_list(form_a, form_b))