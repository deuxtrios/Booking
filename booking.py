import json, sys, time

def welcomeScreen():

    book_names = []
    pages = []

    while True:

        print("To name the book: B, E or A, add * before the title")

        book_name = input("Enter book name: ")

        match book_name:
            case "e":
                print("Thank you and take care")
                sys.exit(0)

            case "" | " ":
                print("Please enter a book name")
                continue

            case _:

                book_names.append(book_name.title())

                while True:

                    try:
                        page = int(input("Enter pages: "))

                        match page:
                            case "e":
                                print("Thank you and take care")
                                sys.exit(0)

                            case "" | " ":
                                print("Please enter amount of pages")

                            case _:

                                pages.append(page)

                                while True:

                                    response_2 = input("Would you like to add another book? [y or n] ")

                                    match response_2.lower():
                                        case "y":
                                            main_go_back = True
                                            go_back = True
                                            break 
                                        case "n":
                                            main_go_back = True
                                            go_back = False
                                            break
                                        case _:
                                            print("Invalid response. Try again")
                                            continue

                    except ValueError:
                        print("Invalid response. Try again")
                        continue
                
                    if main_go_back:
                        break

        if go_back:
            continue
        else:

            with open('books.json', 'r') as outside_books:
                out_library = json.load(outside_books)

            out_library.update(dict(zip(book_names, pages)))

            with open('books.json', 'w') as new_books:
                json.dump(out_library, new_books, indent=2)

            break

    editBooks()
    
def editBooks():

    while True:

        response_3 = input("You have books in your library. Do you want to edit any books? [y or n] ")

        match response_3:
            case "y":

                print("These are your books")

                with open('books.json', 'r') as new_book:
                    library = json.load(new_book)

                for books in library.keys():
                    if "Pages read on" in books:
                        continue
                    else:
                        print(books)

                while True:

                    book_response = input("Choose book you want to edit? ")

                    with open('books.json', 'r') as new_book:
                        library = json.load(new_book)

                    if book_response == "e":
                        print("Thank you and take care")
                        sys.exit(0)
                    elif book_response == "" or book_response == " ":
                        print("Please enter a response")
                        continue
                    elif book_response.title() not in library.keys():
                        print("Reponse not in library. Try again")
                        continue
                    else:
                        break
                
                while True:

                    book_response_2 = input("Do you want to rename, update the page database, remove the book, or remove all books from the database? [rename, update, remove, remove-all] ")

                    match book_response_2.lower():
                        case "" | " ":
                            print("Please enter a response [rename, update, remove, remove-all]")
                            continue

                        case "rename":
                            rename_book = input("Rename book: [enter b to back (enter *b to name the book B)] ")

                            if rename_book == "e":
                                print("Thank you and take care")
                                sys.exit(0)

                            elif rename_book == "b":
                                continue

                            else:

                                if rename_book == "*b" or rename_book == "*B":
                                    rename_book = rename_book.strip("*")

                                with open('books.json', 'r') as new_book:
                                    library = json.load(new_book)

                                library[rename_book.title()] = library.pop(book_response.title())

                                with open('books.json', 'w') as newer_book:
                                    json.dump(library, newer_book, indent=2)

                                print("Book renamed")

                                while True:

                                    book_response_3 = input("Edit database? [y or n]: ")

                                    match book_response_3:
                                        case "y":
                                            go_back = True
                                            break
                                        case "n":
                                            go_back = False
                                            break
                                        case "e":
                                            print("Thank you and take care")
                                            sys.exit(0)
                                        case _:
                                            print("Invalid response. Try again.")
                                            continue

                                if go_back:
                                    continue
                                else:
                                    break


                        case "update":

                            while True:

                                with open('books.json', 'r') as display_page:
                                    library_page_read = json.load(display_page)

                                print(f"{book_response.title()} has {library_page_read[book_response.title()]} pages\n")

                                try:

                                    update_page = input("Update the page: [enter b to back] ")

                                    if update_page == "e":
                                        print("Thank you and take care")
                                        sys.exit(0)

                                    elif update_page == "b":
                                        go_back = True
                                        break

                                    update_page = int(update_page)

                                    with open('books.json', 'r') as new_book:
                                        library = json.load(new_book)

                                    library[book_response.title()] = update_page

                                    with open('books.json', 'w') as newer_book:
                                        json.dump(library, newer_book, indent=2)

                                    print("Page updated")

                                    while True:

                                        book_response_3 = input("Edit database? [y or n]: ")

                                        match book_response_3:
                                            case "y":
                                                go_back = True
                                                break
                                            case "n":
                                                go_back = False
                                                break
                                            case "e":
                                                print("Thank you and take care")
                                                sys.exit(0)
                                            case _:
                                                print("Invalid response. Try again.")
                                                continue
                                    
                                    break

                                except ValueError:
                                        
                                    print("Invalid response. Try again")
                                    continue

                            if go_back:
                                continue
                            else:
                                break

                        case "remove":

                            with open('books.json', 'r') as new_book:
                                library = json.load(new_book)
                            
                            library.pop(book_response.title())

                            with open('books.json', 'w') as newer_book:
                                json.dump(library, newer_book, indent=2)

                            print("Book removed.")

                            with open('books.json', 'r') as future_book:
                                future_library = json.load(future_book)

                            if not future_library:
                                print("No books on the database.")

                                print("Going back to welcome screen")

                                for _ in range(3):
                                    for i in range(4):
                                        sys.stdout.write(f"\rloading{'.' * i}   ")
                                        sys.stdout.flush()
                                        time.sleep(0.4)

                                print("\n")

                                checkBooks()

                                break

                            else:

                                while True:

                                    book_response_3 = input("Edit database? [y or n]: ")

                                    match book_response_3:
                                        case "y":
                                            go_back = True
                                            break
                                        case "n":
                                            go_back = False
                                            break

                                        case "e":
                                            print("Thank you and take care")
                                            sys.exit(0)

                                        case _:
                                            print("Invalid response. Try again.")
                                            continue

                            if go_back:
                                continue
                            else:
                                break

                        case "remove-all":
                            with open('books.json', 'r') as remove_all:
                                remove_library = json.load(remove_all)

                            remove_library.clear()

                            with open('books.json', 'w') as remove_write:
                                json.dump(remove_library, remove_write)

                            print("Book database erased")

                            print("Going back to welcome screen")

                            for _ in range(3):
                                for i in range(4):
                                    sys.stdout.write(f"\rloading{'.' * i}   ")
                                    sys.stdout.flush()
                                    time.sleep(0.4)

                            print("\n")

                            checkBooks()

                            break

                        case "e":
                            print("Thank you and take care")
                            sys.exit(0)

                        case _:
                            print("Invalid response. Try again.")
                            continue


                

            case "e":
                print("Thank you and take care")
                sys.exit(0)

            case "n":

                prefix_book_read = "Pages read on"

                book_read_pages = []
                pages_read = []

                
                print("These are your books:\n")

                with open('books.json', 'r') as book_read:
                    library_2 = json.load(book_read)

                for books in library_2.keys():
                    if "Pages read on" in books:
                        continue
                    else:
                        print(books)

                while True:

                    response_4 = input("\nWhich book have you read? [enter b to go back, enter e to exit, or enter a to add books] ")

                    with open('books.json', 'r') as book_read_2:
                        library_3 = json.load(book_read_2)

                    if response_4.lower() == "b":
                        break

                    elif response_4.lower() == "e":
                        print("Thank you and take care")
                        sys.exit(0)

                    elif response_4.lower() == "a":
                        print("Going back to main menu...")

                        for _ in range(3):
                            for i in range(4):
                                sys.stdout.write(f"\rloading{'.' * i}   ")
                                sys.stdout.flush()
                                time.sleep(0.4)

                        print("\n")
                        checkBooks()
                        break
                        
                    elif response_4.title() not in library_3.keys():
                        print("Response not in library. Try again")
                        continue

                    else:

                        while True:

                            response_4 = response_4.title()

                            try:

                                response_5 = input("How many pages have you read? [enter b to back] ")

                                with open('books.json', 'r') as book_read_3:
                                    library_4 = json.load(book_read_3)

                                if response_5.lower() == "e":
                                    print("Thank you and take care")
                                    sys.exit(0)

                                elif response_5 == "" or response_5 == " ":
                                    print("Please input a response")
                                    continue

                                elif response_5.lower() == "b":
                                    break

                                elif int(response_5) > library_4[response_4]:
                                    print("Pages read is above the total amount of pages. Try again")
                                    continue

                                elif int(response_5) == library_4[response_4]:
                                    print("Book Finished. CONGRATULATIONS!")

                                    with open('books.json', 'r') as book_finished:
                                        library_finish = json.load(book_finished)

                                    library_finish.pop(response_4)

                                    if f"Pages read on {response_4}" in library_finish.keys():
                                        library_finish.pop(f"Pages read on {response_4}")

                                    with open('books.json', 'w') as file:
                                        json.dump(library_finish, file)

                                    print("Going back to main menu")

                                    for _ in range(3):
                                        for i in range(4):
                                            sys.stdout.write(f"\rloading{'.' * i}   ")
                                            sys.stdout.flush()
                                            time.sleep(0.4)

                                    print("\n")

                                    checkBooks()

                                else:
                                    with open('books.json', 'r') as remain_pages:
                                        library_pages = json.load(remain_pages)

                                    remaining_pages = library_pages[response_4] - int(response_5)

                                    print(f"You have read {response_5} pages on {response_4}. {remaining_pages} pages remaining!")

                                    book_read_pages.append(f"{prefix_book_read} {response_4}")
                                    pages_read.append(response_5)

                                    with open('books.json', 'r') as book_page_read:
                                        library_read = json.load(book_page_read)

                                    library_read.update(dict(zip(book_read_pages, pages_read)))

                                    with open('books.json', 'w') as book_appended:
                                        json.dump(library_read, book_appended, indent=2)

                                    break

                            except ValueError:

                                print("Invalid response. Try again")
                                continue 

                        continue               

            case _:
                print("Invalid response. Try again.")
                continue

def addBooks():

    print("books.json file has no books.\n")

    while True:

        response_1 = input("Do you want to add books? [y or n] ")

        match response_1.lower():
            case "y":
                welcomeScreen()
                break
            case "n" | "e":
                print("Thank you and take care")
                sys.exit(0)
            case _:
                print("Invalid response. Try again.")
                continue

def addBooksWithData():

    while True:

        response_1 = input("Do you want to add books? [y or n] ")

        match response_1.lower():
            case "y":
                welcomeScreen()
                break
            case "e":
                print("Thank you and take care")
                sys.exit(0)
            case "n":
                editBooks()
                break
            case _:
                print("Invalid response. Try again.")
                continue


def checkBooks():

    print("Welcome to Booking")
    print("You can exit anytime by entering e\n")

    with open('books.json', 'r') as main_books:
        main_library = json.load(main_books)

    if not main_library:

        addBooks()

    else:

        addBooksWithData()


checkBooks()


