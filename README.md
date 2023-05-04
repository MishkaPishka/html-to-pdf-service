<h1>Html to PDF flask microservice</h1>
<h2>Activation:</h2>
<p>&bull; Install wkhtmltopdf and configur 'PATH_TO_HTML_TO_PDF' environment variable as path to wkhtmltopdf</p>

<p>&bull; Run the app, see requests.json for templates</p>
<p>&bull; The app can either return a pdf file or keep it as a file on the server</p>
<p>&bull; Set env var: MAX_SUPPORTED_FILE_COUNT to regulate the number of files on the server</p>



docker run -it -p 5000:5000 wkhtml1