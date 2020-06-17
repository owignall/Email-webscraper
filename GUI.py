'''
This scipt runs a simple GUI for using the email scraper.
Potential improvements
- Loading bar
- Some explaination labels
- Improve styling
'''
from tkinter import *
from tkinter import font
import email_scraper

def main():
    def scrape(url):
        print(url)
        for result in results:
            result.destroy()
        root.update
        emails = email_scraper.find_site_emails(url)
        results_text = Text(results_list, font=('OpenSymbol', 10), bg='white')
        for email in emails:
            print(email)
            results_text.insert(INSERT, f"- {email}\n")
            results.append(results_text)
        results_text.place(relx = 0, rely=0, relwidth=1, relheight=1)
        root.update
    height = 600
    width = 800
    results = []
    # Main loop
    root = Tk()
    root.title("Email Webscraper")
    root.wm_iconbitmap("icon.ico")
    canvas = Canvas(root, height=height, width=width)
    canvas.pack()
    # Structure frames
    outer_frame = Frame(root, bg="#69c9c9")
    outer_frame.place(relx = 0, rely = 0, relwidth=1, relheight=1)
    inner_frame = Frame(outer_frame, bg="#69c9c9")
    inner_frame.place(relx = 0.05, rely = 0.05, relwidth=0.9, relheight=0.9)
    # Input and controls area
    input_frame = Frame(inner_frame, bg="#A6A6A6", highlightbackground="black", highlightthickness=1)
    input_frame.place(x = 0, y = 0, relwidth=1, height=70)
    # Componets
    url_entry = Entry(input_frame, font=('OpenSymbol', 10), highlightbackground="black", highlightthickness=1)
    url_entry.place(relx=0.05, y=20, relwidth=0.7, height=30)
    enter = Button(input_frame, text='Scrape', font=('OpenSymbol', 10), command=lambda: scrape(url_entry.get()), highlightbackground="black", highlightthickness=1)
    enter.place(relx=0.8, y=20, relwidth=0.15, height=30)
    # Results area
    results_frame = Frame(inner_frame, bg="#A6A6A6", highlightbackground="black", highlightthickness=1)
    results_frame.place(relx = 0, y = 100, relwidth=1, height=400)
    results_list = Frame(results_frame, bg='white', highlightbackground="black", highlightthickness=1)
    results_list.place(relx = 0.05, y=20, relwidth=0.9, height=360)
    root.mainloop()

if __name__ == "__main__":
    main()