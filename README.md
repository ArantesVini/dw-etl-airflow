# Data Warehouse ETL process with Apache Airflow

---

With this project I will extract, transform and load Data into a Data Warehouse database created using Docker and Postgres.
Pipelines and Data Warehousing process of a Data Engineer's life, lovely.

---

This project is made as a activity of the Data Engineering course, Design and Implementation of Data Warehouses, by Data Science Academy.

---

Softwares used to this:

- postgres docker image on dockerhub: `https://hub.docker.com/_/postgres` or with command `docker pull postgres`;\
- Anaconda python: `https://www.anaconda.com`;\
- pgAdmin: `https://www.pgadmin.org`\
- Apache Airflow: ``\

---

WIth postgres image I create the databse through Docker using the command:\
`docker run --name dsalabdw -p 5433:5432 -e POSTGRES_USER=vinicius_arantes -e POSTGRES_PASSWORD=vini170500 -e POSTGRES_DB=dwdb -d postgres`\

After created, I create the pgAdmins server, a new database called `dwdb` and a new schema called `dsalabdw`\
