<h1>Html to PDF flask microservice</h1>
<h2>Activation:</h2>
<p>&bull; Install wkhtmltopdf and configur 'PATH_TO_HTML_TO_PDF' environment variable as path to wkhtmltopdf</p>

<p>&bull; Run the app, see requests.json for templates</p>
<p>&bull; The app can either return a pdf file or keep it as a file on the server</p>
<p>&bull; Set env var: MAX_SUPPORTED_FILE_COUNT to regulate the number of files on the server</p>


<h4>Docker Use</h4>
<p>&bull; docker build -t tagname . </p>
<p>&bull; docker run -it -p <\port>:5000 tagname </p>
<p> docker run --env-file=env.env -it -p 5000:5000 -t tagname </p>
