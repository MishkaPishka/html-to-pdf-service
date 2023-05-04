FROM python:3.8

RUN wget https://s3.amazonaws.com/shopify-managemant-app/wkhtmltopdf-0.9.9-static-amd64.tar.bz2
RUN tar xvjf wkhtmltopdf-0.9.9-static-amd64.tar.bz2
RUN mv wkhtmltopdf-amd64 /usr/local/bin/wkhtmltopdf
RUN chmod +x /usr/local/bin/wkhtmltopdf

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PATH_TO_HTML_TO_PDF="/usr/local/bin/wkhtmltopdf"
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
