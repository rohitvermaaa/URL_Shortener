# URL Shortener App

The **URL Shortener App** is a simple Python application built using the **tkinter** library for creating a graphical user interface (GUI). It allows users to shorten long URLs quickly and conveniently. Here's a brief overview of the application:

## Features

- **User-Friendly Interface**: The app provides a clean and user-friendly interface for entering long URLs.

- **URL Shortening**: It uses the [pyshorteners](https://github.com/ellisonleao/pyshorteners) library to shorten URLs using popular URL shortening services like TinyURL.

- **Clipboard Copy**: Users can easily copy the shortened URL to their clipboard with the click of a button.

## Prerequisites

Before you can run this application, make sure you have the following requirements met:

- Python 3.x installed on your system.
- Required Python libraries: `tkinter`, `pyshorteners`, and `pyperclip`.

## How to Run

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where you have saved the app files.

4. Run the following command to start the application:

   ```
   python url_shortener.py
   ```

5. The app's graphical user interface should open, allowing you to use the URL shortening functionality.

## Usage

1. Launch the application by following the "How to Run" instructions.

2. Enter the long URL you want to shorten in the "Enter the link:" field.

3. Click the "Shorten Link" button to generate the shortened URL.

4. The shortened URL will be displayed in the "Shortened Link:" field.

5. To copy the shortened URL to your clipboard, click the "Copy to Clipboard" button.

6. The button text will change to "Copied!" to confirm that the URL has been copied to the clipboard.

7. You can now paste the shortened URL wherever you need it.

## Customization

- You can customize the appearance of the application by modifying the colors, fonts, and styles in the `create_widgets` method of the `URLShortenerApp` class.

- To use a different URL shortening service or customize the URL format, you can explore the options provided by the [pyshorteners](https://github.com/ellisonleao/pyshorteners) library.

## Author

Rohit

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This application was created using Python and the tkinter library.
- URL shortening is powered by the pyshorteners library.
- Clipboard functionality is achieved with pyperclip.

Feel free to enhance and customize this application according to your needs. Enjoy URL shortening with this simple tool!
