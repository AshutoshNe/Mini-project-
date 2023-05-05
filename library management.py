# Import lib raries
import csv
import tkinter as tk
from ttkthemes import ThemedStyle
import tkinter.messagebox as messagebox


# Define global variables
root = None
title_var = None
author_var = None
publisher_var = None
pub_date_var = None
isbn_var = None
search_var = None
results_listbox = None
username_var = None  # Declare as global variable
password_var = None  # Declare as global variable 

bg_color = "#F8F9FB"
button_bg_color = "#4CAF50"
button_fg_color = "white"

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [row for row in reader]
    return headers, data

def write_csv(filename, headers, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# Define functions to display different pages
def display_home():
    # Remove existing content from main content frame
    for child in main_content_frame.winfo_children():
        child.destroy()
    
    # Image
    image = tk.PhotoImage(file="library_image.png")
    image_label = tk.Label(main_content_frame, image=image, bg=bg_color,height=730,width=1000)
    image_label.image = image
    image_label.grid(row=0,column=0,rowspan=7)
    image_label.grid_propagate(0)


    # Main title
    title_label = tk.Label(main_content_frame, text="Welcome to the Library Management System", font=("Arial", 28), bg=bg_color)
    title_label.grid(row=0,column=0,pady=20)

    
    
    # Description
    description_label = tk.Label(main_content_frame, text="Our library is committed to providing access to quality resources and services that meet the educational, informational, and recreational needs of our diverse community. We offer a wide range of materials and programs for all ages, including books, magazines, DVDs, and online databases. Our knowledgeable staff is always on hand to assist with research and reference questions, and we also provide computer and internet access for public use.", font=("Arial", 16), bg=bg_color, wraplength=800)
    description_label.grid(row=1,column=0,pady=20)

    # Contact information
    contact_label = tk.Label(main_content_frame, text="Contact us:", font=("Arial", 16), bg=bg_color)
    contact_label.grid(row=2,column=0,pady=(50, 20))
    phone_label = tk.Label(main_content_frame, text="Phone: 123-456-7890", font=("Arial", 14), bg=bg_color)
    phone_label.grid(row=3,column=0)
    email_label = tk.Label(main_content_frame, text="Email: library@example.com", font=("Arial", 14), bg=bg_color)
    email_label.grid(row=4,column=0)
    address_label = tk.Label(main_content_frame, text="Address: 123 Main St, Anytown USA", font=("Arial", 14), bg=bg_color)
    address_label.grid(row=5,column=0)


def submit():
    # Retrieve input values from entry boxes and checkboxes
    book_title = book_title_entry.get()
    book_id = book_id_entry.get()
    borrower_name_id = borrower_entry.get()
    date_issued = date_issued_entry.get()
    due_date = due_date_entry.get()
    returned = returned_var.get()

    # Update the Library.csv file with the borrower ID
    headers, data = read_csv('Library.csv')
    
    for row in data:
        if row[5] == book_id and row[0] == book_title:
            row[6] = borrower_name_id
    
    write_csv('Library.csv', headers, data)

    # Reset the input fields
    book_title_entry.delete(0, tk.END)
    book_id_entry.delete(0, tk.END)
    borrower_entry.delete(0, tk.END)
    date_issued_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    returned_checkbox.deselect()


def cancel():
    book_title_entry.delete(0, 'end')
    book_id_entry.delete(0, 'end')
    borrower_entry.delete(0, 'end')
    date_issued_entry.delete(0, 'end')
    due_date_entry.delete(0, 'end')
    returned_var.set(0)
    
def display_issue_book():
    global book_title_entry,book_id_entry,borrower_entry,date_issued_entry,due_date_entry,returned_var
    # Remove existing content from main content frame
    for child in main_content_frame.winfo_children():
        child.destroy()

    # Create labels for book and borrower information
    book_title_label = tk.Label(main_content_frame, text="Book Title:",font=("Arial", 16), bg=bg_color)
    book_title_label.grid(row=0, column=0, padx=50, pady=5)
    
    book_id_label = tk.Label(main_content_frame, text="Book ID:",font=("Arial", 16), bg=bg_color)
    book_id_label.grid(row=1, column=0, padx=50, pady=5)
    
    borrower_label = tk.Label(main_content_frame, text="Borrower Name/ID:",font=("Arial", 16), bg=bg_color)
    borrower_label.grid(row=2, column=0, padx=50, pady=5)
    
    date_issued_label = tk.Label(main_content_frame, text="Date Issued (MM/DD/YYYY):",font=("Arial", 16), bg=bg_color)
    date_issued_label.grid(row=3, column=0, padx=50, pady=5)
    
    due_date_label = tk.Label(main_content_frame, text="Due Date (MM/DD/YYYY):",font=("Arial", 16), bg=bg_color)
    due_date_label.grid(row=4, column=0, padx=50, pady=5)
    
    returned_label = tk.Label(main_content_frame, text="Returned:",font=("Arial", 16), bg=bg_color)
    returned_label.grid(row=5, column=0, padx=50, pady=5)
    
    # Create entry boxes and checkboxes for input
    book_title_entry = tk.Entry(main_content_frame)
    book_title_entry.grid(row=0, column=1)
    
    book_id_entry = tk.Entry(main_content_frame)
    book_id_entry.grid(row=1, column=1)

    borrower_entry = tk.Entry(main_content_frame)
    borrower_entry.grid(row=2, column=1)

    date_issued_entry = tk.Entry(main_content_frame)
    date_issued_entry.grid(row=3, column=1)

    due_date_entry = tk.Entry(main_content_frame)
    due_date_entry.grid(row=4, column=1)

    returned_var = tk.IntVar()
    returned_checkbox = tk.Checkbutton(main_content_frame, variable=returned_var, bg=bg_color,onvalue = 1, offvalue = 0)
    returned_checkbox.grid(row=5, column=1)

    # Create submit and cancel buttons
    submit_button = tk.Button(main_content_frame, text="Submit", command=submit, bg=button_bg_color, fg=button_fg_color,width=20,height=2)
    submit_button.grid(row=6, column=0,padx=50, pady=5)

    cancel_button = tk.Button(main_content_frame, text="Cancel", command=cancel, bg=button_bg_color, fg=button_fg_color,width=20,height=2)
    cancel_button.grid(row=6, column=1,padx=50, pady=5)






# Define a function to search for the book details
def search_book():
    # Get the book ID from the entry field
    book_id = book_id_entry.get()
    
    # Perform a search for the book details based on the ID
    book_index = -1
    for i, book in enumerate(book_data):
        if book[5] == book_id:
            book_index = i
            break
            
    # If the book is not found, display an error message and return
    if book_index == -1:
        tk.messagebox.showerror("Error", "Book not found")
        return
    
    # Update the labels with the book details
    title_label.config(text="Title: " + book_data[book_index][0])
    author_label.config(text="Author: " + book_data[book_index][1])
    publisher_label.config(text="Publisher: " + book_data[book_index][2])
    publication_date_label.config(text="Publication Date: " + book_data[book_index][3])
    isbn_label.config(text="ISBN: " + book_data[book_index][4])
    bookid_label.config(text="Book ID: " + book_data[book_index][5])
    issued_to_label.config(text="Issued To (Member ID): " + book_data[book_index][6])
    date_issued_label.config(text="Date Issued: " + book_data[book_index][7])
    due_date_label.config(text="Due Date: " + book_data[book_index][8])
    
    # Enable the return button so that it can be clicked
    return_button.config(state=tk.NORMAL)



    

#Define a function to return the book
def return_book():
    # Get the book ID from the entry field
    book_id = book_id_entry.get()
    # Perform a search for the book details based on the ID
    book_index = -1
    for i, book in enumerate(book_data):
        if book[5] == book_id:
            book_index = i
            break
        
    # If the book is not found, display an error message and return
    if book_index == -1:
        tk.messagebox.showerror("Error", "Book not found")
        return

    # Update the book data to mark the book as returned
    book_data[book_index][6] = ""
    book_data[book_index][7] = ""
    book_data[book_index][8] = ""

    # Write the updated book data back to the CSV file
    write_csv("Library.csv", headers, book_data)

    # Clear the labels and disable the return button
    title_label.config(text="Title: ")
    author_label.config(text="Author: ")
    publisher_label.config(text="Publisher: ")
    publication_date_label.config(text="Publication Date: ")
    isbn_label.config(text="ISBN: ")
    bookid_label.config(text="Book ID: ")
    issued_to_label.config(text="Issued To (Member ID): ")
    date_issued_label.config(text="Date Issued: ")
    due_date_label.config(text="Due Date: ")
    return_button.config(state=tk.DISABLED)

    # Display a success message
    tk.messagebox.showinfo("Success", "Book successfully returned")

def display_return():
    global return_button, book_id_entry, headers, book_data, title_label, author_label, publisher_label, publication_date_label, isbn_label, bookid_label, issued_to_label, date_issued_label, due_date_label
    # Remove existing content from main content frame
    for child in main_content_frame.winfo_children():
        child.destroy()
    # Load the book data from the CSV file
    headers, book_data = read_csv("Library.csv")

    # Add a label for the Return Books tab
    return_books_label = tk.Label(main_content_frame, font=("Arial", 18), bg=bg_color)
    return_books_label.pack(pady=10)

    # Add an entry field for the book ID
    book_id_label = tk.Label(return_books_label, text="Enter Book ID:", bg=bg_color)
    book_id_label.pack()
    book_id_entry = tk.Entry(return_books_label)
    book_id_entry.pack(pady=5)

    # Add a button to search for the book
    search_button = tk.Button(return_books_label, text="Search", bg=button_bg_color, fg=button_fg_color, font=("Arial", 12))
    search_button.pack(pady=5)

    # Add a label for the book details section
    book_details_label = tk.Label(return_books_label, text="Book Details:", font=("Arial", 14), bg=bg_color)
    book_details_label.pack(pady=10)

    
    # Add labels for book title, author name, publisher, publication date, ISBN, book ID, issued to (member ID), date issued, and due date
    title_label = tk.Label(return_books_label, text="Title: ", font=("Arial", 12), bg=bg_color)
    title_label.pack()
    author_label = tk.Label(return_books_label, text="Author: ", font=("Arial", 12), bg=bg_color)
    author_label.pack()
    publisher_label = tk.Label(return_books_label, text="Publisher: ", font=("Arial", 12), bg=bg_color)
    publisher_label.pack()
    publication_date_label = tk.Label(return_books_label, text="Publication Date: ", font=("Arial", 12), bg=bg_color)
    publication_date_label.pack()
    isbn_label = tk.Label(return_books_label, text="ISBN: ", font=("Arial", 12), bg=bg_color)
    isbn_label.pack()
    bookid_label = tk.Label(return_books_label, text="Book ID: ", font=("Arial", 12), bg=bg_color)
    bookid_label.pack()
    issued_to_label = tk.Label(return_books_label, text="Issued To (Member ID): ", font=("Arial", 12), bg=bg_color)
    issued_to_label.pack()
    date_issued_label = tk.Label(return_books_label, text="Date Issued: ", font=("Arial", 12), bg=bg_color)
    date_issued_label.pack()
    due_date_label = tk.Label(return_books_label, text="Due Date: ", font=("Arial", 12), bg=bg_color)
    due_date_label.pack()

    # Bind the search button to search_book function
    search_button.config(command=search_book)

    # Add a button to return the book
    return_button = tk.Button(return_books_label, text="Return Book", bg=button_bg_color, fg=button_fg_color, font=("Arial", 12), state=tk.DISABLED)
    return_button.pack(pady=20)

    #Bind the return button to the return_book function
    return_button.config(command=return_book)

    
def display_students():
    # Remove existing content from main content frame
    for child in main_content_frame.winfo_children():
        child.destroy()
    
    # Create label for student name
    student_name_label = tk.Label(main_content_frame, text="Student Name:", font=("Arial", 18), bg=bg_color)
    student_name_label.grid(row=0, column=0, padx=10, pady=20)

    # Create stringvar for student name
    student_name_var = tk.StringVar()

    # Create entry widget to enter student name
    student_name_entry = tk.Entry(main_content_frame, textvariable=student_name_var, font=("Arial", 18), width=30)
    student_name_entry.grid(row=0, column=1, padx=(0,10), pady=20)

    #labels just for space
    slabel = tk.Label(main_content_frame, text="", bg=bg_color)
    slabel.grid(row=1, column=0, padx=(10,0), pady=0)
    slabe2 = tk.Label(main_content_frame, text="", bg=bg_color)
    slabe2.grid(row=2, column=0, padx=(10,0), pady=0)
    #place holeder for sortiing option dropdowns and name of columns
    slabe3 = tk.Label(main_content_frame, text="", bg=bg_color)
    slabe3.grid(row=3, column=0, padx=(10,0), pady=0)

def display_fine_management():
    # Remove existing content from main content frame
    for child in main_content_frame.winfo_children():
        child.destroy()
    # Create and add issued books label to main content frame
    issued_books_label = tk.Label(main_content_frame, text="Fine Management", font=("Arial", 24), bg=bg_color)
    issued_books_label.pack(pady=20)



# Define functions to interact with GUI
def add_book():
    title = title_var.get()
    author = author_var.get()
    publisher = publisher_var.get()
    pub_date = pub_date_var.get()
    isbn = isbn_var.get()
    bookid= bookid_var.get()
    data = [title, author, publisher, pub_date, isbn, bookid]
    headers, existing_data = read_csv('library.csv')
    existing_data.append(data)
    write_csv('library.csv', headers, existing_data)
    clear_entries()

def search_books():
    query = search_var.get()
    results = []
    for row in data:
        if query.lower() in row[0].lower() or query.lower() in row[1].lower():
            results.append(row)
    display_results(headers, results)




def update_book():

    if results_listbox.curselection():
        selected_row = int(results_listbox.curselection()[0])
        if len(data) > selected_row:  # Check if selected_row is within range of data list
            book_data = list(data[selected_row])
            edit_window = tk.Toplevel(root)
            edit_window.title("Edit Book")
            edit_window.geometry("400x300")

            style = ThemedStyle(edit_window)
            style.set_theme("breeze")

            book_label = tk.Label(edit_window, text="Book Name:",font=("Arial", 14))
            book_label.pack(pady=10)

            book_entry_var = tk.StringVar()
            book_entry_var.set(book_data[1])
            book_entry = tk.Entry(edit_window, textvariable=book_entry_var, font=("Arial", 14))
            book_entry.pack()

            author_label = tk.Label(edit_window, text="Author:",font=("Arial", 14))
            author_label.pack(pady=10)

            author_entry_var = tk.StringVar()
            author_entry_var.set(book_data[2])
            author_entry = tk.Entry(edit_window, textvariable=author_entry_var, font=("Arial", 14))
            author_entry.pack()

            isbn_label = tk.Label(edit_window, text="ISBN:",font=("Arial", 14))
            isbn_label.pack(pady=10)

            isbn_entry_var = tk.StringVar()
            isbn_entry_var.set(book_data[3])
            isbn_entry = tk.Entry(edit_window, textvariable=isbn_entry_var, font=("Arial", 14))
            isbn_entry.pack()

            def save_changes():
                book_data[1] = book_entry_var.get()
                book_data[2] = author_entry_var.get()
                book_data[3] = isbn_entry_var.get()
                data[selected_row] = tuple(book_data)
                write_csv("library.csv", headers, data)
                edit_window.destroy()
                display_books()

            save_button = tk.Button(edit_window, text="Save Changes", command=save_changes)
            save_button.pack(pady=20)
        else:
            messagebox.showerror("Error", "Selected row is out of range.")
    else:
        messagebox.showerror("Error", "Please select a book to update.")




def delete_book():
    # Get the index of the selected item in the listbox
    selection = results_listbox.curselection()

    if len(selection) > 0:
        # Remove the selected item from the CSV file
        headers, data = read_csv('library.csv')
        try:
            del data[selection[0]]
        except IndexError:
            messagebox.showerror("Error", "Selected item not found in CSV file.")

        write_csv('library.csv', headers, data)

        # Delete the selected item from the listbox
        results_listbox.delete(selection)
    else:
        # Display error message
        messagebox.showerror("Error", "Please select an item to delete.")


def display_results(headers, data):
    results_listbox.delete(0, tk.END)
    results_listbox.insert(tk.END, " | ".join(headers))
    for row in data:
        results_listbox.insert(tk.END, " | ".join(row))

def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    publisher_entry.delete(0, tk.END)
    pub_date_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)

def display_books():
    # Remove existing content from main content frame
    for child in main_content_frame.winfo_children():
        child.destroy()
    #global variables
    global headers, data, title_var, author_var, publisher_var, pub_date_var, isbn_var, bookid_var, search_var, results_listbox, title_entry, author_entry, publisher_entry, pub_date_entry, isbn_entry, search_entry



    # Read data from CSV file
    headers, data = read_csv("library.csv")
    

    
    title_var = tk.StringVar()
    author_var = tk.StringVar()
    publisher_var = tk.StringVar()
    pub_date_var = tk.StringVar()
    isbn_var = tk.StringVar()
    bookid_var=tk.StringVar()
    search_var = tk.StringVar()

    # Create frames
    add_frame = tk.Frame(main_content_frame, bg=bg_color)
    add_frame.pack(expand=True, fill="both", padx=20)

    search_frame = tk.Frame(main_content_frame, bg=bg_color)
    search_frame.pack(expand=True, fill="both", padx=20)

    results_frame = tk.Frame(main_content_frame, bg=bg_color)
    results_frame.pack(expand=True, fill="both", padx=20)

    # Add book form
    add_label = tk.Label(add_frame, text="Add Book", font=("Arial", 16), bg=bg_color)
    add_label.grid(row=0,column=1,columnspan=2,padx=340,pady=20)


    title_label = tk.Label(add_frame, text="Title:", bg=bg_color)
    title_label.grid(row=1,column=1,pady=2.5,padx=(340,0))
    title_entry = tk.Entry(add_frame, textvariable=title_var)
    title_entry.grid(row=1,column=2,padx=(0,340))

    author_label = tk.Label(add_frame, text="Author:", bg=bg_color)
    author_label.grid(row=2,column=1,pady=2.5,padx=(340,0))
    author_entry = tk.Entry(add_frame, textvariable=author_var)
    author_entry.grid(row=2,column=2,padx=(0,340))

    publisher_label = tk.Label(add_frame, text="Publisher:", bg=bg_color)
    publisher_label.grid(row=3,column=1,pady=2.5,padx=(340,0))
    publisher_entry = tk.Entry(add_frame, textvariable=publisher_var)
    publisher_entry.grid(row=3,column=2,padx=(0,340))

    pub_date_label = tk.Label(add_frame, text="Publication Date:", bg=bg_color)
    pub_date_label.grid(row=4,column=1,pady=2.5,padx=(340,0))
    pub_date_entry = tk.Entry(add_frame, textvariable=pub_date_var)
    pub_date_entry.grid(row=4,column=2,padx=(0,340))

    isbn_label = tk.Label(add_frame, text="ISBN:", bg=bg_color)
    isbn_label.grid(row=5,column=1,pady=2.5,padx=(340,0))
    isbn_entry = tk.Entry(add_frame, textvariable=isbn_var)
    isbn_entry.grid(row=5,column=2,padx=(0,340))

    bookid_label = tk.Label(add_frame, text="Book ID:", bg=bg_color)
    bookid_label.grid(row=6,column=1,pady=2.5,padx=(340,0))
    bookid_entry = tk.Entry(add_frame, textvariable=bookid_var)
    bookid_entry.grid(row=6,column=2,padx=(0,340))

    add_button = tk.Button(add_frame, text="Add Book", command=add_book, bg=button_bg_color, fg=button_fg_color)
    add_button.grid(row=7,column=1,columnspan=2,pady=20,padx=340)

    # Search books form
    
    search_label = tk.Label(search_frame, text="Search Books:", font=("Arial", 16), bg=bg_color)
    search_label.grid(row=1,column=1,padx=(315,0),pady=(20,10))

    search_entry = tk.Entry(search_frame, textvariable=search_var)
    search_entry.grid(row=1,column=2,padx=(0,315),pady=(20,10))

    search_button = tk.Button(search_frame, text="Search", command=search_books, bg=button_bg_color, fg=button_fg_color,width=20)
    search_button.grid(row=2,column=1,padx=315,columnspan=2,pady=(10,20))


    # Results listbox
    results_label = tk.Label(results_frame, text="Results", font=("Arial", 16), bg=bg_color)
    results_label.grid(row=0,column=1,padx=304)

    results_listbox = tk.Listbox(results_frame, width=100)
    results_listbox.grid(row=1,column=1,pady=10)


    update_button = tk.Button(results_frame, text="Update Book",command=update_book, bg=button_bg_color, fg=button_fg_color)
    update_button.grid(row=2,column=0,padx=(10,20))

    delete_button = tk.Button(results_frame, text="Delete Book",command=delete_book, bg=button_bg_color, fg=button_fg_color)
    delete_button.grid(row=2,column=2,padx=(20,10))


def login():
    global username_var, password_var  # Access the global variables declared at the beginning of the code
    username = username_var.get()
    password = password_var.get()
    headers, data = read_csv('login.csv')
    for row in data:
        if row[0] == username and row[1] == password:
            login_root.destroy()
            show_main_window()
            return
    error_label.config(text="Invalid username or password")
def show_login_frame():
    global login_root, username_var, password_var,error_label,login_frame  # Declare as global variables
    login_root = tk.Tk()
    login_root.title("Library Management System")
    login_root.geometry("800x600")
    login_root.config(bg=bg_color)

    style = ThemedStyle(login_root)
    style.set_theme("breeze")

    login_frame = tk.Frame(login_root, bg=bg_color)
    login_frame.pack(expand=True)

    style2 = ThemedStyle(login_frame)
    style2.set_theme("breeze")

    username_label = tk.Label(login_frame, text="Username:",font=("Arial",16), bg=bg_color)
    username_label.pack(pady=(20,5))
    username_var = tk.StringVar()
    username_entry = tk.Entry(login_frame, textvariable=username_var,width=30)
    username_entry.pack()
    password_label = tk.Label(login_frame, text="Password:", bg=bg_color,font=("Arial",16))
    password_label.pack(pady=5)
    password_var = tk.StringVar()
    password_entry = tk.Entry(login_frame, textvariable=password_var, show="*",width=30)
    password_entry.pack()

    error_label = tk.Label(login_frame, text="", fg="red", bg=bg_color,font=("Arial",10))
    error_label.pack(pady=10)
    login_button = tk.Button(login_frame, text="Login", command=login, bg=button_bg_color, fg=button_fg_color,width=30)
    login_button.pack()
    
def show_main_window():
    # Create the main window
    global root, body_frame, sidebar_frame, header_frame, main_content_frame
    root = tk.Tk()
    root.title("Library Management")
    root.geometry("1200x800")


    #set style
    style = ThemedStyle(root)
    style.set_theme("breeze")


    # Set body background color
    body_frame = tk.Frame(root, bg=bg_color)
    body_frame.pack(fill="both", expand=True)

    # Add sidebar frame(body)
    sidebar_frame = tk.Frame(body_frame, bg="#18213E", width=20, height=root.winfo_screenheight())
    sidebar_frame.pack(side="left", fill="y")

    # Add logo to header
    logo_image = tk.PhotoImage(file="library_logo.png")
    logo_label = tk.Label(sidebar_frame, image=logo_image, bg="#18213E",height=96,width=220)
    logo_label.image = logo_image
    logo_label.pack(side="top",pady=20)

    # header frame in body frame
    header_frame = tk.Frame(body_frame, bg="white",height=70)
    header_frame.pack(side="top", fill="both", expand=True)
    header_frame.pack_propagate(0)
    header_label = tk.Label(header_frame, text="Search: ", font=("Arial", 18), bg="white")
    header_label.pack(side="left")
    e20=tk.StringVar()
    entry20 = tk.Entry(header_frame, textvariable=e20, font=("Arial", 14), width=59)
    entry20.pack(padx=(10,0),side="left")




    # Add buttons to sidebar
    pages = ["Home", "Issue Books", "Return Books", "Students", "Books","Fine Management"]
    functions = [display_home, display_issue_book, display_return, display_students, display_books,display_fine_management]
    for page, func in zip(pages, functions):
        button = tk.Button(sidebar_frame, text=page, bd=0, bg="#18213E", fg="white", padx=20, pady=10, font=("Arial", 12), command=func)
        button.pack(pady=10)
        button.configure(width=20)
        button.bind("<Enter>", lambda event, btn=button: btn.config(bg="#28354A"))
        button.bind("<Leave>", lambda event, btn=button: btn.config(bg="#18213E"))

    # Add main content frame
    main_content_frame = tk.Frame(body_frame, bg=bg_color,highlightthickness=2,height=730)
    main_content_frame.pack(side="top", fill="both", expand=True)
    main_content_frame.pack_propagate(0)
    main_content_frame.grid_propagate(0)

    # Display home page by default
    display_home()

    # Start main loop
    root.mainloop()
show_login_frame()
