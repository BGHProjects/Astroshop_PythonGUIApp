
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9193243
#    Student name: Brodie Smith 
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Online Shopping Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for simulating an online shopping experience.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import *

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *
import tkinter as tk

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#Other imports required for the assignment
import base64

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'https://www.bintel.com.au/SS_product-category/telescopes/beginner/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + 'txt', #changed from filename_extention to 'txt' to produce a text 
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#
#download()

class View(tk.Frame):
    
    def __init__(self, canvas):
        
        tk.Frame.__init__(self)

        #sets up global variables to be used for the invoice and the database
        global invoice_contents
        invoice_contents = []

        global invoice_prices
        invoice_prices = []

        global database_products
        database_products = []

        global database_prices
        database_prices = []

        #code for getting the logo onto the main screen via a file in the folder
        photo = tk.PhotoImage(file="shoplogo.gif")
        tk.Label.image = photo
        #need to keep a reference of the image, otherwise it will not display
        logo = Label(image=photo)
        logo.image = photo
        logo.grid(row=1, column=1,rowspan=3, pady=10, padx=10)


        #title label requirements
        title_label = tk.Label(canvas,
                               text = "Welcome to ASTRO SHOP - All your astrophysics needs in one shop!",
                               font =('Roboto', 20, 'bold'),
                                  bg = 'black',
                                  fg = 'yellow')
        title_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        #trending label requirements
        trending_label = tk.Label(canvas,
                                  text = "Trending Products",
                                  font =('Roboto', 15, 'italic'),
                                  bg = 'purple',
                                  fg = 'white')
        trending_label.grid(row=1, column=0, pady=10, padx=10)

        #favourites label requirements
        favourites_label = tk.Label(canvas,
                                    text = "Our Favourite Products",
                                    font =('Roboto', 15, 'italic'),
                                    bg = 'orangered',
                                    fg = 'white')
        favourites_label.grid(row=1, column=2, pady=10, padx=10)
        
        #space store button requirements
        space_store_button = tk.Button(canvas,
                                       text="Open the Space Store window",
                                       font =('Arial', 12),
                                       bg = 'blue',
                                       fg = 'yellow',
                                       command=self.space_store_window)
        space_store_button.grid(row=2, column=0, pady=10, padx=10)

        
        #ebay rss feed button requirements
        ebay_feed_button = tk.Button(canvas,
                                     text="Open the Ebay RSS Feed window",
                                     font =('Arial', 12),
                                     bg = 'blue',
                                     fg = 'yellow',
                                     command=self.ebay_feed_window)
        ebay_feed_button.grid(row=3, column=0, pady=10, padx=10)
        
        #bintel button requirements
        bintel_button = tk.Button(canvas,
                                  text="Open the BinTel window",
                                  font =('Arial', 12),
                                  bg = 'red',
                                  fg = 'yellow',
                                  command=self.bintel_window)
        bintel_button.grid(row=2, column=2, pady=10, padx=10)
        
        #mad about science button requirements
        MAS_button = tk.Button(canvas,
                               text="Open the Mad About Science window",
                               font =('Arial', 12),
                               bg = 'red',
                               fg = 'yellow',
                               command=self.MAS_window)
        MAS_button.grid(row=3, column=2, pady=10, padx=10)

        #invoice button requirements
        invoice_button = tk.Button (canvas,
                                    text = "Print Invoice",
                                    font =('Arial', 12),
                                     bg = 'yellow',
                                     fg = 'black',
                                    command=self.invoice
                                    )
        invoice_button.grid(row=4, column=1, pady=10, padx=10)
        

#
#   ALL THE CODE FOR THE SPACE STORE WINDOW
#
    def space_store_window(self):

        #code for opening the window and filling it
        space_store_window = tk.Toplevel(self)

        #code for window details
        space_store_window.title('Space Store')
        space_store_window.configure(background = 'black')
        
        #part of the function that displays the item stuff
        web_page = urlopen('https://thespacestore.com/collections/trending-now')
        html_code = web_page.read().decode("UTF-8")
        web_page.close()

        #code that takes the SS_product titles
        # and puts them in a list
        SS_product_title_list = []
        SS_product_titles = findall ('product__title">([0-9A-Za-z\s_:-]+)*', html_code)
        SS_product_title_list.append(SS_product_titles)
        
        #code that takes the image urls for the SS_products
        SS_image_url_list = []
        SS_image_urls = findall('<img.* src="([^"]+)".*>', html_code)
        SS_image_url_list.append(SS_image_urls)

        #code that collects the prices for the SS_products
        SS_product_prices_list = []
        SS_product_price = findall ('price</span>\s* \$([0-9.]*)', html_code)

        #adds them to the list
        SS_product_prices_list.append(SS_product_price)

        #code for sorting the information into the 10 SS_products

        global SS_product_1
        SS_product_1 = []
        SS_product_1.append(SS_product_title_list[0][0])
        SS_product_1.append(SS_image_url_list[0][0])
        #converts product price to a float
        SS_product_prices_list[0][0] = float(SS_product_prices_list[0][0])
        #converts to USD
        SS_product_prices_list[0][0] = 1.32 * SS_product_prices_list[0][0]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][0] = round(SS_product_prices_list[0][0], 2)
        #reverts to a string
        SS_product_prices_list[0][0] = str(SS_product_prices_list[0][0])
        #adds it to the product information
        SS_product_1.append(SS_product_prices_list[0][0])

        global SS_product_2
        SS_product_2 = []
        SS_product_2.append (SS_product_title_list[0][1])
        SS_product_2.append(SS_image_url_list[0][1])
        #converts product price to a float
        SS_product_prices_list[0][1] = float(SS_product_prices_list[0][1])
        #converts to USD
        SS_product_prices_list[0][1] = 1.32 * SS_product_prices_list[0][1]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][1] = round(SS_product_prices_list[0][1], 2)
        #reverts to a string
        SS_product_prices_list[0][1] = str(SS_product_prices_list[0][1])
        #adds it to the product information
        SS_product_2.append(SS_product_prices_list[0][1])

        global SS_product_3
        SS_product_3 = []
        SS_product_3.append (SS_product_title_list[0][2])
        SS_product_3.append(SS_image_url_list[0][2])
        #converts product price to a float
        SS_product_prices_list[0][2] = float(SS_product_prices_list[0][2])
        #converts to USD
        SS_product_prices_list[0][2] = 1.32 * SS_product_prices_list[0][2]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][2] = round(SS_product_prices_list[0][2], 2)
        #reverts to a string
        SS_product_prices_list[0][2] = str(SS_product_prices_list[0][2])
        #adds it to the product information
        SS_product_3.append(SS_product_prices_list[0][2])

        global SS_product_4
        SS_product_4 = []
        SS_product_4.append (SS_product_title_list[0][3])
        SS_product_4.append(SS_image_url_list[0][3])
        #converts product price to a float
        SS_product_prices_list[0][3] = float(SS_product_prices_list[0][3])
        #converts to USD
        SS_product_prices_list[0][3] = 1.32 * SS_product_prices_list[0][3]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][3] = round(SS_product_prices_list[0][3], 2)
        #reverts to a string
        SS_product_prices_list[0][3] = str(SS_product_prices_list[0][3])
        #adds it to the product information
        SS_product_4.append(SS_product_prices_list[0][3])

        global SS_product_5
        SS_product_5 = []
        SS_product_5.append (SS_product_title_list[0][4])
        SS_product_5.append(SS_image_url_list[0][4])
        #converts product price to a float
        SS_product_prices_list[0][4] = float(SS_product_prices_list[0][4])
        #converts to USD
        SS_product_prices_list[0][4] = 1.32 * SS_product_prices_list[0][4]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][4] = round(SS_product_prices_list[0][4], 2)
        #reverts to a string
        SS_product_prices_list[0][4] = str(SS_product_prices_list[0][4])
        #adds it to the product information
        SS_product_5.append(SS_product_prices_list[0][4])

        global SS_product_6
        SS_product_6 = []
        SS_product_6.append (SS_product_title_list[0][5])
        SS_product_6.append(SS_image_url_list[0][5])
        #converts product price to a float
        SS_product_prices_list[0][5] = float(SS_product_prices_list[0][5])
        #converts to USD
        SS_product_prices_list[0][5] = 1.32 * SS_product_prices_list[0][5]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][5] = round(SS_product_prices_list[0][5], 2)
        #reverts to a string
        SS_product_prices_list[0][5] = str(SS_product_prices_list[0][5])
        #adds it to the product information
        SS_product_6.append(SS_product_prices_list[0][5])

        global SS_product_7
        SS_product_7 = []
        SS_product_7.append (SS_product_title_list[0][6])
        SS_product_7.append(SS_image_url_list[0][6])
        #converts product price to a float
        SS_product_prices_list[0][6] = float(SS_product_prices_list[0][6])
        #converts to USD
        SS_product_prices_list[0][6] = 1.32 * SS_product_prices_list[0][6]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][6] = round(SS_product_prices_list[0][6], 2)
        #reverts to a string
        SS_product_prices_list[0][6] = str(SS_product_prices_list[0][6])
        #adds it to the product information
        SS_product_7.append(SS_product_prices_list[0][6])


        global SS_product_8
        SS_product_8 = []
        SS_product_8.append (SS_product_title_list[0][7])
        SS_product_8.append(SS_image_url_list[0][7])
        #converts product price to a float
        SS_product_prices_list[0][7] = float(SS_product_prices_list[0][7])
        #converts to USD
        SS_product_prices_list[0][7] = 1.32 * SS_product_prices_list[0][7]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][7] = round(SS_product_prices_list[0][7], 2)
        #reverts to a string
        SS_product_prices_list[0][7] = str(SS_product_prices_list[0][7])
        #adds it to the product information
        SS_product_8.append(SS_product_prices_list[0][7])

        global SS_product_9
        SS_product_9 = []
        SS_product_9.append (SS_product_title_list[0][8])
        SS_product_9.append(SS_image_url_list[0][8])
        #converts product price to a float
        SS_product_prices_list[0][8] = float(SS_product_prices_list[0][8])
        #converts to USD
        SS_product_prices_list[0][8] = 1.32 * SS_product_prices_list[0][8]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][8] = round(SS_product_prices_list[0][8], 2)
        #reverts to a string
        SS_product_prices_list[0][8] = str(SS_product_prices_list[0][8])
        #adds it to the product information
        SS_product_9.append(SS_product_prices_list[0][8])

        global SS_product_10
        SS_product_10 = []
        SS_product_10.append (SS_product_title_list[0][9])
        SS_product_10.append(SS_image_url_list[0][9])
        #converts product price to a float
        SS_product_prices_list[0][9] = float(SS_product_prices_list[0][9])
        #converts to USD
        SS_product_prices_list[0][9] = 1.32 * SS_product_prices_list[0][9]
        #rounds it to 2 decimal places
        SS_product_prices_list[0][9] = round(SS_product_prices_list[0][9], 2)
        #reverts to a string
        SS_product_prices_list[0][9] = str(SS_product_prices_list[0][9])
        #adds it to the product information
        SS_product_10.append(SS_product_prices_list[0][9])

        
        #displaying the SS_products and other information in the window

        #brief intro to the website and products
        SS_slogan = tk.Label (space_store_window,
                            text = "SPACE STORE \n Honouring the Past, Inspiring the Future",
                              font = ('Arial', 20, 'bold'),
                              bg = 'black',
                              fg = 'yellow')
        SS_slogan.grid(row=0,column=0,columnspan=2, padx=20, pady=20)

        
        #code for how the info is displayed in the window
        SS_product1 = tk.Label(space_store_window,
                            text= (SS_product_1[0] + " - $" + SS_product_1[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product1.grid(row=1, column=0, padx=5)

        SS_product1_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.SS_product1_button)
        SS_product1_button.grid(row=1, column=1, pady=5)

        #SS_product 2 code
        SS_product2 = tk.Label(space_store_window,
                            text= (SS_product_2[0] + " - $" + SS_product_2[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product2.grid(row=2,column=0, padx=5)

        SS_product2_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.SS_product2_button)
        SS_product2_button.grid(row=2, column=1, pady=5)

        #SS_product 3 code
        SS_product3 = tk.Label(space_store_window,
                            text= (SS_product_3[0] + " - $" +SS_product_3[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product3.grid(row=3, column=0, padx=5)
        SS_product3_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.SS_product3_button)
        SS_product3_button.grid(row=3, column=1, pady=5)

        #SS_product 4 code
        SS_product4 = tk.Label(space_store_window,
                            text= (SS_product_4[0] + " - $" +SS_product_4[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product4.grid(row=4, column=0, padx=5)
        SS_product4_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.SS_product4_button)
        SS_product4_button.grid(row=4, column=1, pady=5)

        #SS_product 5 code
        SS_product5 = tk.Label(space_store_window,
                            text= (SS_product_5[0] + " - $" +SS_product_5[2]),
                               font =('Airal'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product5.grid(row=5, column=0, padx=5)
        SS_product5_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.SS_product5_button)
        SS_product5_button.grid(row=5, column=1, pady=5)

        #SS_product 6 code
        SS_product6 = tk.Label(space_store_window,
                            text= (SS_product_6[0] + " - $" +SS_product_6[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product6.grid(row=6, column=0, padx=5)
        SS_product6_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.SS_product6_button)
        SS_product6_button.grid(row=6, column=1, pady=5)

        #SS_product 7 code
        SS_product7 = tk.Label(space_store_window,
                            text= (SS_product_7[0] + " - $" +SS_product_7[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product7.grid(row=7, column=0, padx=5)
        SS_product7_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.SS_product7_button)
        SS_product7_button.grid(row=7, column=1, pady=5)

        #SS_product 8 code
        SS_product8 = tk.Label(space_store_window,
                            text= (SS_product_8[0] + " - $" +SS_product_8[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product8.grid(row=8, column=0, padx=5)
        SS_product8_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.SS_product8_button)
        SS_product8_button.grid(row=8, column=1, pady=5)

        #SS_product 9 code
        SS_product9 = tk.Label(space_store_window,
                            text= (SS_product_9[0] + " - $" +SS_product_9[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product9.grid(row=9, column=0, padx=5)
        SS_product9_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.SS_product9_button)
        SS_product9_button.grid(row=9, column=1, pady=5)

        #SS_product 10 code
        SS_product10 = tk.Label(space_store_window,
                            text= (SS_product_10[0] + " - $" +SS_product_10[2]),
                                font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                            justify="left")
        SS_product10.grid(row=10, column=0, padx=5)
        SS_product10_button = tk.Button(space_store_window,
                                    text = 'Add to Cart',
                                        font = ('Arial'),
                                       bg = 'blue',
                                        fg = 'yellow',
                                     command = self.SS_product10_button)
        SS_product10_button.grid(row=10, column=1, pady=5)

        #code for the label detailing the website
        SS_info = tk.Label (space_store_window,
                            text = 'Space Store Trending Products \n https://thespacestore.com/collections/trending-now',
                            font = ('Arial', 15, 'italic'),
                            bg = 'black',
                            fg = 'yellow')
        SS_info.grid(row=11,column=0, columnspan=2, padx=20, pady=20)

    #all of these buttons convert their respective
    #lists into html syntax, and then add their
    #information to the invoice_contents list

    def SS_product1_button(self):
        SS_P1_contents = []
        SS_P1_contents.append('<tr><td>' + SS_product_1[0] + '</td>')
        SS_P1_contents.append('<td><img src=http:' + SS_product_1[1] + ' width="200" height="200"></td>')
        SS_P1_contents.append('<td>$' + SS_product_1[2] + '</td></tr>')
        invoice_contents.append(SS_P1_contents)
        invoice_prices.append(SS_product_1[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_1[0])
        database_prices.append( SS_product_1[2])

    def SS_product2_button(self):
        SS_P2_contents = []
        SS_P2_contents.append('<tr><td>' + SS_product_2[0] + '</td>')
        SS_P2_contents.append('<td><img src=http:' + SS_product_2[1] + ' width="200" height="200"></td>')
        SS_P2_contents.append('<td>$' + SS_product_2[2] + '</td></tr>')
        invoice_contents.append(SS_P2_contents)
        invoice_prices.append(SS_product_2[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_2[0])
        database_prices.append( SS_product_2[2])

    def SS_product3_button(self):
        SS_P3_contents = []
        SS_P3_contents.append('<tr><td>' + SS_product_3[0] + '</td>')
        SS_P3_contents.append('<td><img src=http:' + SS_product_3[1] + ' width="200" height="200"></td>')
        SS_P3_contents.append('<td>$' + SS_product_3[2] + '</td></tr>')
        invoice_contents.append(SS_P3_contents)
        invoice_prices.append(SS_product_3[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_3[0])
        database_prices.append( SS_product_3[2])

    def SS_product4_button(self):
        SS_P4_contents = []
        SS_P4_contents.append('<tr><td>' + SS_product_4[0] + '</td>')
        SS_P4_contents.append('<td><img src=http:' + SS_product_4[1] + ' width="200" height="200"></td>')
        SS_P4_contents.append('<td>$' + SS_product_4[2] + '</td></tr>')
        invoice_contents.append(SS_P4_contents)
        invoice_prices.append(SS_product_4[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_4[0])
        database_prices.append( SS_product_4[2])

    def SS_product5_button(self):
        SS_P5_contents = []
        SS_P5_contents.append('<tr><td>' + SS_product_5[0] + '</td>')
        SS_P5_contents.append('<td><img src=http:' + SS_product_5[1] + ' width="200" height="200"></td>')
        SS_P5_contents.append('<td>$' + SS_product_5[2] + '</td></tr>')
        invoice_contents.append(SS_P5_contents)
        invoice_prices.append(SS_product_5[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_5[0])
        database_prices.append( SS_product_5[2])

    def SS_product6_button(self):
        SS_P6_contents = []
        SS_P6_contents.append('<tr><td>' + SS_product_6[0] + '</td>')
        SS_P6_contents.append('<td><img src=http:' + SS_product_6[1] + ' width="200" height="200"></td>')
        SS_P6_contents.append('<td>$' + SS_product_6[2] + '</td></tr>')
        invoice_contents.append(SS_P6_contents)
        invoice_prices.append(SS_product_6[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_6[0])
        database_prices.append( SS_product_6[2])

    def SS_product7_button(self):
        SS_P7_contents = []
        SS_P7_contents.append('<tr><td>' + SS_product_7[0] + '</td>')
        SS_P7_contents.append('<td><img src=http:' + SS_product_7[1] + ' width="200" height="200"></td>')
        SS_P7_contents.append('<td>$' + SS_product_7[2] + '</td></tr>')
        invoice_contents.append(SS_P7_contents)
        invoice_prices.append(SS_product_7[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_7[0])
        database_prices.append( SS_product_7[2])

    def SS_product8_button(self):
        SS_P8_contents = []
        SS_P8_contents.append('<tr><td>' + SS_product_8[0] + '</td>')
        SS_P8_contents.append('<td><img src=http:' + SS_product_8[1] + ' width="200" height="200"></td>')
        SS_P8_contents.append('<td>$' + SS_product_8[2] + '</td></tr>')
        invoice_contents.append(SS_P8_contents)
        invoice_prices.append(SS_product_8[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_8[0])
        database_prices.append( SS_product_8[2])

    def SS_product9_button(self):
        SS_P9_contents = []
        SS_P9_contents.append('<tr><td>' + SS_product_9[0] + '</td>')
        SS_P9_contents.append('<td><img src=http:' + SS_product_9[1] + ' width="200" height="200"></td>')
        SS_P9_contents.append('<td>$' + SS_product_9[2] + '</td></tr>')
        invoice_contents.append(SS_P9_contents)
        invoice_prices.append(SS_product_9[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_9[0])
        database_prices.append( SS_product_9[2])

    def SS_product10_button(self):
        SS_P10_contents = []
        SS_P10_contents.append('<tr><td>' + SS_product_10[0] + '</td>')
        SS_P10_contents.append('<td><img src=http:' + SS_product_10[1] + ' width="200" height="200"></td>')
        SS_P10_contents.append('<td>$' + SS_product_10[2] + '</td></tr>')
        invoice_contents.append(SS_P10_contents)
        invoice_prices.append(SS_product_10[2])
        #adds details to the database list to add to the SQL database
        database_products.append(SS_product_10[0])
        database_prices.append( SS_product_10[2])

#
# ALL THE CODE FOR THE EBAY RSS FEED
#

    def ebay_feed_window(self):
        #code for opening the window and filling it
        ebay_feed_window = tk.Toplevel(self)

        #code for titling the window
        ebay_feed_window.title('Ebay RSS Feed (Solar System Posters)')
        ebay_feed_window.configure(background = 'black')
        
        #part of the function that hopefully displays the item stuff
        web_page = urlopen('https://www.ebay.com.au/sch/i.html?&_nkw=solar+system+posters&_rss=1')
        html_code = web_page.read().decode("UTF-8")
        web_page.close()

        #code that takes the ER_product titles
        # and puts them in a list
        ER_product_title_list = []
        ER_product_titles = findall ('<item>\n<title><!\[CDATA\[(.*)\]]', html_code)
        ER_product_title_list.append(ER_product_titles)

        #code that takes the image urls for the ER_products
        ER_image_url_list = []
        ER_image_urls = findall('<img.* src="([^"]+\.*)"></a>', html_code)
        ER_image_url_list.append(ER_image_urls)

        #code that collects the prices for the ER_products
        ER_product_prices_list = []
        ER_product_price = findall ('AU\s\$</b>([0-9.]*)</s', html_code)
        ER_product_prices_list.append(ER_product_price)

        #code for sorting the information in the 10 ER_products
        
        global ER_product_1
        ER_product_1 = []
        ER_product_1.append (ER_product_title_list[0][0])
        ER_product_1.append(ER_image_url_list[0][0])
        ER_product_1.append(ER_product_prices_list[0][0])

        global ER_product_2
        ER_product_2 = []
        ER_product_2.append (ER_product_title_list[0][1])
        ER_product_2.append(ER_image_url_list[0][1])
        ER_product_2.append(ER_product_prices_list[0][1])

        global ER_product_3
        ER_product_3 = []
        ER_product_3.append (ER_product_title_list[0][2])
        ER_product_3.append(ER_image_url_list[0][2])
        ER_product_3.append(ER_product_prices_list[0][2])

        global ER_product_4
        ER_product_4 = []
        ER_product_4.append (ER_product_title_list[0][3])
        ER_product_4.append(ER_image_url_list[0][3])
        ER_product_4.append(ER_product_prices_list[0][3])

        global ER_product_5
        ER_product_5 = []
        ER_product_5.append (ER_product_title_list[0][4])
        ER_product_5.append(ER_image_url_list[0][4])
        ER_product_5.append(ER_product_prices_list[0][4])

        global ER_product_6
        ER_product_6 = []
        ER_product_6.append (ER_product_title_list[0][5])
        ER_product_6.append(ER_image_url_list[0][5])
        ER_product_6.append(ER_product_prices_list[0][5])

        global ER_product_7
        ER_product_7 = []
        ER_product_7.append (ER_product_title_list[0][6])
        ER_product_7.append(ER_image_url_list[0][6])
        ER_product_7.append(ER_product_prices_list[0][6])

        global ER_product_8
        ER_product_8 = []
        ER_product_8.append (ER_product_title_list[0][7])
        ER_product_8.append(ER_image_url_list[0][7])
        ER_product_8.append(ER_product_prices_list[0][7])

        global ER_product_9
        ER_product_9 = []
        ER_product_9.append (ER_product_title_list[0][8])
        ER_product_9.append(ER_image_url_list[0][8])
        ER_product_9.append(ER_product_prices_list[0][8])

        global ER_product_10
        ER_product_10 = []
        ER_product_10.append (ER_product_title_list[0][9])
        ER_product_10.append(ER_image_url_list[0][9])
        ER_product_10.append(ER_product_prices_list[0][9])


        #displaying the ER_products and other information in the window
        
        #brief intro to the website and products
        ER_intro = tk.Label (ebay_feed_window,
                            text = "EBAY RSS FEED \n Browse the newest listings for Solar System Posters on Ebay",
                             font = ('Arial', 20, 'bold'),
                             bg = 'black',
                             fg = 'yellow')
        ER_intro.grid(row=0,column=0, columnspan=2, padx=20, pady=20)
        
        #ER_product 1 code
        ER_product1 = tk.Label(ebay_feed_window,
                            text= (ER_product_1[0] + " - $" + ER_product_1[2]),
                            font =('Arial'),
                            bg = 'black',
                            fg = 'blue',
                            justify="left")
        ER_product1.grid(row=1, column=0, padx=5)

        ER_product1_button = tk.Button(ebay_feed_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                       bg = 'blue',
                                       fg = 'yellow',
                                     command = self.ER_product1_button)
        ER_product1_button.grid(row=1, column=1, pady=5)

        #ER_product 2 code
        ER_product2 = tk.Label(ebay_feed_window,
                                text= (ER_product_2[0] + " - $" + ER_product_2[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                                justify="left")
        ER_product2.grid(row=2, column=0)

        ER_product2_button = tk.Button(ebay_feed_window,
                                    text = 'Add to Cart',
                                    font = ('Arial'),
                                     bg = 'blue',
                                    fg = 'yellow',
                                     command = self.ER_product2_button)
        ER_product2_button.grid(row=2, column=1, pady=5)

        #ER_product 3 code
        ER_product3 = tk.Label(ebay_feed_window,
                              text= (ER_product_3[0] + " - $" + ER_product_3[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                              justify="left")
        ER_product3.grid(row=3, column=0)

        ER_product3_button = tk.Button(ebay_feed_window,
                                       text = 'Add to Cart',
                                       font = ('Arial'),
                                        bg = 'blue',
                                        fg = 'yellow',
                                       command = self.ER_product3_button)
        ER_product3_button.grid(row=3, column=1, pady=5)

        #ER_product 4 code
        ER_product4 = tk.Label(ebay_feed_window,
                              text= (ER_product_4[0] + " - $" + ER_product_4[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                              justify="left")
        ER_product4.grid(row=4, column=0)

        ER_product4_button = tk.Button(ebay_feed_window,
                                       text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'blue',
                                    fg = 'yellow',
                                       command = self.ER_product4_button)
        ER_product4_button.grid(row=4, column=1, pady=5)

        #ER_product 5 code
        ER_product5 = tk.Label(ebay_feed_window,
                          text= (ER_product_5[0] + " - $" + ER_product_5[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                          justify="left")
        ER_product5.grid(row=5, column=0)

        ER_product5_button = tk.Button(ebay_feed_window,
                               text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'blue',
                                    fg = 'yellow',
                               command = self.ER_product5_button)
        ER_product5_button.grid(row=5, column=1, pady=5)

        #ER_product 6 code
        ER_product6 = tk.Label(ebay_feed_window,
                      text= (ER_product_6[0] + " - $" + ER_product_6[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                      justify="left")
        ER_product6.grid(row=6, column=0)

        ER_product6_button = tk.Button(ebay_feed_window,
                               text = 'Add to Cart',
                                font = ('Arial'),
                                bg = 'blue',
                                fg = 'yellow',
                               command = self.ER_product6_button)
        ER_product6_button.grid(row=6, column=1, pady=5)

        #ER_product 7 code
        ER_product7 = tk.Label(ebay_feed_window,
                      text= (ER_product_7[0] + " - $" + ER_product_7[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                      justify="left")
        ER_product7.grid(row=7, column=0)

        ER_product7_button = tk.Button(ebay_feed_window,
                               text = 'Add to Cart',
                                font = ('Arial'),
                                bg = 'blue',
                                fg = 'yellow',
                               command = self.ER_product7_button)
        ER_product7_button.grid(row=7, column=1, pady=5)

        #ER_product 8 code
        ER_product8 = tk.Label(ebay_feed_window,
                      text= (ER_product_8[0] + " - $" + ER_product_8[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                      justify="left")
        ER_product8.grid(row=8, column=0)

        ER_product8_button = tk.Button(ebay_feed_window,
                               text = 'Add to Cart',
                                font = ('Arial'),
                                bg = 'blue',
                                fg = 'yellow',
                               command = self.ER_product8_button)
        ER_product8_button.grid(row=8, column=1, pady=5)

        #ER_product 9 code
        ER_product9 = tk.Label(ebay_feed_window,
                      text= (ER_product_9[0] + " - $" + ER_product_9[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                      justify="left")
        ER_product9.grid(row=9, column=0)

        ER_product9_button = tk.Button(ebay_feed_window,
                               text = 'Add to Cart',
                                font = ('Arial'),
                                bg = 'blue',
                                fg = 'yellow',
                               command = self.ER_product9_button)
        ER_product9_button.grid(row=9, column=1, pady=5)

        #ER_product 10 code
        ER_product10 = tk.Label(ebay_feed_window,
                      text= (ER_product_10[0] + " - $" + ER_product_10[2]),
                                font =('Arial'),
                               bg = 'black',
                               fg = 'blue',
                      justify="left")
        ER_product10.grid(row=10, column=0)

        ER_product10_button = tk.Button(ebay_feed_window,
                               text = 'Add to Cart',
                                font = ('Arial'),
                                bg = 'blue',
                                fg = 'yellow',
                               command = self.ER_product10_button)
        ER_product10_button.grid(row=10, column=1, pady=5)

        #code for the label detailing the website
        ER_info = tk.Label (ebay_feed_window,
                            text = 'Solar System Posters (Ebay RSS Feed) \n https://www.ebay.com.au/sch/i.html?&_nkw=solar+system+posters&_rss=1',
                            font = ('Arial', 15, 'italic'),
                            bg = 'black',
                            fg = 'yellow')
        ER_info.grid(row=11,column=0,columnspan=2, pady=20)

        #all of these buttons convert their respective
        #lists into html syntax, and then add their
        #information to the invoice_contents list

    def ER_product1_button(self):
        ER_P1_contents = []
        ER_P1_contents.append('<tr><td>' + ER_product_1[0] + '</td>')
        ER_P1_contents.append('<td><img src=' + ER_product_1[1] + ' width="200" height="200"></td>')
        ER_P1_contents.append('<td>$' + ER_product_1[2] + '</td></tr>')
        invoice_contents.append(ER_P1_contents)
        invoice_prices.append(ER_product_1[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_1[0])
        database_prices.append( ER_product_1[2])

    def ER_product2_button(self):
        ER_P2_contents = []
        ER_P2_contents.append('<tr><td>' + ER_product_2[0] + '</td>')
        ER_P2_contents.append('<td><img src=' + ER_product_2[1] + ' width="200" height="200"></td>')
        ER_P2_contents.append('<td>$' + ER_product_2[2] + '</td></tr>')
        invoice_contents.append(ER_P2_contents)
        invoice_prices.append(ER_product_2[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_2[0])
        database_prices.append( ER_product_2[2])

    def ER_product3_button(self):
        ER_P3_contents = []
        ER_P3_contents.append('<tr><td>' + ER_product_3[0] + '</td>')
        ER_P3_contents.append('<td><img src=' + ER_product_3[1] + ' width="200" height="200"></td>')
        ER_P3_contents.append('<td>$' + ER_product_3[2] + '</td></tr>')
        invoice_contents.append(ER_P3_contents)
        invoice_prices.append(ER_product_3[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_3[0])
        database_prices.append( ER_product_3[2])

    def ER_product4_button(self):
        ER_P4_contents = []
        ER_P4_contents.append('<tr><td>' + ER_product_4[0] + '</td>')
        ER_P4_contents.append('<td><img src=' + ER_product_4[1] + ' width="200" height="200"></td>')
        ER_P4_contents.append('<td>$' + ER_product_4[2] + '</td></tr>')
        invoice_contents.append(ER_P4_contents)
        invoice_prices.append(ER_product_4[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_4[0])
        database_prices.append( ER_product_4[2])

    def ER_product5_button(self):
        ER_P5_contents = []
        ER_P5_contents.append('<tr><td>' + ER_product_5[0] + '</td>')
        ER_P5_contents.append('<td><img src=' + ER_product_5[1] + ' width="200" height="200"></td>')
        ER_P5_contents.append('<td>$' + ER_product_5[2] + '</td></tr>')
        invoice_contents.append(ER_P5_contents)
        invoice_prices.append(ER_product_5[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_5[0])
        database_prices.append( ER_product_5[2])
        
    def ER_product6_button(self):
        ER_P6_contents = []
        ER_P6_contents.append('<tr><td>' + ER_product_6[0] + '</td>')
        ER_P6_contents.append('<td><img src=' + ER_product_6[1] + ' width="200" height="200"></td>')
        ER_P6_contents.append('<td>$' + ER_product_6[2] + '</td></tr>')
        invoice_contents.append(ER_P6_contents)
        invoice_prices.append(ER_product_6[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_6[0])
        database_prices.append( ER_product_6[2])

    def ER_product7_button(self):
        ER_P7_contents = []
        ER_P7_contents.append('<tr><td>' + ER_product_7[0] + '</td>')
        ER_P7_contents.append('<td><img src=' + ER_product_7[1] + ' width="200" height="200"></td>')
        ER_P7_contents.append('<td>$' + ER_product_7[2] + '</td></tr>')
        invoice_contents.append(ER_P7_contents)
        invoice_prices.append(ER_product_7[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_7[0])
        database_prices.append( ER_product_7[2])

    def ER_product8_button(self):
        ER_P8_contents = []
        ER_P8_contents.append('<tr><td>' + ER_product_8[0] + '</td>')
        ER_P8_contents.append('<td><img src=' + ER_product_8[1] + ' width="200" height="200"></td>')
        ER_P8_contents.append('<td>$' + ER_product_8[2] + '</td></tr>')
        invoice_contents.append(ER_P8_contents)
        invoice_prices.append(ER_product_8[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_8[0])
        database_prices.append( ER_product_8[2])
    
    def ER_product9_button(self):
        ER_P9_contents = []
        ER_P9_contents.append('<tr><td>' + ER_product_9[0] + '</td>')
        ER_P9_contents.append('<td><img src=' + ER_product_9[1] + ' width="200" height="200"></td>')
        ER_P9_contents.append('<td>$' + ER_product_9[2] + '</td></tr>')
        invoice_contents.append(ER_P9_contents)
        invoice_prices.append(ER_product_9[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_9[0])
        database_prices.append( ER_product_9[2])

    def ER_product10_button(self):
        ER_P10_contents = []
        ER_P10_contents.append('<tr><td>' + ER_product_10[0] + '</td>')
        ER_P10_contents.append('<td><img src=' + ER_product_10[1] + ' width="200" height="200"></td>')
        ER_P10_contents.append('<td>$' + ER_product_10[2] + '</td></tr>')
        invoice_contents.append(ER_P10_contents)
        invoice_prices.append(ER_product_10[2])
        #adds details to the database list to add to the SQL database
        database_products.append(ER_product_10[0])
        database_prices.append( ER_product_10[2])
        
#
# ALL THE CODE FOR THE BINTEL WINDOW
#

    def bintel_window(self):
        #code for opening the window and filling it
        bintel_window = tk.Toplevel(self)

        #code that titles the window
        bintel_window.title('Bintel (Binoculars and Telescopes)')
        bintel_window.configure(background = 'black')

        #part of the code that accesses
        #the text file of the html code
        bintel = open('BinTel Beginners Telescopes Page HTMLcode.txt', 'U').read()

        #code that take the names of the products
        #and puts them in a list
        BT_title_list = []
        BT_titles = findall ( '"name">([a-zA-Z0-9' '].*)</p>', bintel)
        BT_title_list.append(BT_titles)

        #code that takes the image URLs from Bintel
        BT_image_list = []
        BT_images = findall ('front-image"><img.* src="([^"]+)', bintel)
        BT_image_list.append(BT_images)

        #code that collects the prices from Bintel
        BT_prices_list = []
        BT_price = findall( '"price".*&#36.*</span>([0-9.,]+)', bintel)
        BT_prices_list.append(BT_price)

        #code for sorting the information in the 10 BT_products

        global BT_product_1
        BT_product_1 = []
        BT_product_1.append(BT_title_list[0][0])
        BT_product_1.append(BT_image_list[0][0])
        BT_product_1.append(BT_prices_list[0][0])

        global BT_product_2
        BT_product_2 = []
        BT_product_2.append(BT_title_list[0][1])
        BT_product_2.append(BT_image_list[0][1])
        BT_product_2.append(BT_prices_list[0][1])

        global BT_product_3
        BT_product_3 = []
        BT_product_3.append(BT_title_list[0][2])
        BT_product_3.append(BT_image_list[0][2])
        BT_product_3.append(BT_prices_list[0][2])

        global BT_product_4
        BT_product_4 = []
        BT_product_4.append(BT_title_list[0][3])
        BT_product_4.append(BT_image_list[0][3])
        BT_product_4.append(BT_prices_list[0][3])
    
        global BT_product_5
        BT_product_5 = []
        BT_product_5.append(BT_title_list[0][4])
        BT_product_5.append(BT_image_list[0][4])
        BT_product_5.append(BT_prices_list[0][4])
        
        global BT_product_6
        BT_product_6 = []
        BT_product_6.append(BT_title_list[0][5])
        BT_product_6.append(BT_image_list[0][5])
        BT_product_6.append(BT_prices_list[0][5])
        
        global BT_product_7
        BT_product_7 = []
        BT_product_7.append(BT_title_list[0][6])
        BT_product_7.append(BT_image_list[0][6])
        BT_product_7.append(BT_prices_list[0][6])

        global BT_product_8
        BT_product_8 = []
        BT_product_8.append(BT_title_list[0][7])
        BT_product_8.append(BT_image_list[0][7])
        BT_product_8.append(BT_prices_list[0][7])

        global BT_product_9
        BT_product_9 = []
        BT_product_9.append(BT_title_list[0][8])
        BT_product_9.append(BT_image_list[0][8])
        BT_product_9.append(BT_prices_list[0][8])

        global BT_product_10
        BT_product_10 = []
        BT_product_10.append(BT_title_list[0][9])
        BT_product_10.append(BT_image_list[0][9])
        BT_product_10.append(BT_prices_list[0][9])

        #displaying the BT_products and other information in the window

        #brief intro to the website and products
        BT_slogan = tk.Label (bintel_window,
                            text = ("BINTEL \n Browse Australia's largest range of telescopes and binoculars"),
                              font = ('Arial', 20, 'bold'),
                              bg = 'black',
                              fg = 'yellow')
        BT_slogan.grid(row=0,column=0, columnspan=2, padx=20, pady=20)

        #code for BT_product1
        BT_product1 = tk.Label(bintel_window,
                            text= (BT_product_1[0] + " - $" + BT_product_1[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product1.grid(row=1, column=0, padx=5)

        BT_product1_button = tk.Button(bintel_window,
                                       text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.BT_product1_button)
        BT_product1_button.grid(row=1, column=1, pady=5)

        #code for BT_product2
        BT_product2 = tk.Label(bintel_window,
                            text= (BT_product_2[0] + " - $" + BT_product_2[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product2.grid(row=2, column=0)

        BT_product2_button = tk.Button(bintel_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.BT_product2_button)
        BT_product2_button.grid(row=2, column=1, pady=5)

        #code for BT_product3
        BT_product3 = tk.Label(bintel_window,
                            text= (BT_product_3[0] + " - $" + BT_product_3[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product3.grid(row=3, column=0, padx=5)

        BT_product3_button = tk.Button(bintel_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                     command = self.BT_product3_button)
        BT_product3_button.grid(row=3, column=1, pady=5)

        #code for BT_product4
        BT_product4 = tk.Label(bintel_window,
                            text= (BT_product_4[0] + " - $" + BT_product_4[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product4.grid(row=4, column=0, padx=5)

        BT_product4_button = tk.Button(bintel_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                     command = self.BT_product4_button)
        BT_product4_button.grid(row=4, column=1, pady=5)

        #code for BT_product5
        BT_product5 = tk.Label(bintel_window,
                            text= (BT_product_5[0] + " - $" + BT_product_5[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product5.grid(row=5, column=0, padx =5)

        BT_product5_button = tk.Button(bintel_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                     command = self.BT_product5_button)
        BT_product5_button.grid(row=5, column=1, pady=5)

        #code for BT_product6
        BT_product6 = tk.Label(bintel_window,
                            text= (BT_product_6[0] + " - $" + BT_product_6[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product6.grid(row=6, column=0, padx=5)

        BT_product6_button = tk.Button(bintel_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                     command = self.BT_product6_button)
        BT_product6_button.grid(row=6, column=1, pady=5)

        #code for BT_product7
        BT_product7 = tk.Label(bintel_window,
                            text= (BT_product_7[0] + " - $" + BT_product_7[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product7.grid(row=7, column=0, padx=5)

        BT_product7_button = tk.Button(bintel_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                     command = self.BT_product7_button)
        BT_product7_button.grid(row=7, column=1, pady=5)

        #code for BT_product8
        BT_product8 = tk.Label(bintel_window,
                            text= (BT_product_8[0] + " - $" + BT_product_8[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product8.grid(row=8, column=0, padx=5)

        BT_product8_button = tk.Button(bintel_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                     command = self.BT_product8_button)
        BT_product8_button.grid(row=8, column=1, pady=5)

        #code for BT_product9
        BT_product9 = tk.Label(bintel_window,
                            text= (BT_product_9[0] + " - $" + BT_product_9[2]),
                               font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product9.grid(row=9, column=0, padx=5)

        BT_product9_button = tk.Button(bintel_window,
                                    text = 'Add to Cart',
                                       font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                     command = self.BT_product9_button)
        BT_product9_button.grid(row=9, column=1, pady=5)

        #code for BT_product10
        BT_product10 = tk.Label(bintel_window,
                            text= (BT_product_10[0] + " - $" + BT_product_10[2]),
                                font =('Arial'),
                               bg = 'black',
                               fg = 'red',
                            justify="left")
        BT_product10.grid(row=10, column=0, padx=5)

        BT_product10_button = tk.Button(bintel_window,
                                    text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                     command = self.BT_product10_button)
        BT_product10_button.grid(row=10, column=1, pady=5)

        #code for the label detailing the website
        BT_info = tk.Label (bintel_window,
                            text = "Bintel (Australia's Largest Binocular and Telescope Store) \n https://www.bintel.com.au/product-category/telescopes/beginner/",
                            font = ('Arial', 15, 'italic'),
                            bg = 'black',
                            fg = 'yellow')
        BT_info.grid(row=11,column=0, columnspan=2, pady=20, padx=20)

        #all of these buttons convert their respective
        #lists into html syntax, and then add their
        #information to the invoice_contents list

    def BT_product1_button(self):
        BT_P1_contents = []
        BT_P1_contents.append('<tr><td>' + BT_product_1[0] + '</td>')
        BT_P1_contents.append('<td><img src=' + BT_product_1[1] + ' width="200" height="200"></td>')
        BT_P1_contents.append('<td>$' + BT_product_1[2] + '</td></tr>')
        invoice_contents.append(BT_P1_contents)
        invoice_prices.append(BT_product_1[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_1[0])
        database_prices.append( BT_product_1[2])

    def BT_product2_button(self):
        BT_P2_contents = []
        BT_P2_contents.append('<tr><td>' + BT_product_2[0] + '</td>')
        BT_P2_contents.append('<td><img src=' + BT_product_2[1] + ' width="200" height="200"></td>')
        BT_P2_contents.append('<td>$' + BT_product_2[2] + '</td></tr>')
        invoice_contents.append(BT_P2_contents)
        invoice_prices.append(BT_product_2[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_2[0])
        database_prices.append( BT_product_2[2])

    def BT_product3_button(self):
        BT_P3_contents = []
        BT_P3_contents.append('<tr><td>' + BT_product_3[0] + '</td>')
        BT_P3_contents.append('<td><img src=' + BT_product_3[1] + ' width="200" height="200"></td>')
        BT_P3_contents.append('<td>$' + BT_product_3[2] + '</td></tr>')
        invoice_contents.append(BT_P3_contents)
        invoice_prices.append(BT_product_3[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_3[0])
        database_prices.append( BT_product_3[2])

    def BT_product4_button(self):
        BT_P4_contents = []
        BT_P4_contents.append('<tr><td>' + BT_product_4[0] + '</td>')
        BT_P4_contents.append('<td><img src=' + BT_product_4[1] + ' width="200" height="200"></td>')
        BT_P4_contents.append('<td>$' + BT_product_4[2] + '</td></tr>')
        invoice_contents.append(BT_P4_contents)
        invoice_prices.append(BT_product_4[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_4[0])
        database_prices.append( BT_product_4[2])

    def BT_product5_button(self):
        BT_P5_contents = []
        BT_P5_contents.append('<tr><td>' + BT_product_5[0] + '</td>')
        BT_P5_contents.append('<td><img src=' + BT_product_5[1] + ' width="200" height="200"></td>')
        BT_P5_contents.append('<td>$' + BT_product_5[2] + '</td></tr>')
        invoice_contents.append(BT_P5_contents)
        invoice_prices.append(BT_product_5[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_5[0])
        database_prices.append( BT_product_5[2])

    def BT_product6_button(self):
        BT_P6_contents = []
        BT_P6_contents.append('<tr><td>' + BT_product_6[0] + '</td>')
        BT_P6_contents.append('<td><img src=' + BT_product_6[1] + ' width="200" height="200"></td>')
        BT_P6_contents.append('<td>$' + BT_product_6[2] + '</td></tr>')
        invoice_contents.append(BT_P6_contents)
        invoice_prices.append(BT_product_6[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_6[0])
        database_prices.append( BT_product_6[2])

    def BT_product7_button(self):
        BT_P7_contents = []
        BT_P7_contents.append('<tr><td>' + BT_product_7[0] + '</td>')
        BT_P7_contents.append('<td><img src=' + BT_product_7[1] + ' width="200" height="200"></td>')
        BT_P7_contents.append('<td>$' + BT_product_7[2] + '</td></tr>')
        invoice_contents.append(BT_P7_contents)
        invoice_prices.append(BT_product_7[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_7[0])
        database_prices.append( BT_product_7[2])

    def BT_product8_button(self):
        BT_P8_contents = []
        BT_P8_contents.append('<tr><td>' + BT_product_8[0] + '</td>')
        BT_P8_contents.append('<td><img src=' + BT_product_8[1] + ' width="200" height="200"></td>')
        BT_P8_contents.append('<td>$' + BT_product_8[2] + '</td></tr>')
        invoice_contents.append(BT_P8_contents)
        invoice_prices.append(BT_product_8[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_8[0])
        database_prices.append( BT_product_8[2])

    def BT_product9_button(self):
        BT_P9_contents = []
        BT_P9_contents.append('<tr><td>' + BT_product_9[0] + '</td>')
        BT_P9_contents.append('<td><img src=' + BT_product_9[1] + ' width="200" height="200"></td>')
        BT_P9_contents.append('<td>$' + BT_product_9[2] + '</td></tr>')
        invoice_contents.append(BT_P9_contents)
        invoice_prices.append(BT_product_9[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_9[0])
        database_prices.append( BT_product_9[2])

    def BT_product10_button(self):
        BT_P10_contents = []
        BT_P10_contents.append('<tr><td>' + BT_product_10[0] + '</td>')
        BT_P10_contents.append('<td><img src=' + BT_product_10[1] + ' width="200" height="200"></td>')
        BT_P10_contents.append('<td>$' + BT_product_10[2] + '</td></tr>')
        invoice_contents.append(BT_P10_contents)
        invoice_prices.append(BT_product_10[2])
        #adds details to the database list to add to the SQL database
        database_products.append(BT_product_10[0])
        database_prices.append( BT_product_10[2])

                        
#
# ALL THE CODE FOR THE MAS WINDOW
#

    def MAS_window(self):
        #code for opening the window and filling it
        MAS_window = tk.Toplevel(self)

        #code that titles the window
        MAS_window.title('Mad About Science (Space Category)')
        MAS_window.configure(background = 'black')

        #part of the code that accesses
        #the text file of the html code
        mashtml = open('Mad About Science HTML code.txt', 'U').read()
        
        #code that take the names of the products
        #and puts them in a list
        MAS_title_list = []
        MAS_titles = findall ( '"product-item-link"\s.*title="([a-zA-Z0-9 -]*)', mashtml)
        MAS_title_list.append(MAS_titles)

        #code that takes the image URLs from the MAS HTML code
        MAS_image_list = []
        MAS_images = findall ('"product-image-photo"\s.*src="([^"]+)"', mashtml)
        MAS_image_list.append(MAS_images)
        
        #code that collects the prices from the MAS HTML code
        MAS_prices_list = []
        MAS_price = findall( 'data-price-amount="([0-9.]*)"', mashtml)
        MAS_prices_list.append(MAS_price)

        #code for sorting the information into the ten MAS products

        global MAS_product_1
        MAS_product_1 = []
        MAS_product_1.append(MAS_title_list[0][0])
        MAS_product_1.append(MAS_image_list[0][0])
        MAS_product_1.append(MAS_prices_list[0][0])

        global MAS_product_2
        MAS_product_2 = []
        MAS_product_2.append(MAS_title_list[0][1])
        MAS_product_2.append(MAS_image_list[0][1])
        MAS_product_2.append(MAS_prices_list[0][1])

        global MAS_product_3
        MAS_product_3 = []
        MAS_product_3.append(MAS_title_list[0][2])
        MAS_product_3.append(MAS_image_list[0][2])
        MAS_product_3.append(MAS_prices_list[0][2])

        global MAS_product_4
        MAS_product_4 = []
        MAS_product_4.append(MAS_title_list[0][3])
        MAS_product_4.append(MAS_image_list[0][3])
        MAS_product_4.append(MAS_prices_list[0][3])

        global MAS_product_5
        MAS_product_5 = []
        MAS_product_5.append(MAS_title_list[0][4])
        MAS_product_5.append(MAS_image_list[0][4])
        MAS_product_5.append(MAS_prices_list[0][4])

        global MAS_product_6
        MAS_product_6 = []
        MAS_product_6.append(MAS_title_list[0][5])
        MAS_product_6.append(MAS_image_list[0][5])
        MAS_product_6.append(MAS_prices_list[0][5])

        global MAS_product_7
        MAS_product_7 = []
        MAS_product_7.append(MAS_title_list[0][6])
        MAS_product_7.append(MAS_image_list[0][6])
        MAS_product_7.append(MAS_prices_list[0][6])

        global MAS_product_8
        MAS_product_8 = []
        MAS_product_8.append(MAS_title_list[0][7])
        MAS_product_8.append(MAS_image_list[0][7])
        MAS_product_8.append(MAS_prices_list[0][7])

        global MAS_product_9
        MAS_product_9 = []
        MAS_product_9.append(MAS_title_list[0][8])
        MAS_product_9.append(MAS_image_list[0][8])
        MAS_product_9.append(MAS_prices_list[0][8])

        global MAS_product_10
        MAS_product_10 = []
        MAS_product_10.append(MAS_title_list[0][9])
        MAS_product_10.append(MAS_image_list[0][9])
        MAS_product_10.append(MAS_prices_list[0][9])

        #displaying the MAS products and other information in the window

        #brief intro to the website and products
        MAS_intro = tk.Label (MAS_window,
                            text = "MAD ABOUT SCIENCE \n Browse our range of space-themed science items",
                              font = ('Arial', 20, 'bold'),
                              bg = 'black',
                              fg = 'yellow')
        MAS_intro.grid(row=0,column=0, columnspan=2, padx=20, pady=20)

        #code for MAS_product1
        MAS_product1 = tk.Label(MAS_window,
                            text= (MAS_product_1[0] + " - $" + MAS_product_1[2]),
                                font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product1.grid(row=1, column=0)

        MAS_product1_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product1_button)
        MAS_product1_button.grid(row=1, column=1, pady=5)

        #code for MAS_product2
        MAS_product2 = tk.Label(MAS_window,
                            text= (MAS_product_2[0] + " - $" + MAS_product_2[2]),
                                font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product2.grid(row=2, column=0)

        MAS_product2_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product2_button)
        MAS_product2_button.grid(row=2, column=1, pady=5)

        #code for MAS_product3
        MAS_product3 = tk.Label(MAS_window,
                            text= (MAS_product_3[0] + " - $" + MAS_product_3[2]),
                                font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product3.grid(row=3, column=0)

        MAS_product3_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product3_button)
        MAS_product3_button.grid(row=3, column=1, pady=5)

        #code for MAS_product4
        MAS_product4 = tk.Label(MAS_window,
                            text= (MAS_product_4[0] + " - $" + MAS_product_4[2]),
                                font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product4.grid(row=4, column=0)

        MAS_product4_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product4_button)
        MAS_product4_button.grid(row=4, column=1, pady=5)

        #code for MAS_product5
        MAS_product5 = tk.Label(MAS_window,
                            text= (MAS_product_5[0] + " - $" + MAS_product_5[2]),
                                font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product5.grid(row=5, column=0)

        MAS_product5_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product5_button)
        MAS_product5_button.grid(row=5, column=1, pady=5)

        #code for MAS_product6
        MAS_product6 = tk.Label(MAS_window,
                            text= (MAS_product_6[0] + " - $" + MAS_product_6[2]),
                                font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product6.grid(row=6, column=0)

        MAS_product6_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product6_button)
        MAS_product6_button.grid(row=6, column=1, pady=5)

        #code for MAS_product7
        MAS_product7 = tk.Label(MAS_window,
                            text= (MAS_product_7[0] + " - $" + MAS_product_7[2]),
                                font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product7.grid(row=7, column=0)

        MAS_product7_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product7_button)
        MAS_product7_button.grid(row=7, column=1, pady=5)

        #code for MAS_product8
        MAS_product8 = tk.Label(MAS_window,
                            text= (MAS_product_8[0] + " - $" + MAS_product_8[2]),
                                font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product8.grid(row=8, column=0)

        MAS_product8_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product8_button)
        MAS_product8_button.grid(row=8, column=1, pady=5)

        #code for MAS_product9
        MAS_product9 = tk.Label(MAS_window,
                            text= (MAS_product_9[0] + " - $" + MAS_product_9[2]),
                                font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product9.grid(row=9, column=0)

        MAS_product9_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                        font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product9_button)
        MAS_product9_button.grid(row=9, column=1, pady=5)

        #code for MAS_product10
        MAS_product10 = tk.Label(MAS_window,
                            text= (MAS_product_10[0] + " - $" + MAS_product_10[2]),
                                 font =('Arial'),
                            bg = 'black',
                            fg = 'red',
                            justify="left")
        MAS_product10.grid(row=10, column=0)

        MAS_product10_button = tk.Button(MAS_window,
                                       text = 'Add to Cart',
                                         font = ('Arial'),
                                     bg = 'red',
                                    fg = 'yellow',
                                       command = self.MAS_product10_button)
        MAS_product10_button.grid(row=10, column=1, pady=5)

        #code for the label detailing the website
        MAS_info = tk.Label (MAS_window,
                            text = "Mad About Science (Space Category) \n https://www.madaboutscience.com.au/shop/science-fun.html?cat=16&p=2",
                             font = ('Arial', 15, 'italic'),
                             bg = 'black',
                             fg = 'yellow')
        MAS_info.grid(row=11,column=0,columnspan=2, padx=20, pady=20)


        #buttons that convert their lists into
        #html syntax, which is added to invoice_contents

    def MAS_product1_button(self):
        MAS_P1_contents = []
        MAS_P1_contents.append('<tr><td>' + MAS_product_1[0] + '</td>')
        MAS_P1_contents.append('<td><img src=' + MAS_product_1[1] + ' width="200" height="200"></td>')
        MAS_P1_contents.append('<td>$' + MAS_product_1[2] + '</td></tr>')
        invoice_contents.append(MAS_P1_contents)
        invoice_prices.append(MAS_product_1[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_1[0])
        database_prices.append( MAS_product_1[2])

    def MAS_product2_button(self):
        MAS_P2_contents = []
        MAS_P2_contents.append('<tr><td>' + MAS_product_2[0] + '</td>')
        MAS_P2_contents.append('<td><img src=' + MAS_product_2[1] + ' width="200" height="200"></td>')
        MAS_P2_contents.append('<td>$' + MAS_product_2[2] + '</td></tr>')
        invoice_contents.append(MAS_P2_contents)
        invoice_prices.append(MAS_product_2[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_2[0])
        database_prices.append( MAS_product_2[2])

    def MAS_product3_button(self):
        MAS_P3_contents = []
        MAS_P3_contents.append('<tr><td>' + MAS_product_3[0] + '</td>')
        MAS_P3_contents.append('<td><img src=' + MAS_product_3[1] + ' width="200" height="200"></td>')
        MAS_P3_contents.append('<td>$' + MAS_product_3[2] + '</td></tr>')
        invoice_contents.append(MAS_P3_contents)
        invoice_prices.append(MAS_product_3[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_3[0])
        database_prices.append( MAS_product_3[2])

    def MAS_product4_button(self):
        MAS_P4_contents = []
        MAS_P4_contents.append('<tr><td>' + MAS_product_4[0] + '</td>')
        MAS_P4_contents.append('<td><img src=' + MAS_product_4[1] + ' width="200" height="200"></td>')
        MAS_P4_contents.append('<td>$' + MAS_product_4[2] + '</td></tr>')
        invoice_contents.append(MAS_P4_contents)
        invoice_prices.append(MAS_product_4[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_4[0])
        database_prices.append( MAS_product_4[2])

    def MAS_product5_button(self):
        MAS_P5_contents = []
        MAS_P5_contents.append('<tr><td>' + MAS_product_5[0] + '</td>')
        MAS_P5_contents.append('<td><img src=' + MAS_product_5[1] + ' width="200" height="200"></td>')
        MAS_P5_contents.append('<td>$' + MAS_product_5[2] + '</td></tr>')
        invoice_contents.append(MAS_P5_contents)
        invoice_prices.append(MAS_product_5[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_5[0])
        database_prices.append( MAS_product_5[2])

    def MAS_product6_button(self):
        MAS_P6_contents = []
        MAS_P6_contents.append('<tr><td>' + MAS_product_6[0] + '</td>')
        MAS_P6_contents.append('<td><img src=' + MAS_product_6[1] + ' width="200" height="200"></td>')
        MAS_P6_contents.append('<td>$' + MAS_product_6[2] + '</td></tr>')
        invoice_contents.append(MAS_P6_contents)
        invoice_prices.append(MAS_product_6[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_6[0])
        database_prices.append( MAS_product_6[2])

    def MAS_product7_button(self):
        MAS_P7_contents = []
        MAS_P7_contents.append('<tr><td>' + MAS_product_7[0] + '</td>')
        MAS_P7_contents.append('<td><img src=' + MAS_product_7[1] + ' width="200" height="200"></td>')
        MAS_P7_contents.append('<td>$' + MAS_product_7[2] + '</td></tr>')
        invoice_contents.append(MAS_P7_contents)
        invoice_prices.append(MAS_product_7[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_7[0])
        database_prices.append( MAS_product_7[2])

    def MAS_product8_button(self):
        MAS_P8_contents = []
        MAS_P8_contents.append('<tr><td>' + MAS_product_8[0] + '</td>')
        MAS_P8_contents.append('<td><img src=' + MAS_product_8[1] + ' width="200" height="200"></td>')
        MAS_P8_contents.append('<td>$' + MAS_product_8[2] + '</td></tr>')
        invoice_contents.append(MAS_P8_contents)
        invoice_prices.append(MAS_product_8[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_8[0])
        database_prices.append( MAS_product_8[2])

    def MAS_product9_button(self):
        MAS_P9_contents = []
        MAS_P9_contents.append('<tr><td>' + MAS_product_9[0] + '</td>')
        MAS_P9_contents.append('<td><img src=' + MAS_product_9[1] + ' width="200" height="200"></td>')
        MAS_P9_contents.append('<td>$' + MAS_product_9[2] + '</td></tr>')
        invoice_contents.append(MAS_P9_contents)
        invoice_prices.append(MAS_product_9[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_9[0])
        database_prices.append( MAS_product_9[2])

    def MAS_product10_button(self):
        MAS_P10_contents = []
        MAS_P10_contents.append('<tr><td>' + MAS_product_10[0] + '</td>')
        MAS_P10_contents.append('<td><img src=' + MAS_product_10[1] + ' width="200" height="200"></td>')
        MAS_P10_contents.append('<td>$' + MAS_product_10[2] + '</td></tr>')
        invoice_contents.append(MAS_P10_contents)
        invoice_prices.append(MAS_product_10[2])
        #adds details to the database list to add to the SQL database
        database_products.append(MAS_product_10[0])
        database_prices.append( MAS_product_10[2])


        
    def invoice(self):

        if not invoice_contents:
            invoice_contents.append(
                '<h2 style="color:yellow;font-family:roboto"> Nothing in Shopping Cart, try again</h2>')
        
        price_floats = []
        for price in invoice_prices:
            price_floats.append(float(price))
        total_price = sum(price_floats)
        
        invoice_file = open('invoice.html', 'w', encoding = 'UTF-8')

        invoice_file.write((
            '''<!DOCTYPE html>
            <html>
                <head>
                    <title>Astro Shop Invoice</title>
                </head>
                <body background="darkspace.jpg">
                <h1 style="color:yellow;font-family:roboto">Astro Shop Invoice</h1>
                <h2><img src = "https://thumbs.gfycat.com/ScrawnyAdorableBlackbird-size_restricted.gif"></h2>
                <h3 style="color:yellow;font-family:roboto">Shopping Cart Total Price = $%f</h3>
                <table style="color:yellow;font-family:roboto"><tr><th>Product Title</th><th>Product Image</th><th>Product Price</th></tr>
                %s
                </body>

                <table>
                <p style="color:yellow;font-family:roboto"> Our Trending Products can be found here:<br>
                Space Store - https://thespacestore.com/collections/trending-now<br>
                Ebay RSS Feed - https://www.ebay.com.au/sch/i.html?&_nkw=solar+system+posters&_rss=1<br>
                </p>
                
                <p style="color:yellow;font-family:roboto"> Our Favourite Products can be found here:<br>
                Bintel - https://www.bintel.com.au/product-category/telescopes/beginner/<br>
                Mad About Science - https://www.madaboutscience.com.au/shop/science-fun.html?cat=16&p=2<br>
                </p>
                </table>
                
            </html>
            ''')%((round(total_price,2)),(invoice_contents)))

        invoice_file.close()

        #part of the invoice function that attempts to edit the SQL database

        #connects to the database
        connection = connect(database = "shopping_cart.db")

        #puts a cursor in the database
        c = connection.cursor()

        #clears the database before entering in new invoice information
        c.execute("UPDATE ShoppingCart SET Item = NULL")
        connection.commit()

        c.execute("UPDATE ShoppingCart SET Price = NULL")
        connection.commit()

        c.execute("DELETE FROM ShoppingCart WHERE Item IS NULL")
        connection.commit()

        c.execute("DELETE FROM ShoppingCart WHERE Price IS NULL")
        connection.commit()

        #SQL insert query for the invoice information
        #cycles through using the length of one of the lists
        #because they should both be the same length by design
        for item in range(len(database_products)): 
            c.execute("INSERT INTO ShoppingCart VALUES (?,?)",(database_products[item],
                                                           database_prices[item]))
        connection.commit()
        
        #close cursors and connections
        c.close()
        connection.close()
        
        
#code for the main loop of the program
if __name__ == "__main__":
    root = tk.Tk()
    root.title('ASTRO SHOP')
    root.configure(background = 'black')
    view = View(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()

# Name of the invoice file. To simplify marking, your program should
# generate its invoice using this file name.
invoice_file = 'invoice.html'

