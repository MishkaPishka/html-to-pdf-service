<h1>Html to PDF flask microservice</h1>
<h2>Info:</h2>
<p>A rest api that converts html to PDF</p>
<p>HTML's can be styled according to templates that the user uploads</p>
<p>Pdf's can be stored locally on the server, uploaded to AWS, or return as response</p>
<h2>Local Activation:</h2>
<p>&bull; Install wkhtmltopdf and configur 'PATH_TO_HTML_TO_PDF' environment variable as path to wkhtmltopdf</p>

<p>&bull; Run the app, see requests.json for templates</p>
<p>&bull; The app can either return a pdf file or keep it as a file on the server</p>
<p>&bull; Set env var: MAX_SUPPORTED_FILE_COUNT to regulate the number of files on the server</p>
<p>&bull; For AWS use, set AWS_REGION,AWS_BUCKET_NAME,AWS_SECRET_KEY,AWS_ACCESS_KEY
</p>

<h2>Docker Use</h2>
<p>&bull; docker build -t tagname . </p>
<p>&bull; docker run -it -p <\port>:5000 tagname </p>
<p>&bull; For AWS use: docker run --env-file=env.env -it -p 5000:5000 -t tagname </p>
